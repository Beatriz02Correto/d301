# # EXERCICIO 1
# nome = input("Seja bem vindo ao sistema de aprovação de credito, Qual seu nome?")
# salario = input("Qual seu salario hoje?")
# emprestimo = input("Qual seu emprestimo?")
# media = salario*5
# if float(emprestimo>= media): 
#     print (f"{nome}, você foi aprovado!")
# else:
#     print ("você foi reprovado....")


# EXERCICIO 2

# lances = int(input("Quantos Lances?"))
# material = input("Material?")
# desenho = ''
# i = 0

# while not int (lances):
#     input(f"você digitou {lances} Por favor só Numeros")

# while i < lances:
#     desenho = desenho + material
#     print(desenho)    
#     i+=1

# #EXERCICIO 3
# import random

# def embaralhar(lista):
#   for i in range(len(lista) - 1,0,-1) :
#     indice_aleatorio = random.randint(0, i)
#     valor_temporario = lista[i]
#     lista[i] = lista[indice_aleatorio]
#     lista[indice_aleatorio] = valor_temporario
#   return lista

# valores = [1, 2, 3, 4, 5,]

# embaralhado = embaralhar(valores)
# print(embaralhado)

# EXERCICIO 4

# meninos = ["luiz", 'joão', 'fernando', 'bruno']
# meninas = ['lais','lolo', 'ana']
# i = 1
# for meninos in meninas:
#   for meninas in meninos:
#     print (f"casalsinho {i}: {meninos} e {meninas}")
#     i += 1

# # EXERCICIO 5
# meninos = ["luiz", 'joão', 'fernando', 'bruno']
# meninas = ['lais','lolo', 'ana']
# todos = meninas + meninas
# i = 1
# j = 0
# for pessoa1 in meninas:
#   for k in range(j, len(todos)):
#     if pessoa1 != todos[k]:
#       print (f"casalsinho {i}: {pessoa1} e {todos[k]}")
#       i += 1
#   j += 1

# EXERCICIO 6

# iguais = [a, a, a, a, a,]
# diferente = [a, a, a, b, a,]

# def todos-iguais(lista):
#     for i in range(1, len(lista)):
#         if lista[i]!= lista[i-1]:
#             return False
#     return True



