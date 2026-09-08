"""Prueba aislada de la consulta de géneros para el AppID 34330.

Este archivo permite observar la respuesta de la tienda de Steam para un
juego específico sin ejecutar el menú completo de 'steamAPI.py'.
"""

import os, requests

url_juego = f'https://store.steampowered.com/api/appdetails?appids=34330&l=spanish'
response_juego = requests.get(url_juego)
json_categoria = response_juego.json()
categoria = json_categoria['34330']['data']['genres']
print(categoria)
