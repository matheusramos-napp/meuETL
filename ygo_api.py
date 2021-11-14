import requests
import json
import sys

from requests.sessions import dispatch_hook

class MeuETL:

    def __init__(self, card_name=None, *args, **kwargs):
        self.card_name = card_name
        self.url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'

        session = requests.Session()
        session.get(self.url)

        def search_name():
            dic_card = {}       
            req_nome = session.get(f'{self.url}?name={self.card_name}')
            if req_nome.status_code == 200:
                req_nome = req_nome.json()
                for card in req_nome['data']:
                    name = str(card['name'])
                    type = str(card['type'])
                    attribute = str(card['attribute'])
                    raca = card['race']
                    for image in card['card_images']:
                        picture = str(image['image_url'])
                dic_card = {"Nome":name,"Tipo":type,"Atributo":attribute,"Raca":raca,"Imagem":picture}

                nome_arquivo = str(self.card_name).replace(' ','').lower()
                arquivo = open(f"{nome_arquivo}.txt", "a")
                arquivo.write(f"Nome: {dic_card['Nome']}\nTipo: {dic_card['Tipo']}\nAtributo: {dic_card['Atributo']}\nRaça: {dic_card['Raca']}\nLink Imagem: {dic_card['Imagem']}")  
            else:
                print("NOME INCORRETO!")
            
        if self.card_name != None:
            search_name()

        else:
            req_api = requests.get(f"{self.url}")
            if req_api.status_code == 200:
                print("TUDO CERTO!")
            else:
                print("HOUVE ALGUM ERRO :/")

if __name__ == "__main__":
    etl = MeuETL(card_name='Dark Magician')


    