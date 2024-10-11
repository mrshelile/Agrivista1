import flet as ft
# https://i.ibb.co/5jwXSDf/Spinach.jpg
def TopHeader(page:ft.Page,image):
    
    body = ft.Container(
        # image_src="",
        # bgcolor=ft.colors.BLUE_300,
        width=350,
        height=300,
        border_radius=ft.border_radius.only(40,40,0,0),
        content=ft.Image(
            fit=ft.ImageFit.COVER,
            src=image)
        )
    return body