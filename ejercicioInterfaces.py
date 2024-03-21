import tkinter as tk
def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  return a / b

def raiz_cuadrada(a):
  return a ** 0.5

def potencia(a, b):
  return a ** b

def calcular_resultado(operacion, cajaNumero1, cajaNumero2):
  try:
    if cajaNumero1.get().isdigit() and cajaNumero2.get().isdigit():
      numero1 = int(cajaNumero1.get())
      numero2 = int(cajaNumero2.get())

      if operacion == "Suma":
        resultado = sumar(numero1, numero2)
      elif operacion == "Resta":
        resultado = restar(numero1, numero2)
      elif operacion == "Multiplicación":
        resultado = multiplicar(numero1, numero2)
      elif operacion == "División":
        resultado = dividir(numero1, numero2)
      elif operacion == "Raíz cuadrada":
        resultado = raiz_cuadrada(numero1)
      elif operacion == "Potencia":
        resultado = potencia(numero1, numero2)
      else:
        raise ValueError("Operación no válida")

     
    else:
      raise ValueError("Los valores introducidos no son números")

  except ValueError as e:
    print(f"Error: {e}")

def main():
  # Crear la ventana principal
  ventana = tk.Tk()
  ventana.title("Calculadora")

  # Crear las etiquetas
  etiqueta_operacion = tk.Label(text="Operación:")
  etiqueta_numero1 = tk.Label(text="Primer número:")
  etiqueta_numero2 = tk.Label(text="Segundo número:")
  etiqueta_resultado = tk.Label(text="Resultado:")

  # Crear los cuadros de texto
  operacion_seleccionada = tk.StringVar()
  operacion_seleccionada.set("Suma")
  menu_operacion = tk.OptionMenu(ventana, operacion_seleccionada, "Suma", "Resta", "Multiplicación", "División", "Raíz cuadrada", "Potencia")
  cajaNumero1 = tk.Entry()
  cajaNumero2 = tk.Entry()
  resultado_entry = tk.StringVar()
  resultado_entry.set("") # Inicializar la variable con un valor vacío
  resultado_text = tk.Entry(textvariable=resultado_entry)

  # Crear el botón
  boton_calcular = tk.Button(text="Calcular", command=lambda: calcular_resultado(operacion_seleccionada.get(), cajaNumero1, cajaNumero2))

  # Organizar los elementos en la ventana
  etiqueta_operacion.pack()
  menu_operacion.pack()
  etiqueta_numero1.pack()
  cajaNumero1.pack()
  etiqueta_numero2.pack()
  cajaNumero2.pack()
  boton_calcular.pack()
  etiqueta_resultado.pack()
  resultado_text.pack()

  # Iniciar la ventana principal
  ventana.mainloop()

if __name__ == "__main__":
  main()
