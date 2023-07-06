# Manipulação de arquivos CSV
# PAra manipular ler criar arquivos CSV utilizamos a biblioteca CSV

import csv

## Usando gerenciador de contexto de arquivos para criar um csv

with open('arquivos/nomes.csv','w+',encoding='UTF8',newline="") as fcsv:
    escrever = csv.writer(fcsv,delimiter=',')
    escrever.writerow(("Nome","Sobrenome","Idade"))
    escrever.writerow(("João","Cavichiolli",38))
    escrever.writerow(("Juca","Souza",56))
    escrever.writerow(("Alberto","Cunha",54))


# Ler o arquivo criado com a funcao csv.reader

with open('arquivos/nomes.csv','r',encoding='UTF8') as fcsv:
    ler = csv.reader(fcsv)

    lista1 = list(ler)

    print(lista1)

    for i in lista1:
        print(i)

## Ler um arquivo CSV e transforma-lo em dicionario com a funcao dictreader


with open('arquivos/nomes.csv','r',encoding='UTF8') as fcsv:
    ler_dict = csv.DictReader(fcsv)



# Iterando diretamente o objeto convertido

    for i in ler_dict:
        print(i)
    
    for d in ler_dict:
        print(d["Nome"])


## Ler um arquivo csv e gravar numa lista

with open('arquivos/arquivo1.csv','r') as arq1:
    arq1 = csv.reader(arq1)

# iterar os valores do csv

    #for i in arq1:
     #   print(i)

# Transformar uma lista

    lista2 = list(arq1)

    print(lista2)
