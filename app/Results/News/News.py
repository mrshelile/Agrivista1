import flet as ft
# from time import sleep

def News(page:ft.Page):
    
    lv = ft.ListView(expand=1, spacing=10, padding=5, auto_scroll=True)

    count = 1


    for i in range(0, 60):
        # sleep(1)
        lv.controls.append(
            ft.ListTile(
            leading=ft.Icon(ft.icons.INFO_OUTLINE),
            title=ft.Text("Maize, a versatile and resilient crop, is well-suited for Lesotho's conditions. By following proper practices, farmers can increase yields and contribute to food security."
                          ,size=18,style=ft.TextStyle(color=ft.colors.BLACK87)),
                        )
        )
        count += 1
        page.update()
    
    body = ft.Container(
        height=710,
        width=380,
        # bgcolor=ft.colors.BLUE_600,
        content=lv
    )
    body = ft.Column(
        [   
            ft.Container(height=10),
            ft.Container(
                border_radius=ft.border_radius.only(20,20,0,0),
                width=380,
                height=200,
                content=ft.Image("https://i.ibb.co/Xb5tmJH/farming.jpg",
                fit=ft.ImageFit.COVER)
                ),
            body,
        ]
    )
    return body