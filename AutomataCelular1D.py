import numpy as np
import tkinter as tk
from tkinter import ttk

class AutomataCelular1D:
    def __init__(self, regla, estado_inicial):
        self.regla = [int(x) for x in np.binary_repr(regla, width=8)]
        self.estado_actual = estado_inicial.copy()
        self.historia = [self.estado_actual.copy()]

    def siguiente_generacion(self):
        nuevo_estado = np.zeros_like(self.estado_actual)
        for i in range(1, len(self.estado_actual) - 1):
            vecindad = self.estado_actual[i - 1: i + 2]
            indice_binario = 7 - int("".join(str(int(celda)) for celda in vecindad), 2)
            nuevo_estado[i] = self.regla[indice_binario]
        self.estado_actual = nuevo_estado
        self.historia.append(self.estado_actual.copy())

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Automata Celular 1D")
    
    self.create_widgets()
    self.automata = None
    
  def create_widgets(self):
    self.label = ttk.Label(self.root, text="Seleccione una Regla:")
    self.label.grid(row=0, column=0, padx=10, pady=10)

    self.reglas = [f"Regla {i}" for i in range(256)]
    self.combo = ttk.Combobox(self.root, values=self.reglas)
    self.combo.grid(row=0, column=1, padx=10, pady=10)
    self.combo.current(0)

    self.button = ttk.Button(self.root, text="Visualizar", command=self.visualizar)
    self.button.grid(row=0, column=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.root, width=610, height=800
    , bg="white")  # Aumentar la altura del lienzo
    self.canvas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    self.nombre = ttk.Label(self.root, text="Hernández Rodríguez Oscar David")  # Agregar tu nombre
    self.nombre.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

  def visualizar(self):
    regla_seleccionada = int(self.combo.get().split()[1])
    estado_inicial = np.zeros(61)
    estado_inicial[30] = 1
    
    self.automata = AutomataCelular1D(regla_seleccionada, estado_inicial)

    self.canvas.delete("all")
    self.dibujar_automata()

  def dibujar_automata(self):
    celda_size = 10
    for i in range(80):  # Aumentar el número de generaciones
      if i > 0:
        self.automata.siguiente_generacion()
      estado = self.automata.historia[-1]
      for j, celda in enumerate(estado):
        color = "black" if celda else "white"
        self.canvas.create_rectangle(
          j * celda_size, i * celda_size,
          (j + 1) * celda_size, (i + 1) * celda_size,
          fill=color, outline="gray"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
