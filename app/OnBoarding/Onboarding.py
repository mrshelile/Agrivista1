import flet as ft
from constants.colors import * 
from constants import constants
# https://i.ibb.co/Ycm0SyT/removal-ai-40155078-242f-4d07-b8c8-4bd345e10eed-stronger-together-1-0-2456105835.png
def Onboarding(page:ft.Page):
    intro = "Welcome"
    # intro +="climate insights and market insights"
    text_intro = ft.Text(intro,style=ft.TextStyle(
        size=40,
        color=ft.colors.WHITE70,
        weight=ft.FontWeight.W_900,
    ))
    text_intro =ft.Container(
        content=text_intro,
        width=300,
        margin=ft.margin.only(left=100)
    )
    img = ft.Image(
        fit=ft.ImageFit.COVER,
        src=constants.logo)
    img = ft.Container(
        content=img,
        margin=ft.margin.only(left=20),
        width=330 ,
        height=480   
    )
    return [
        ft.Container(
        height=50,    
        ),
        text_intro,
        ft.Container(height=10),
        img,
        ft.Container(height=1),
        ft.Row(
            controls=[
            ft.Container(width=90),
            ft.ElevatedButton(
            style=ft.ButtonStyle(
                bgcolor=ft.colors.WHITE,
                shape=ft.StadiumBorder(),
            ),
            text="Continue here!",
            icon="park_rounded",
            icon_color="green400",
            on_click=lambda e: page.go("/gatherFeatures")
        ),
            ]
        )
        ]