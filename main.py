from app.GatherFeatures.GatherFeatures import GatherFeatures
from app.OnBoarding.Onboarding import  Onboarding
from constants.colors import *
from app.home.home import home
import flet as ft

def main(page: ft.Page):
    page.title = "AgriVista"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                Onboarding(page),   
                bgcolor=ft.colors.GREEN_200
            )
        )
     
        if page.route == "/gatherFeatures":
            page.views.append(
                ft.View(
                    "/gatherFeatures",
                    GatherFeatures(page),
                    bgcolor=ft.colors.WHITE
                )
            )
        
        if page.route == "/home":
            page.views.append(
                ft.View(
                    "/home",
                    home(page),
                    bgcolor=ft.colors.WHITE
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main,)
