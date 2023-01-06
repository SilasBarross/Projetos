import PySimpleGUI as sg

def calculator(num1, operator, num2):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2
  else:
    return "Operação invalida"

layout = [
  [sg.Text("primeiro numero:")],
  [sg.InputText()],
  [sg.Text("qual operador:")],
  [sg.InputText()],
  [sg.Text("segundo numero:")],
  [sg.InputText()],
  [sg.Button("Calcular"), sg.Exit()]
]

window = sg.Window("Calculadora", layout)

while True:
  event, values = window.read()
  if event in (None, "Sair"):
    break
  elif event == "Calcular":
    try:
      num1 = float(values[0])
      operator = values[1]
      num2 = float(values[2])
      result = calculator(num1, operator, num2)
      sg.popup(result)
    except ValueError:
      sg.popup("Entrada invalida, digite novamente.")

window.close()