# crear dependencias con el comando: pip freeze > requirements.txt
# instalar dependencias con el comando: pip install -r requirements.txt
# ejecutar con el comando: python main.py
# ejecutar con el comando: python -m main

import time
import locale
import sys
import hashlib
import getpass

from time import sleep
from datetime import datetime
import keyboard as kb
import msvcrt

from colorama import Cursor, init, Fore, Back, Style

import conectar_postgreSQL as con
import listado as Listado
import voz_texto as vt
import texto_voz as tv

init(autoreset=True)
locale.setlocale(locale.LC_ALL, '')

# Clase Taximetro
class Taximetro:
    # Constructor
    def __init__(self):
        self.tarifa_parado = con.sql_select('precios', 'parado')
        self.tarifa_movimiento = con.sql_select('precios', 'marcha')
        self.total = 0
        self.en_trayecto = False
    # uncion para iniciar trayecto, definir variables y calcular tarifa nuevos
    def iniciar_trayecto(self):
        print(Fore.BLUE + "\nTrayecto iniciado.\n" + Fore.WHITE)
        self.en_marcha = 0
        self.parado = 0
        self.total = 0
        self.suma_final = 0
        self.en_trayecto = True
        self.calcular_tarifa()
    # Funcion para calcular la tarifa del trayecto, con la posibilidad de moverse o pararse
    def calcular_tarifa(self):
        print( Fore.BLACK + Back.LIGHTWHITE_EX + "Manten pulado 'm' para mover y 's' para acabar viaje, mientras está parado.\n" + Back.RESET + Fore.WHITE)
        print("")
        # Bucle para saber si el taxi está en marcha, parado o finalizar trayecto
        while self.en_trayecto:
            start_time = time.time()
            elapsed_time = 0
            print("En marcha:", 
                  locale.currency(self.en_marcha, grouping=True), 
                  "Parado:", locale.currency(self.parado, grouping=True), 
                  "Total:", locale.currency(self.total, grouping=True), 
                  end="\r")
            en_marcha = 0
            parado = 0
            if kb.is_pressed("m"):
                elapsed_time = time.time() - start_time
                en_marcha += self.tarifa_movimiento * elapsed_time
                self.total += en_marcha
                print(Cursor.UP(1) + Fore.YELLOW + "En marcha " + Fore.WHITE)
            elif kb.is_pressed("s"):
                self.finalizar_trayecto()
                break
            else:
                elapsed_time = time.time() - start_time
                parado += self.tarifa_parado * elapsed_time
                self.total += parado
                print(Cursor.UP(1) + Fore.RED + "Parado      " + Fore.WHITE)
            self.en_marcha += en_marcha
            self.parado += parado

    def finalizar_trayecto(self):
        # para limpiar el buffer de entrada mientras hacemos el trayecto
        while msvcrt.kbhit():
            msvcrt.getch()
            
        print("\033[2J\033[1;1f")
        sys.stdin.flush()
        print(f"Trayecto finalizado. Total a cobrar: {Fore.LIGHTWHITE_EX + locale.currency(self.total, grouping=True)+ Fore.WHITE} euros\n", end="\r")
        con.insertar_sql(f"INSERT INTO trayecto(precio) VALUES({self.total})")
        input("Pulsa una tecla para continuar...")
        print("\033[2J\033[1;1f")
        self.en_trayecto = False

