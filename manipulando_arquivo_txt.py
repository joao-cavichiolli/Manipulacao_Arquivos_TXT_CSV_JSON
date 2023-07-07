## Vamos abrir um arquivo para Leitura ##

arq1 = open('arquivos/arquivo.txt','r')


print(arq1.read())


# Retorna ao inicio do arquivo com a função seek

arq1.seek(0)

print(arq1.read())

# Fechar o arquivo

arq1.close()


# Abrir o arquivo para opção de gravação e leitura

arq2 = open('arquivos/arquivo.txt','w+')

arq2.write('Tem novo conteudo\n')
arq2.write('Tem novo Conteudo Escrito de novo\n')

# Voltar o curso para cima 

arq2.seek(0)

# Ler o arquivo
print(arq2.read())

# Fechar o arquivo
arq2.close()


## Inserir dados sem sobrescrever. a função append a+

arq3 = open('arquivos/arquivo.txt','a+')

arq3.write("Nova escrita sem Excluir")

# Trazer o cursor para linha 0

arq3.seek(0)

print(arq3.readable())

arq3.seek(1)
arq3.write("Nova escrita sem Excluir")

arq3.close()

## Utilizando contexto de manipulacao de Arquivos. Pode ser qualquer 
# tipo. E uma boa pratica e mantem o codigo organizado e performado.

# With open vai gerar um nome de contexto para o arquivo

with open('arquivos/arquivo.txt','w+') as f:
    f.write('Nova Linhas\n')
    f.write("De novo linha\n")
    f.write("De novo linha\n")
    f.seek(0)
    print(f.read())
    f.close()


# Criando um novo Arquivo

with open('arquivos/arquivo1.txt','a+') as f:
    f.write('Teste linhas\n')
    f.write('Teste linhas\n')
    f.seek(0)
    print(f.read())
    f.close()








