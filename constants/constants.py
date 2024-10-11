import pandas as pd    
import flet as ft

logo = "https://i.ibb.co/xDXsfnK/spi.png"
logo1 = "https://i.ibb.co/7K3hpfZ/logo.png"

iconUp = "https://i.ibb.co/Zf3cdtL/up.png"
iconDown = "https://i.ibb.co/LtpMsQD/down.png"

def loadMarketResutl(page:ft.page):
    values = list(page.session.get("top_3_crops"))
    crops =""
    
    for crop_name,prob in values:
        crops +=  f"{crop_name}, "
    df = pd.read_csv("market.csv",header='infer')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df,crops