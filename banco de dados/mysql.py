import requests
from bs4 import BeautifulSoup

busca = input('Digita o nome da cidade: ')

url = f"https://www.google.com/search?&q={busca}"

r = requests.get(url)

s = BeautifulSoup(r.text,"html.parser")

update = s.find("div",class_="BNeawe").text

print(f'Previsão de {update} em {busca}')