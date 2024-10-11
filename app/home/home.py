import flet as ft
from app.Results.MarketAnalysis.MarketAnalysis import MarketAnalysis
from app.Results.ListDisplay.ListDisplay import ListDisplay
from app.Results.News.News import  News
import pandas as pd
from constants import constants

def home(page: ft.Page):
    if  page.session.get("top_3_crops")== None:
        page.go("/gatherFeatures")
    try:
        values = list(page.session.get("top_3_crops"))
    except:
        page.go("/gatherFeatures")
    
    page_number = 1
    
    def nav_selected(number):
        nonlocal page_number
        if number ==3:
            page.go("/gatherFeatures")
            return
        page_number = number
        update_button_colors()  # Update button colors when navigation is selected
        update_screen()  # Update the screen content
        page.update()

    def update_button_colors():
        # Update the background color of each button based on the selected page
        for idx, button in enumerate(buttons):
            button.bgcolor = ft.colors.CYAN_200 if page_number == idx + 1 else None
        page.update()  # Update the page after modifying button colors

    def update_screen():
        # Replace the content of the screen container with the corresponding screen
        screen_container.content = screens[page_number - 1]
        page.update()
    
    logo = ft.Image(
        src=constants.logo1,
        width=None,
        height=None,
        fit=ft.ImageFit.COVER,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=ft.border_radius.all(30),
    )
    # Create buttons
    buttons = [
        ft.Container(
            on_click=lambda e: nav_selected(1),
            margin=ft.margin.only(left=10),
            padding=ft.padding.all(3),
            bgcolor=ft.colors.CYAN_200 if page_number == 1 else None,  # Set initial color
            border_radius=5,
            content=ft.Row(controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.BLACK45,
                    content=ft.Icon(ft.icons.HOME_ROUNDED, size=40, color=ft.colors.WHITE)
                ),
                ft.Text("Home", style=ft.TextStyle(color=ft.colors.BLACK87, weight=ft.FontWeight.W_900))
            ])
        ),
        ft.Container(
            on_click=lambda e: nav_selected(2),
            margin=ft.margin.only(left=30),
            padding=ft.padding.all(6),
            border_radius=5,
            content=ft.Row(controls=[
                ft.CircleAvatar(
                    bgcolor=ft.colors.BLACK45,
                    content=ft.Icon(ft.icons.TRENDING_UP, size=40, color=ft.colors.WHITE)
                ),
                
                ft.Text("Trends", style=ft.TextStyle(color=ft.colors.BLACK87, weight=ft.FontWeight.W_900))
            ])
        ),
        ft.Container(
            on_click=lambda e: nav_selected(3),
            margin=ft.margin.only(left=20),
            padding=ft.padding.all(6),
            border_radius=5,
            content=ft.Row(controls=[
                ft.CircleAvatar(
                    # rotate=-90,
                    bgcolor=ft.colors.GREEN_300,
                    content=ft.Icon(ft.icons.EXIT_TO_APP)
                ),
                ft.Text("Back", style=ft.TextStyle(color=ft.colors.BLACK87, weight=ft.FontWeight.W_900))
            ])
        ),
    ]

    # Create bottom navigation
    bottomNav = ft.Row(controls=buttons)
    bottomNav = ft.Container(
        margin=ft.margin.only(top=730, left=-9, right=-9),
        bgcolor=ft.colors.GREEN_400,
        height=70,
        content=bottomNav
    )

    screens =[
        ListDisplay(page,values),
        MarketAnalysis(page),
        # News(page)
    ]

    # Create a container for the screen content
    screen_container = ft.Container(
        height=None,
        content=screens[page_number - 1]
    )

    body = ft.Stack(
        controls=[
            screen_container,
            bottomNav,
        ]
    )
    return [body]

# logo = ft.Image(
#         src=constants.logo1,
#         width=None,
#         height=None,
#         fit=ft.ImageFit.COVER,
#         repeat=ft.ImageRepeat.NO_REPEAT,
#         border_radius=ft.border_radius.all(30),
#     )