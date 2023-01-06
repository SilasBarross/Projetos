import PySimpleGUI as sg

questions = [  ["Qual a cor do céu?", "azul"],
  ["Qual a cor da nuvem?", "branco"],
  ["Qual a cor do sol?", "amarelo"]
]

score = 0

for question, answer in questions:
  layout = [
    [sg.Text(question)],
    [sg.InputText()],
    [sg.Button("Submit"), sg.Exit()]
  ]
  window = sg.Window("Quiz", layout)
  event, values = window.read()
  if event in (None, "Exit"):
    break
  elif values[0] == answer:
    score += 1
  window.close()

sg.popup(f"Your score is {score}/{len(questions)}")