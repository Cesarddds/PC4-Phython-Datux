"""1. Bitcoin es una forma de moneda digital, también conocida como
criptomoneda. En lugar de depender de una autoridad central como un
banco, Bitcoin se basa en una red distribuida, también conocida como
cadena de bloques, para registrar transacciones.
En este problema debe generar un programa que realice:
- Solicite al usuario por línea de comando un valor de “n” el cual representa la cantidad
de bitcoins que posee el usuario.
- Consulte la API del índice de precios de Bitcoin de CoinDesk en el siguiente link
(https://api.coindesk.com/v1/bpi/currentprice.json), la cual retornará un objeto JSON,
entre cuyas claves anidadas encontrará el precio actual de Bitcoin como un número
decimal. Asegúrese de detectar cualquier excepción, como el siguiente código:
import requests
try:
...
except requests.RequestException:
...
- Muestra el costo actual de “n” Bitcoins en USD con cuatro decimales, usando , como
separador de miles.
Nota: El empleo de format string es apropiado para brindar formatos a nuestros datos. Le será
de utilidad el siguiente comando: print(f"${amount:,.4f}")
Recuerde instalar la librería Requests mediante el comando: pip install requests
Puede apoyarse de un formateador de json para que le facilite la busqueda de información:
https://jsonformatter.curiousconcept.com/#"""import requests

n = float(input("Ingrese la cantidad de bitcoins que posee: "))

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()  # Verificar si hubo algún error en la solicitud

    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]

    cost = n * price

    print(f"El costo actual de {n:,} Bitcoins es ${cost:,.4f}")
except requests.RequestException:
    print("Error al conectar con la API de CoinDesk")
"""2- FIGlet, llamado así por las cartas de Frank, Ian y Glen, es un programa de principios de la
década de 1990 para hacer letras grandes a partir de texto ordinario, una forma de arte ASCII:
- En la siguiente web puede ver una lista de fuentes admitidas por FIGlet
figlet.org/examples.html
- Desde entonces, FIGlet ha sido portado a Python como un módulo llamado pyfiglet.
Cree un programa el cual cumpla con las siguientes especificaciones:
- Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
- Solicite al usuario un texto.
- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.
Notas:
- Instalar la librería usando: pip install pyfiglet
- Para usar la librería, debe hacer:
from pyfiglet import Figlet
figlet = Figlet()
- Puede obtener la lista de fuentes disponibles usando: figlet.getFonts()
- Para seleccionar el fondo a utilizar emplee: figlet.setFont(font=fuente_seleccionada)
- Finalmente podrá imprimir el texto usando : print(figlet.renderText(texto_imprimir))
- Recuerde que random tiene un método random choice"""

from pyfiglet import Figlet
import random

figlet = Figlet()
available_fonts = figlet.getFonts()

font_name = input("Ingrese el nombre de la fuente (deje en blanco para seleccionar aleatoriamente): ")

if not font_name:
    font_name = random.choice(available_fonts)

if font_name not in available_fonts:
    print(f"La fuente '{font_name}' no está disponible.")
    print("Fuentes disponibles:")
    print(", ".join(available_fonts))
else:
    figlet.setFont(font=font_name)

    text_to_print = input("Ingrese el texto a imprimir: ")

    print(figlet.renderText(text_to_print))

"""3. Del siguiente URL https://unsplash.com/es/s/fotos/perrito
Descargue la imagen que más le agrade, según lo revisado en la clase.
"""
import requests

url = "https://unsplash.com/es/fotos/wFlrIeyBDBk"

response = requests.get(url)

if response.status_code == 200:
    filename = url.split("/")[-1]

    with open(filename, "wb") as file:
        file.write(response.content)
    
    print(f"La imagen se ha descargado correctamente como '{filename}'")
else:
    print("No se pudo descargar la imagen")

"""4. Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones,
también puede usar un menú para organizar su programa):
- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, donde “n” es el número introducido, y la muestre por
pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de
ello.
- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero
no existe debe mostrar un mensaje por pantalla informando de ello.
Notas:
- Note que dentro del manejo de errores existe una excepción de tipo
FileNotFoundError la cual le será de mucha utilidad.
- Revise los métodos de cadena
- Dentro del open() el método “readlines” le podría ser de utilidad"""

def guardar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "w") as file:
            for i in range(1, 11):
                linea = f"{numero} x {i} = {numero * i}\n"
                file.write(linea)
        
        print(f"Se ha guardado la tabla de multiplicar del número {numero} en el archivo 'tabla-{numero}.txt'")
    except IOError:
        print("No se pudo guardar la tabla de multiplicar.")

def mostrar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            tabla = file.read()
        
        if tabla:
            print(tabla)
        else:
            print(f"No se encontró la tabla de multiplicar del número {numero}.")
    except FileNotFoundError:
        print(f"No se encontró la tabla de multiplicar del número {numero}.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as file:
            lineas = file.readlines()

        if lineas:
            if linea <= len(lineas):
                print(lineas[linea - 1])
            else:
                print(f"No se encontró la línea {linea} en la tabla de multiplicar del número {numero}.")
        else:
            print(f"No se encontró la tabla de multiplicar del número {numero}.")
    except FileNotFoundError:
        print(f"No se encontró la tabla de multiplicar del número {numero}.")


def mostrar_menu():
    while True:
        print("-------- Menú --------")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar completa")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_linea_tabla_multiplicar(numero, linea)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


mostrar_menu()

"""5. Almacene los datos de precio de Bitcoin en un archivo txt y csv según crea conveniente.
"""
import csv
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/historical/close.json?start=2023-01-01&end=2023-12-31")
data = response.json()

dates = data["bpi"].keys()
prices = data["bpi"].values()

with open("bitcoin_prices.txt", "w") as txt_file:
    for date, price in zip(dates, prices):
        txt_file.write(f"{date}: {price}\n")

print("Datos de precio de Bitcoin almacenados en bitcoin_prices.txt")

with open("bitcoin_prices.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Fecha", "Precio"])

    for date, price in zip(dates, prices):
        writer.writerow([date, price])

print("Datos de precio de Bitcoin almacenados en bitcoin_prices.csv")


"""6. Para este problema deberá generar una base de datos llamada “cryptos” donde generará una tabla
llamada bitcoin en el cual deberá colocar el precio del bitcoin según la moneda USD, GBP, EUR. Deberá
tomar como base lo realizado en el problema 1.
Asegúrese de crear las columnas necesarias para este ejercicio, además de añadir una columna de fecha
que almacenerá los datos en que se tomaron los datos."""

import sqlite3
import requests
from datetime import datetime

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()

usd_price = data["bpi"]["USD"]["rate"]
gbp_price = data["bpi"]["GBP"]["rate"]
eur_price = data["bpi"]["EUR"]["rate"]

date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("cryptos.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date_time TEXT,
                   usd_price REAL,
                   gbp_price REAL,
                   eur_price REAL)''')

cursor.execute("INSERT INTO bitcoin (date_time, usd_price, gbp_price, eur_price) VALUES (?, ?, ?, ?)",
               (date_time, usd_price, gbp_price, eur_price))

conn.commit()

conn.close()

print("Datos de precio de Bitcoin almacenados en la tabla 'bitcoin' de la base de datos 'cryptos'")

