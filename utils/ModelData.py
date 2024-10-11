import requests
# api_key = '61b0b632a8544dcb8bb93704242909' #worldweather
# url = f'http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={CITY}&fx=no&gb-defra-index=Band&format=json'#worldweather

# api_key1 = '8a1b6e70490e41ddf5a53b131acbc60c' #open weather
# URL = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key1}&units=metric"#open weather
import datetime

class ModelData:
    def __init__(self, city, latitude, longitude,ph_level,soil_type):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.soil_type = soil_type
        self.ph_level = ph_level
        self.conditions =[]
        api_key = '61b0b632a8544dcb8bb93704242909'
        api_key1 = '8a1b6e70490e41ddf5a53b131acbc60c'
        self.url = f'http://api.worldweatheronline.com/premium/v1/weather.ashx?key={api_key}&q={city}&fx=no&gb-defra-index=Band&format=json'#worldweather
        self.URL = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key1}&units=metric"#open weather
    
    async def getModelData(self):
        
        response = requests.get(self.url)
        data1 = response.json()
        # print(data1)
        
        response = requests.get(self.URL)
        data = response.json()
        # print(data)

        # Extract weather conditions openweather 
        humidity = data['main']['humidity']
        ## Extract weather conditions worldweather
        avrainfall = float(data1['data']['ClimateAverages'][0]['month'][8]['avgDailyRainfall'])
        ava_temparature = float(data1['data']['current_condition'][0]['temp_C'])
        wind_d = data1['data']['current_condition'][0]['windspeedMiles']
        wind_d = int(wind_d)
        if wind_d < 5:
            wind_category = 0
        elif 5 <= wind_d <= 15:
            wind_category = 1
        else:
            wind_category = 2
        current_month = datetime.datetime.now().month

        if 10 <= current_month <= 3:  # Summer months in the Southern Hemisphere
            sunlight_hours = 10 + (2 * (datetime.datetime.now().day % 2))  # Between 10-12 hours
        else:  # Winter months
            sunlight_hours = 8 + (2 * (datetime.datetime.now().day % 2))  # 
        # print(data1['data']['current_condition'][0]['windspeedMiles'])
        # Example with fetched data
        # new_conditions = [[ava_temparature, avrainfall * 30, self.ph_level, humidity, 7, 1, self.soil_type]]
        new_conditions = [[ava_temparature, avrainfall * 30, self.ph_level, humidity, sunlight_hours, wind_category, self.soil_type]]  
        self.conditions = new_conditions
        # print(new_conditions)
        