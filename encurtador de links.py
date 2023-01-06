import requests

def shorten_url(long_url, name):
  # Faz a requisição para o serviço Silas
  response = requests.get(f"https://silas.link/api?url={long_url}&name={name}")

  # Verifica se a requisição foi bem-sucedida
  if response.status_code == 200:
    # Retorna o URL encurtado
    return response.text
  else:
    # Retorna o URL original em caso de falha
    return long_url

# Testa o encurtador de links
print(shorten_url("https://www.google.com/", "Silas"))

