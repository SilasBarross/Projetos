# Lê o valor em reais e a taxa de câmbio
value_in_reais = float(input("Informe o valor em reais: "))
exchange_rate = float(input("Informe a taxa de câmbio atual: "))

# Verifica se a taxa de câmbio é válida
if exchange_rate > 0:
  # Converte o valor em reais para dólar
  value_in_dollar = value_in_reais / exchange_rate

  # Exibe o resultado da conversão
  print(f"{value_in_reais} reais = {value_in_dollar:.2f} dólares")
else:
  # Exibe uma mensagem de erro
  print("Por favor, informe uma taxa de câmbio válida!")
