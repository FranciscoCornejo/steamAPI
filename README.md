# Biblioteca de Steam con Python

Proyecto personal de aprendizaje de backend con Python, sin frameworks. El
programa consulta la biblioteca de una cuenta mediante la API de Steam y
organiza los juegos utilizando listas y diccionarios.

## Funcionalidades actuales

El menú permite:

1. Mostrar la cantidad de juegos de la biblioteca.
2. Consultar si un juego pertenece a la biblioteca.
3. Listar los nombres de todos los juegos.
4. Listar el nombre y AppID.
5. Listar el nombre, AppID y género de los juegos.
6. Mostrar los juegos agrupados por género.
7. Mostrar los juegos que no tienen género disponible.
0. Salir del programa.

Un juego puede aparecer en más de un grupo porque Steam puede asignarle varios
géneros.

## Requisitos

- Python 3.
- Una clave de la API web de Steam.
- El SteamID de la cuenta que se desea consultar.
- Los paquetes `requests` y `python-dotenv`.

## Instalación

Desde una terminal ubicada en la carpeta del proyecto:

```powershell
python -m pip install -r requirements.txt
```

## Configuración

1. Copiar `.env.example` con el nombre `.env`.
2. Completar las variables con la clave y el SteamID correspondientes:

```env
steam_api_key=TU_CLAVE_DE_STEAM
steam_id=TU_STEAM_ID
```

El archivo `.env` está incluido en `.gitignore` para evitar publicar las
credenciales. No se debe escribir la clave real en el código, el README ni
`.env.example`.

Para que Steam entregue la biblioteca, los detalles de juegos del perfil deben
estar visibles para la consulta.

## Ejecución

```powershell
python steamAPI.py
```

El programa primero consulta los datos de todos los juegos. En bibliotecas
grandes, el menú puede tardar en aparecer porque la información de géneros se
solicita por separado para cada AppID.

## Estructura del proyecto

```text
SteamAPI/
├── steamAPI.py       # Programa principal y menú
├── API.py            # Prueba de consulta para un AppID específico
├── requirements.txt  # Dependencias de Python
├── .env.example      # Ejemplo de configuración sin datos privados
├── .env              # Credenciales locales; no se comparte
├── .gitignore        # Archivos excluidos del control de versiones
└── README.md          # Documentación del proyecto
```

## Datos utilizados en el programa

- `lista_juegos`: nombres de los juegos de la biblioteca.
- `lista_id_juegos`: AppID de cada juego.
- `lista_genero`: nombre, género y AppID de cada juego clasificado.
- `lista_sin_genero`: juegos cuya respuesta no contiene géneros.
- `categoria_juegos`: relaciona cada nombre con su AppID.
- `diccionario_categorias`: usa el género como clave y guarda como valor la
  lista de juegos asociados.

Ejemplo conceptual de `diccionario_categorias`:

```python
{
    "Acción": ["Counter-Strike 2", "Left 4 Dead 2"],
    "Simuladores": ["Euro Truck Simulator 2"]
}
```

## APIs consultadas

- `IPlayerService/GetOwnedGames`: entrega la biblioteca de la cuenta.
- `store.steampowered.com/api/appdetails`: entrega detalles como los géneros de
  un AppID.

## Estado del proyecto

El proyecto está en desarrollo y se utiliza para practicar solicitudes HTTP,
respuestas JSON, listas, diccionarios, ciclos y menús de consola en Python.
