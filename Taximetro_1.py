#import time
import locale

locale.setlocale(locale.LC_ALL, '')

class Taximetro:
    def __init__(self):
        self.tarifa_parado = 0.02  # 2 céntimos por segundo
        self.tarifa_movimiento = 0.05  # 5 céntimos por segundo
        self.total = 0
        self.en_trayecto = False
        

    def iniciar_trayecto(self):
        print("\nTrayecto iniciado.\n")
        self.total = 0
        self.suma_final = 0
        self.en_trayecto = True
        self.calcular_tarifa()

    def calcular_tarifa(self):
        while self.en_trayecto:
            estado = input("¿El taxi está en movimiento (m) o parado (p)? (f para finalizar): ").lower()

            if estado == 'f':
                self.finalizar_trayecto()
                break
            elif estado in ['m', 'p']:
                try:
                    duracion = int(input("Ingrese la duración en segundos: "))
                    if duracion < 0:
                        print("La duración no puede ser negativa.")
                        continue
                except ValueError:
                    print("Por favor, ingrese un número válido de segundos.")
                    continue

                if estado == 'm':
                    self.total += self.tarifa_movimiento * duracion
                else:
                    self.total += self.tarifa_parado * duracion
                self.suma_final = (self.suma_final + self.total)
                print(f"Total actual: {self.total:.2f} euros\n")
            else:
                print("Opción no válida. Intente de nuevo.")

    def finalizar_trayecto(self):
        print(f"\nTrayecto finalizado. Total a cobrar: {locale.currency(self.suma_final, grouping=True)} euros\n")
        self.en_trayecto = False


def main():
    print("Bienvenido al prototipo de taxímetro digital.")
    print("Este programa calcula la tarifa de un trayecto según el tiempo de parada y movimiento.\n")

    taximetro = Taximetro()

    while True:
        opcion = input("¿Desea iniciar un nuevo trayecto? (s/n): ").lower()
        if opcion == 's':
            taximetro.iniciar_trayecto()
        elif opcion == 'n':
            print("Gracias por usar el taxímetro digital. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()