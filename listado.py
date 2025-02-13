import locale
from time import sleep
from datetime import date
import keyboard as kb
from colorama import Cursor, init, Fore, Back, Style
import conectar_postgreSQL as con
import pandas as pd

def iniciar_lista():
    con.cursor.execute("SELECT * FROM trayecto")
    print(f"{'ID':<5} {'FECHA':<20} {'PRECIO':<10}")
    print(Fore.LIGHTGREEN_EX + "=" * 40 + Fore.WHITE)
    total = 0
    for id, fecha, precio in con.cursor:
        fecha_formateada = fecha.strftime("%Y-%m-%d %H:%M") 
        total += precio
        print(f"{id:<5} {fecha_formateada:<20} {Fore.LIGHTWHITE_EX + locale.currency(precio, grouping=True)+ Fore.WHITE}")
    #con.cursor.close()
    print(Fore.LIGHTGREEN_EX + "=" * 40 + Fore.WHITE)
    print(f"{'TOTAL:':<25} {Fore.LIGHTWHITE_EX + locale.currency(total, grouping=True)+ Fore.WHITE}")

def exportar_csv():
    hoy = date.today()
    print("Exportando datos a trayecto.csv")
    df = pd.read_sql("SELECT * FROM trayecto", con.connection)
    archivo = format(hoy.day) + "-" + format(hoy.month) + "-" + format(hoy.year) + "_trayectos.csv"
    df.to_csv(archivo, index=False)
    print("\033[2J\033[1;1f")
    print(f"Datos exportados a {archivo}") 
    sleep(2) 