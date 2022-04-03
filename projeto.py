import os
import requests
import bs4
import webbrowser

def acha_proximo_nome(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return nome_arquivo
    base, extensao = os.path.splitext(nome_arquivo)
    numero = 1
    while True:
        nome_arquivo = '{}_{:03d}{}'.format(base, numero, extensao)
        if not os.path.exists(nome_arquivo): 
            return nome_arquivo
        numero += 1


teste = input("digite sua busca: ")
busca = "intext: " + teste

res= requests.get ("https://www.google.com/search?q=" + busca)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

teste = soup.find_all("a",limit= 25)

for link in teste:
    if "/url?q=" in link.get("href"):
        print(link.get("href")[7:])
        res1= requests.get(link.get("href")[7:])
        soup1 = bs4.BeautifulSoup(res1.text, features="html.parser")
        for cada in soup1:
            arquivo = open(acha_proximo_nome('raspagem.txt'), 'w+', newline='')
            arquivo.write(soup1.get_text())
        #webbrowser.open(link.get("href")[7:])
