
import requests
from geopy.geocoders import Nominatim
import geocoder

def get_current_location():
    response = requests.get('https://ipapi.co/json/')
    data = response.json()
    latitude = data['latitude']
    longitude = data['longitude']
    # print(latitude,longitude)
    return latitude,longitude

async def get_current_location1():
    g =geocoder.ip('me')
    if g.ok:
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        return latitude, longitude
    else:
        print(g)
        return None, None
    
    
def get_city_name():
    latitude, longitude = get_current_location()
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.reverse((latitude, longitude), language='en')
    city = location.raw['address'].get('city', '')
    
    return city

async def get_city_and_village():
    latitude, longitude = get_current_location()
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.reverse((latitude, longitude), language='en')
    
    city = location.raw['address'].get('city') or location.raw['address'].get('town')
    village = location.raw['address'].get('village') or location.raw['address'].get('hamlet') or location.raw['address'].get('locality')
    # print(location.raw['address'])
    return city, latitude,longitude


def reverse_geocode(latitude, longitude):
    try:
        geoLoc = Nominatim(user_agent="GetLoc")
        location = geoLoc.reverse((latitude, longitude))
        if location and 'address' in location.raw:
            city = location.raw['address'].get('city') or location.raw['address'].get('town') or location.raw['address'].get('village')
            return city if city else "City not found"
        else:
            return "Location not found"
    except Exception as e:
        return f"Error: {e}"
import requests

def get_village():
    lat, lon = get_current_location()
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Check if 'village' exists in the address
        village = data.get('address', {}).get('village', 'Not found')
        return village
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

