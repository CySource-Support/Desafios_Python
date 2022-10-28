nomes = [] # cria uma lista para o usuário inserir os nomes

for i in range(2):
    nome = input('Digite o nome aqui: ')
    nomes.append(nome) # Adiciona os nomes na lista (comando app)
print(nomes[::-1]) # inverte a ordem  dentro da lista