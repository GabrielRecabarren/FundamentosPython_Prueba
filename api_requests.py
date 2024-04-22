import requests

def get_birds_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error al obtener los datos de la API. Código de estado: {response.status_code}')
        return None
