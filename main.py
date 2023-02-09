import sys
import requests
from support import get_spn
from io import BytesIO
from PIL import Image

toponym_to_find = ' '.join(sys.argv[1:])

geocoder_address = 'http://geocode-maps.yandex.ru/1.x/'
geocoder_params = {
    'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
    'geocode': toponym_to_find,
    'format': 'json'}

response = requests.get(geocoder_address, params=geocoder_params).json()
toponym = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
ll = toponym['Point']['pos'].replace(' ', ',')

map_api_address = 'http://static-maps.yandex.ru/1.x/'
map_params = {
    'll': ll,
    'spn': get_spn(toponym['boundedBy']['Envelope']),
    'l': 'map',
    'pt': f'{ll},vkbkm'
}

response = requests.get(map_api_address, params=map_params)
Image.open(BytesIO(response.content)).show()
