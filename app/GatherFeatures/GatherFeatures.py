import flet as ft
import numpy as np
from model.crop_prediction import CropPrediction
from utils import Location
from utils import ModelData
from constants import constants
import asyncio
from model.marketPrediction import MarketModel


def GatherFeatures(page: ft.Page):
    isLoading =False  # No need to pass a type, just initialize as ft.Ref()
    
    # cropMarket = MarketModel()
    
# Loading spinner

    
 
    async def evalutate(e):
        # nonlocal cropMarket
        nonlocal isLoading
        nonlocal btn
        nonlocal loading_row
     
        isLoading =True
        # if isLoading:
        btn.opacity=0
        loading_row.opacity=1
        btn.height=0
        # else:
        #     btn.height=50
        #     loading_row.opacity=0
        #     btn =1
        # print(loading_row)
        
        page.update()  # Trigger UI update to show loading

        await asyncio.sleep(0.1)  # Briefly yield control

        try:
            # Proceed with long-running tasks
            city, lat, lon = await Location.get_city_and_village()
            
            model_data = ModelData.ModelData(city, lat, lon, float(ph.value), int(soil_type.value))
            await model_data.getModelData()
            
                
            model = CropPrediction()
            await model.load_model()
            await model.make_prediction(model_data.conditions)
            await model.predict_market()
            # await cropMarket.load_model()
            if model.top_3_crops and not model.marketPredictionData.empty :
                page.session.set("top_3_crops", model.top_3_crops)
                
                page.go("/home")
        except Exception as e:
            print(f"Error during evaluation: {e}")
        finally:
            isLoading = False  # Set loading state back to False
             # Trigger UI update to hide loading
            btn.height=50
            btn.opacity =1
            loading_row.opacity=0
            page.update() 

    def loading():
        loading_spinner = ft.ProgressRing(
        width=25,
        height=30,
        color=ft.colors.GREEN_300,
        stroke_width=10
        )
        loading_spinner_container = ft.Container(
            margin=ft.margin.only(left=15),
            border_radius=10,
            content=loading_spinner
        )
        loading_row = ft.Container(
            opacity=0,
            content=ft.Row(
                controls=[
                    loading_spinner_container,
                    ft.Container(margin=5),
                    ft.Text("Processing...", style=ft.TextStyle(color=ft.colors.GREEN_700, size=20, weight=ft.FontWeight.BOLD))
                    
                ]
            )
        )
        return loading_row
    loading_row = loading()
    # Logo definition
    logo = ft.Image(
        src=constants.logo1,
        width=None,
        height=None,
        fit=ft.ImageFit.COVER,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(30),
    )
    logo = ft.CircleAvatar(
        content=logo,
        width=150,
        height=150,
        bgcolor=ft.colors.GREEN_300,
    )

    # Form elements
    ph = ft.TextField(
        keyboard_type=ft.KeyboardType.NUMBER,
        prefix_icon=ft.icons.SCALE,
        prefix_style=ft.TextStyle(bgcolor=ft.colors.GREEN_500),
        label="Enter Soil PH Level",
        label_style=ft.TextStyle(color=ft.colors.GREEN_500),
        text_size=15,
        height=70,
        color=ft.colors.GREEN_500,
        bgcolor=ft.colors.WHITE,
        filled=True,
        border=ft.InputBorder.NONE,
        border_color=ft.colors.CYAN_500,
    )
    
    soil_type = ft.Dropdown(
        options=[
            ft.dropdown.Option(0, "Loam"),
            ft.dropdown.Option(1, "Sandy loam"),
        ],
        label="Choose Soil Type",
        label_style=ft.TextStyle(color=ft.colors.GREEN_500),
        height=80,
        filled=True,
        border_color=ft.colors.GREEN_500,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.GREEN_500,
        prefix_icon=ft.icons.ENERGY_SAVINGS_LEAF, 
    )

    btn = ft.FilledButton(
            "Evaluate",
            style=ft.ButtonStyle(
                bgcolor=ft.colors.GREEN_300,
                shape=ft.RoundedRectangleBorder(radius=30),
            ),
            on_click=evalutate,
        )
    # Updateable form
    def build_form():
        nonlocal btn
        return ft.ListView(
            
            controls=[
                ph,
                ft.Container(height=50),
                soil_type,
                ft.Container(height=30),  # Space between fields
                btn,
                loading_row
            ]
        )

    # Main form container
    form_container = ft.Container(
        margin=ft.margin.only(left=20, top=50, right=20, bottom=30),
        border_radius=30,
        width=270,
        content=build_form()  # Load the form with dynamic content
    )

    # Card container
    form_card = ft.Card(
        margin=ft.margin.only(left=30),
        content=form_container,
        color="#EBEEF3",
    )

    # Page layout
    return [
        ft.Container(content=ft.Text(""), height=40),
        logo,
        ft.Container(content=ft.Text(""), height=30),
        form_card,
    ]