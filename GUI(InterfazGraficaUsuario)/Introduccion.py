import tkinter as tk
from tkinter import ttk, messagebox
import os

ventana = tk.Tk()
ventana.title("Pantalla principal")
ventana.geometry("720x480")

caja = tk.Frame(ventana, padx = 10, pady = 10)
caja.pack(fill="both", expand=True)

ventana.mainloop()