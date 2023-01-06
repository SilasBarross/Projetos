
users = {}

def registerUser():
  # Ask for user's name
  name = input("Qual seu nome: ")
  
  # Check if the user already exists
  if name in users:
    print("Esse usuário ja existe! Tente novamente com um usuario diferente.")
    return
  
  # Ask for user's age
  age = input("Qual sua idade: ")
  
  # Add the user to the dictionary
  users[name] = age
  
  print("Registrado com sucesso!")

def viewUsers():
  # Print all the registered users
  for user in users:
    print("Name:", user, "Age:", users[user])

# Main program
while True:
  # Print the options
  print("O que deseja fazer?")
  print("1. Registrar um usuario novo")
  print("2. Ver todos usuarios")
  print("3. Sair")
  
  # Get the user's choice
  choice = input()
  
  # Execute the chosen option
  if choice == "1":
    registerUser()
  elif choice == "2":
    viewUsers()
  elif choice == "3":
    break
  else:
    print("Opção invalida, tente novamente.")
