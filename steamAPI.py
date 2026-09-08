"""Consulta y organiza los juegos de una cuenta de Steam.

El programa utiliza la API de Steam para:
- Obtener los juegos del usuario.
- Consultar si un juego pertenece a la biblioteca.
- Mostrar el AppID de cada juego.
- Agrupar los juegos según su género.
- Mostrar los juegos que no tienen género disponible.

Configuración requerida:
    Las variables ``steam_api_key`` y ``steam_id`` deben estar guardadas
    dentro de un archivo ``.env``.
"""

import os, requests
from dotenv import load_dotenv 

load_dotenv()

# Credenciales necesarias para consultar la biblioteca del usuario.
steam_api_key = os.getenv('steam_api_key')
steam_id = os.getenv('steam_id')

if not steam_api_key or not steam_id:
    raise ValueError('Faltan STEAM_API_KEY o STEAM_ID en el archivo .env')

url = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'
# Datos enviados a la API para solicitar la biblioteca con sus nombres.
parametros = {
    'key': steam_api_key,
    'steamid': steam_id,
    'format': 'json',
    'include_appinfo': 'true'
}

response = requests.get(url, params=parametros)
json = response.json()

cantidad = json['response']['game_count']

# Estructuras utilizadas para organizar la información de los juegos.
lista_juegos = []
lista_id_juegos = []
lista_genero = []
lista_sin_genero = []
categoria_juegos = {}
diccionario_categorias = {}


for juegos in json['response']['games']:
    nombre = juegos['name']
    appid = juegos['appid']

    lista_juegos.append(juegos['name'])
    lista_id_juegos.append(juegos['appid'])
    # print(juegos['name'])
    categoria_juegos[nombre] = appid


    # Consultar los géneros asociados al AppID actual.
    url_juego = f'https://store.steampowered.com/api/appdetails?appids={appid}&l=spanish'
    response_juego = requests.get(url_juego)
    json_categoria = response_juego.json()
    categoria = json_categoria[str(appid)]['data'].get('genres', [])

    contador = 0
    if len(categoria) == 0:
        #print(f'{nombre} no tiene genero')
        contador +=1
        lista_sin_genero.append([nombre,categoria])
    else:
        for genero in categoria:
            nombre_categoria = genero['description']
            lista_genero.append([nombre, nombre_categoria, appid])
            #print(nombre, ' - ', nombre_categoria, ' - ', appid)
            #print(categoria, appid)
            if nombre_categoria not in diccionario_categorias:
                    diccionario_categorias[nombre_categoria] = []
            # Cada género funciona como clave y contiene una lista de juegos.
            diccionario_categorias[nombre_categoria].append(nombre)
            #print(diccionario_categorias)
# Menú principal del programa.
print('(1) cantidad de juegos: ')
print('(2) consulta juego: ')
print('(3) listar juegos(nombre): ')
print('(4) listar juegos(nombre y id): ')
print('(5) listar juegos(nombre , id y categoria): ')
print('(6) consultar juegos por categoria: ') 
print('(7) consultar juegos sin categoria: ')
print('(0) salir')
opcion = int(input('opcion: ')) 

while opcion != 0:
       
    if opcion == 1:
        print(cantidad)
    elif opcion == 2:
        consulta_juego = input('ingrese juego: ')
        if consulta_juego in lista_juegos:
            print('juego en inventario')
        else:
            print('juego no existe en inventario')
    elif opcion == 3:
        for nombre_juego in lista_juegos:
            print(nombre_juego) 
            #print(f'lista de juegos: \n {lista_juegos}')
    elif opcion == 4:
        # for nombre, appid in categoria_juegos.items():
        #     print(f'{nombre} - AppID: {appid}')
        for clave in categoria_juegos:
            print(clave, categoria_juegos[clave])
    elif opcion == 5:
        for cnid in lista_genero:
            print(cnid)
    elif opcion == 6:
        for nombre_categoria in diccionario_categorias:
            print(f'\n {nombre_categoria}')
            for nombre in diccionario_categorias[nombre_categoria]:
                print(f'{nombre}')
    elif opcion == 7:
            for sin_categoria in lista_sin_genero:
                print(sin_categoria[0])
    elif opcion == 0:
        break
    opcion = int(input('opcion: ')) 
