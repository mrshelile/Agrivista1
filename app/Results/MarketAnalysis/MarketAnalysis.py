import matplotlib.pyplot as plt
import numpy as np
import flet as ft
from flet.matplotlib_chart import MatplotlibChart
import pandas as pd 
import json
import constants
import constants.constants



def MarketAnalysis(page: ft.Page):
    page.title = "Market Analysis"
    df,crops = constants.constants.loadMarketResutl(page)
    df_2024 = df[df.index.year == 2024]
    # # Data for months and crop margin performance
    # months = np.arange(1, 13)  # 12 months
    # maize_margin = np.random.uniform(20, 50, 12)  # Simulated margin for maize
    # spinach_margin = np.random.uniform(15, 35, 12)  # Simulated margin for spinach
    # wheat_margin = np.random.uniform(25, 55, 12)  # Simulated margin for wheat

    fig, ax = plt.subplots()

    # Plotting the data
    for crop in df_2024['Crop'].unique():

        crop_data = df_2024[df_2024['Crop'] == crop]
        plt.plot(crop_data.index.month, crop_data['Gross_Profit_Margin'], marker='o', label=crop)

    try:
        # Adding labels and title
        ax.set_xlabel("Months")
        ax.set_ylabel("Margin Performance (M)")
        ax.set_title("Simulated Crop Margin Performance Over Months")

        # Add a legend
        ax.legend(title="Crops")

        # Adding the plot to Flet page
        chart = MatplotlibChart(fig, expand=True)
        body = ft.Container(
            height=710,
            width=380,
            # bgcolor=ft.colors.BLUE_900
            content=ft.Column(
                [   ft.Container(height=80),
                    ft.Container(
                        margin=ft.margin.only(left=30),
                        content=ft.Text(f"Chart shows the monthly profit trends for  {crops}—quick insights at a glance!"
                        ,style=ft.TextStyle(color=ft.colors.GREEN_500,weight=ft.FontWeight.W_900,size=20))
                    ),chart
                ]
            )
        )
    except :
        return []
    return body