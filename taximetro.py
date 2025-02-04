import tkinter as tk
import time
from pyvirtualdisplay import Display

# Create a virtual display
display = Display(visible=0, size=(800, 600))
display.start()

class TaxiApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Tarifas de Taxi")

        self.bienvenida = tk.Label(master, text="Bienvenido a la Calculadora de Tarifas de Taxi")
        self.bienvenida.pack(pady=10)

        self.boton_iniciar = tk.Button(master, text="Iniciar Trayecto", command=self.iniciar_trayecto)
        self.boton_iniciar.pack()

        self.label_tarifa = tk.Label(master, text="Tarifa actual: 0.00 €")
        self.label_tarifa.pack()

        self.boton_finalizar = tk.Button(master, text="Finalizar Trayecto", command=self.finalizar_trayecto, state=tk.DISABLED)
        self.boton_finalizar.pack()

        self.trayecto_en_curso = False
        self.tiempo_inicio = 0
        self.tarifa_total = 0.0

    def iniciar_trayecto(self):
        self.trayecto_en_curso = True
        self.tiempo_inicio = time.time()
        self.boton_iniciar.config(state=tk.DISABLED)
        self.boton_finalizar.config(state=tk.NORMAL)
        self.actualizar_tarifa()

    def finalizar_trayecto(self):
        self.trayecto_en_curso = False
        self.boton_iniciar.config(state=tk.NORMAL)
        self.boton_finalizar.config(state=tk.DISABLED)
        self.label_tarifa.config(text=f"Tarifa total: {self.tarifa_total:.2f} €")
        self.tarifa_total = 0.0  # Reiniciar para el próximo trayecto

    def actualizar_tarifa(self):
        if self.trayecto_en_curso:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            tarifa_parado = int(tiempo_transcurrido) * 0.02  # 2 céntimos por segundo
            tarifa_movimiento = int(tiempo_transcurrido) * 0.05  # 5 céntimos por segundo
            self.tarifa_total = tarifa_parado + tarifa_movimiento
            self.label_tarifa.config(text=f"Tarifa actual: {self.tarifa_total:.2f} €")
            self.master.after(1000, self.actualizar_tarifa)  # Actualizar cada segundo

root = tk.Tk()
app = TaxiApp(root)
root.mainloop()

display.stop() # Stop the virtual display when you are done