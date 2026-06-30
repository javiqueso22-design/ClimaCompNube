import requests

def buscar_ciudades(nombre_ciudad):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={nombre_ciudad}&count=5&language=es&format=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "results" in data:
                return data["results"]
    except Exception as e:
        print(f"Error al buscar ciudad: {e}")
    
    return []

def obtener_clima(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error al obtener clima: {e}")
        
    return None