class Precios:
    def __init__(self):
        self.nombre = ""
        self.menu_seleccion = True
        self.seleccionar = True

    def logeado(self):
        self.menu_seleccion = True
        print("\033[2J\033[1;1f")
        print(Fore.LIGHTGREEN_EX + "Bienvenido", self.nombre + Fore.WHITE)
        con.cursor.execute(f"SELECT * FROM precios ORDER BY id DESC")
        print(f"{'Tipo':<5} {'PRECIO':<10}")
        print(Fore.LIGHTGREEN_EX + "=" * 20 + Fore.WHITE)

        for id, estado, precio in con.cursor:
            print(f"{estado:<5} {Fore.LIGHTWHITE_EX + locale.currency(precio, grouping=True)+ Fore.WHITE:<10}")
    
        print("¿Qué quieres hacer?")
        print(Fore.LIGHTWHITE_EX +"1" +Fore.WHITE, "Editar precio de marcha")
        print(Fore.LIGHTWHITE_EX +"2" +Fore.WHITE, "Editar precio de parado")
        print(Fore.LIGHTWHITE_EX +"3" +Fore.WHITE, "Cerrar sesión")

        while self.menu_seleccion:
            opcion = int( input("Selecciona una opción :"))
            if opcion == 1:
                precio = float(input("Introduce el nuevo precio para 'marcha': "))
                self.modificar_precios(precio, 'marcha')
            elif opcion == 2:
                precio = float(input("Introduce el nuevo precio para 'parado': "))
                self.modificar_precios(precio, 'parado')
            elif opcion == 3:
                self.finalirzar_sesion()

            else:
                print("Opción no válida. Intente de nuevo.")

    def modificar_precios(self, precio, estado):
        con.insertar_sql(f"UPDATE precios SET precio = {precio} WHERE estado = '{estado}'") 
        print(f"Precio de {estado} actualizado a {precio}.")
        
        sleep(2)
        print("\033[2J\033[1;1f")
        self.logeado()

    def finalirzar_sesion(self):
        input("Pulsa una tecla para continuar...")
        print("\033[2J\033[1;1f")
        self.menu_seleccion = False  

    def iniciar_precios(self):
        self.seleccionar = True
        print(Fore.RED + "Estas entrando en un lugar reservado para los taxistas." + Fore.WHITE)
        print("Por favor, introduce usuario.")
        intentos = 0

        while self.seleccionar:
            usuario = getpass.getpass("").lower()
            #usuario = input().lower()
            usuario_hash = hashlib.md5(usuario.encode()).hexdigest()
            #print(usuario_hash)
            con.cursor.execute("SELECT nombre FROM usuarios WHERE usuario = %s", (usuario_hash,))
            self.nombre = con.cursor.fetchone()[0]
            if self.nombre:
                self.logeado()
                self.seleccionar = False
            else:
                intentos += 1
                if intentos == 3:
                    print("Demasiados intentos.")
                    sleep(2)
                    print("\033[2J\033[1;1f")
                    break

precios = Precios()
taximetro = Taximetro()
def Main():
    print("\033[2J\033[1;1f")
    print("Bienvenido al prototipo de taxímetro digital.")
    print("Este programa calcula la tarifa de un trayecto según el tiempo de parada y movimiento.\n")
    while True:
        print("  Listado de precios,", "taxi parado:", Fore.RED + locale.currency(taximetro.tarifa_parado, grouping=True) + Fore.WHITE, ", taxi en movimiento:", Fore.RED + locale.currency(taximetro.tarifa_movimiento, grouping=True) + Fore.WHITE,".")
        print(Fore.LIGHTWHITE_EX + "t" + Fore.WHITE," - Hacer un trayecto")
        print(Fore.LIGHTWHITE_EX + "a" + Fore.WHITE," - listar trayectos")
        print(Fore.LIGHTWHITE_EX + "x" + Fore.WHITE," - Exportar trayectos a un archivo CSV")
        print(Fore.LIGHTWHITE_EX + "i" + Fore.WHITE," - Información precios")
        print(Fore.LIGHTWHITE_EX + "s" + Fore.WHITE," - Salir de la aplicación")
        print("Puedes usar el", Fore.LIGHTWHITE_EX + " asistente de voz"+ Fore.WHITE," (limitado a este menú), si lo deseas escribe asistente.")
        opcion = input("  Selecciona una opción:").lower()
        print("\033[2J\033[1;1f")
        if opcion == 'asistente':
            asistente_voz()
        elif opcion == 't':
            taximetro.iniciar_trayecto()
        elif opcion == 'a':
            Listado.iniciar_lista()
        elif opcion == 'x':
            Listado.exportar_csv()
        elif opcion == 'i':
            precios.iniciar_precios()
        elif opcion == 's':
            print("\033[2J\033[1;1f")
            print("Gracias por usar el taxímetro digital. ¡Hasta luego!")
            con.cursor.close()
            sleep(2)
            print("\033[2J\033[1;1f")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def asistente_voz():
    tv.texto_voz("Asistente de voz activado.\n Recuerda que solo puedes usar el asistente en este menú.")
    tv.texto_voz("Di 'trayecto' para iniciar un trayecto.")
    tv.texto_voz("Di 'listar' para ver los trayectos.")
    tv.texto_voz("Di 'exportar' para exportar los trayectos a un archivo CSV.")
    tv.texto_voz("Di 'información' para ver los precios.")
    tv.texto_voz("Di 'salir' para salir del asistente de vo.")
    seleccion = vt.escuchar()
    if seleccion == "trayecto":
        taximetro.iniciar_trayecto()
    elif seleccion == "listar":
        Listado.iniciar_lista()
    elif seleccion == "exportar":
        Listado.exportar_csv()
    elif seleccion == "información":
        precios.iniciar_precios()
    elif seleccion == "salir":
        tv.texto_voz("Gracias por utilizar el asistente para taxis.\n En futuras actuliaciones se podrán realizar más cosas.")
        tv.texto_voz("Hasta luego, que tengas un buen día.")
        Main()
    else:
        print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    Main()
