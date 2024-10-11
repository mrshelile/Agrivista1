import flet as ft
from constants import constants
width = 180
height = 230

boxbgcolor = "#8FAA97"
def CropInfo(page:ft.Page,margin,changes):
    
    body = ft.Row(
        [   
            
            ft.Container(
                border_radius=15,
                width=width,
                height=height,
                bgcolor=boxbgcolor,
                content=ft.Column(
                    [   ft.Container(height=10),
                        ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("Estimate Margin",size=18,color=ft.colors.GREEN_900),
                            ),
                        ft.Container(
                            height=120,
                            margin=ft.margin.only(left=15),
                            content=ft.Image(constants.iconUp if margin>50 else constants.iconDown),
                            ),
                       ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text(f"{margin:.2f}%",size=18,color=ft.colors.GREEN_900),
                            ),
                    ]
                )
                ),
            
            ft.Container(
                border_radius=15,
                width=width,
                height=height,
                bgcolor=boxbgcolor,
                content=ft.Column(
                    [   ft.Container(height=10),
                        ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("Chances",size=18,color=ft.colors.GREEN_900),
                            ),
                        ft.Container(
                            height=120,
                            margin=ft.margin.only(left=15),
                            content=ft.Image(constants.iconUp if changes>10 else constants.iconDown),
                            ),
                       ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text(f"{changes:.2f}%",size=18,color=ft.colors.GREEN_900),
                            ),
                    ]
                )
                ),
        ]
    )
    body = ft.Container(
        content=body,
        # bgcolor=ft.colors.GREEN_200,
        width=370,
    )
    return body


def buildChanges(value,icon):
    return ft.Container(
                border_radius=15,
                width=width,
                height=height,
                bgcolor=boxbgcolor,
                content=ft.Column(
                    [   ft.Container(height=10),
                        ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text("Chances",size=18,color=ft.colors.GREEN_900),
                            ),
                        ft.Container(
                            height=120,
                            margin=ft.margin.only(left=15),
                            content=ft.Image(icon),
                            ),
                       ft.Container(
                            margin=ft.margin.only(left=20),
                            content=ft.Text(f"{value:.2f}%",size=18,color=ft.colors.GREEN_900),
                            ),
                    ]
                )
                )