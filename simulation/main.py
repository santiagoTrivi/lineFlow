import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import numpy as np
from queue import Queue
from validation import (is_float, is_int, servers_validation)
from customer import Customer

class BankSimulation:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulación de Cola en el Banco")
        self.master.geometry("480x380")  # Ajustar tamaño de la ventana para el nuevo espaciado
        self.master.resizable(False, False)

        # Fondo blanco de la ventana principal
        self.master.configure(bg="#FFFFFF")

        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Verdana", 12), background="#FFFFFF")  # Fuente Verdana para etiquetas
        self.style.configure("TFrame", background="#FFFFFF")

        self.create_widgets()

        self.cashiers = [None] * 6
        self.customer_queue = Queue()
        self.running = False

    def create_widgets(self):
        frame = ttk.Frame(self.master, padding=15, style="TFrame")  # Espaciado general más ajustado
        frame.pack(fill=tk.BOTH, expand=True)

        # Etiquetas y entradas con espaciado reducido
        ttk.Label(frame, text="Lambda (Llegadas por minuto):", style="TLabel").pack(pady=7)  # Menos separación
        self.lambda_input = tk.Entry(frame, width=30, font=("Verdana", 12), highlightbackground="#007BFF", highlightthickness=1)
        self.lambda_input.pack(pady=7)

        ttk.Label(frame, text="Mu (Tiempo medio de servicio):", style="TLabel").pack(pady=7)
        self.mu_input = tk.Entry(frame, width=30, font=("Verdana", 12), highlightbackground="#007BFF", highlightthickness=1)
        self.mu_input.pack(pady=7)

        ttk.Label(frame, text="Número de cajeros:", style="TLabel").pack(pady=7)
        self.servers_input = tk.Entry(frame, width=30, font=("Verdana", 12), highlightbackground="#007BFF", highlightthickness=1)
        self.servers_input.pack(pady=7)

        # Botones con espaciado reducido
        button_frame = ttk.Frame(frame, style="TFrame")
        button_frame.pack(pady=15)  # Menos separación entre las entradas y los botones

        self.submit_button = tk.Button(button_frame,
                                        text="Iniciar Simulación",
                                        command=self.start_simulation,
                                        font=("Verdana", 12),
                                        bg="#007BFF",  # Fondo azul original
                                        fg="white",  # Texto blanco
                                        activebackground="#0056b3",  # Azul más oscuro al hacer clic
                                        activeforeground="white",  # Texto blanco al hacer clic
                                        borderwidth=0,  # Eliminar borde negro
                                        highlightthickness=0)  # Eliminar borde de enfoque
        self.submit_button.pack(side=tk.LEFT, padx=7)  # Espaciado horizontal más ajustado
        self.submit_button.bind("<Enter>", lambda e: self.on_hover(self.submit_button))
        self.submit_button.bind("<Leave>", lambda e: self.on_leave(self.submit_button))

        self.stop_button = tk.Button(button_frame,
                                      text="Detener",
                                      command=self.stop_simulation,
                                      font=("Verdana", 12),
                                      bg="#007BFF",  # Fondo azul original
                                      fg="white",  # Texto blanco
                                      activebackground="#0056b3",  # Azul más oscuro al hacer clic
                                      activeforeground="white",  # Texto blanco al hacer clic
                                      borderwidth=0,  # Eliminar borde negro
                                      highlightthickness=0)  # Eliminar borde de enfoque
        self.stop_button.pack(side=tk.LEFT, padx=7)  # Espaciado horizontal más ajustado
        self.stop_button.bind("<Enter>", lambda e: self.on_hover(self.stop_button))
        self.stop_button.bind("<Leave>", lambda e: self.on_leave(self.stop_button))

        # Etiqueta de estado con espaciado reducido
        self.status_label = ttk.Label(frame, text="Estado: Detenido", style="TLabel")
        self.status_label.pack(pady=15)

    def on_hover(self, button):
        """Estilo al pasar el mouse por encima."""
        button.config(bg="#0056b3", fg="white")  # Fondo azul oscuro, texto blanco

    def on_leave(self, button):
        """Revertir el estilo al sacar el mouse."""
        button.config(bg="#007BFF", fg="white")  # Fondo azul original, texto blanco

    def start_simulation(self):
        lambda_value = self.lambda_input.get()
        mu_value = self.mu_input.get()
        servers_value = self.servers_input.get()

        if not is_float(lambda_value):
            messagebox.showerror("Error de entrada", "Lambda debe ser un número flotante válido.")
            return
        if not is_float(mu_value):
            messagebox.showerror("Error de entrada", "Mu debe ser un número flotante válido.")
            return
        if not is_int(servers_value):
            messagebox.showerror("Error de entrada", "El número de cajeros debe ser un entero válido.")
            return
        if not servers_validation(int(servers_value)):
            messagebox.showerror("Error de entrada", "El número de cajeros debe ser menor o igual a 6.")
            return

        self.running = True
        self.status_label.config(text="Estado: En ejecución")
        self.simulate_customers()
        self.process_customers()

    def stop_simulation(self):
        self.running = False
        self.status_label.config(text="Estado: Detenido")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankSimulation(root)
    root.mainloop()
