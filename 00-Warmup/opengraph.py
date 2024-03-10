# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    # Definir el endpoint de la API de OpenGraph
    endpoint = "https://opengraph.lewagon.com/?url={}".format(url)
    
    # Realizar la solicitud HTTP GET a la API
    response = requests.get(endpoint)
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Retornar el contenido de la respuesta como un diccionario de Python
        data = response.json()
        return data.get('data')
    else:
        # Retornar None si la solicitud no fue exitosa
        return None

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.github.com"))