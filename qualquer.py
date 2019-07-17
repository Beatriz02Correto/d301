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

#EXERCICIO 3

def embaralhar(lista):
valor_temporario = none
indice_aleatorio = none

  for  i = len(lista) - 1 i != 0 i-=1 {
    indice_aleatorio = Math.floor(Math.random() * i)
    valor_temporario = lista[i]
    lista[i] = lista[indice_aleatorio]
    lista[indice_aleatorio] = valor_temporario
  
  return lista

