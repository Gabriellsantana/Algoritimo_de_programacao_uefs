#Para .. faça ou Para .. .ir 

# for in range()
#  |   |    |
# para em  sequencia()
#FOR TEM QUE TER UM VARIAVEL DE CONTROLE  for i ... , for a ... , for b .. ,

#for = para /  é o laço
#in = em / é um conexão do laço com algo que tem que acontecer
#range() = sequência / é função que determina oque deve aconte ou como aconter

#não é obrigatori ter funçã range() para alguns cas lógico

#usamos a funça pré-defenida "range()"

#Mostrando dez número na tela
print()

for i in range(10):
  print(i)
print()

#mostrando valor de uma lista ou percorrendo valores de uma lista
lista = [40,70,34,45,23,12,3,3,2]

for i in lista:
    print(i)

#contando de forma decressente
for i in range (10,1,-1):
   print(i)

#percorrendo um lista de nomes
nomes = ["Gabriel","Júlia","Vitoria","Andreza","Luis"]

for i in nomes:
   print(i)

#somando numeros naturais 
print("Digite um número natural (positivo):")
n = int(input())
soma = 0

for i in range(1,n+1):
  print(i)
  soma += i
print(f"A soma dos naturais até {n} é {soma}." )














#porque range(lista) não funciona
# for i in range(lista):
#Pq passa um parametro ao range ele assume que é stop , pq star é defenido 1 ,e step 0
print()
for b in enumerate(lista):
    print(b)
