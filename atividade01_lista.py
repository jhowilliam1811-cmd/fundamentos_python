# Autor : Jhonatan 
# Projeto : Listas

# lista de frutas com 5 unidades
#            0         1         3         4        5
frutas = ['banana', 'maçã', 'abacaxi', 'goiaba', 'kiwi']

print(frutas)

# adicionar um item na lista
frutas.append('laranja')
print(frutas)

# alterar o contúdo de uma posição
# mudar a fruta kiwi para morango
frutas[4]='morango'
print(frutas)

# deletar um item por posição
# excluir a maçã
del frutas[1]
print(frutas) 

# inserir uma nova fruta na posição 1
frutas.insert(1,'mamão')
print(frutas)


# ordena a lista
frutas.sort()
print(frutas)