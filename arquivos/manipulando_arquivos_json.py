# Para manipular baixar e gerenciar formato Json
# utilizamos a biblioteca JSON

import json
import urllib.request


cadastro_pessoas = {
    "1": {
        "Nome": "Joao",
        "Idade": 35,
        "Sexo": "Masculino",
        "Data Nascimento": "29/12/1985"
    },
    "2": {
        "Nome": "Juca",
        "Idade": 34,
        "Sexo": "Masculino",
        "Data Nascimento": "12/12/1985"
    },
    "3": {
        "Nome": "Leandro",
        "Idade": 50,
        "Sexo": "Masculino",
        "Data Nascimento": "01/01/1970"
    },
    "4": {
        "Nome": "Rita",
        "Idade": 23,
        "Sexo": "Feminino",
        "Data Nascimento": "12/09/1997"
    }
}


# Iterar o objeto

for c,v in cadastro_pessoas.items():
    print(c,v)

# Converter esse dicionario em um arquivo e vamos manipular 
# utilizando a funcao json.dump

dados = json.dumps(cadastro_pessoas,indent=4)

with open('arquivos/pessoas.json','w+') as j:
    json.dump(cadastro_pessoas,j,indent=4)

## Abrir o arquivo com o json loads para um dicionario

with open('arquivos/pessoas.json','r') as f:
    le_json = json.load(f)

    print(le_json)

    for v in le_json.values():
        print(v)

# Vamos capturar uma informação da internet e armazenar utilizando Python

url = 'http://api.open-notify.org/astros.json'

## Capturar os dados e armazenar em uma variavel

pega_json = urllib.request.urlopen(url).read().decode()


# Converter esse dado em dicionario

dic_json = json.loads(pega_json)

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name'])

## Criar um arquivo com dados capturados

with open('arquivos/astros.json','w+') as f:
    json.dump(dic_json,f,indent=4)