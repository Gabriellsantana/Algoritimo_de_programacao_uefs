#OREDENAÇÃO MANUAL 
# Bubble Sort — método da bolha
#Compara dois elementos vizinhos. Se estiverem fora de ordem, troca suas posições.

#passos logicos 

#1- saber tamanho da lista 

#2- O i  até a penúltima posição da lista, pois comparamos os elementos em pares (um ao lado do outro). Quando chegamos à penúltima posição, já conseguimos comparar o penúltimo elemento com o último. Não precisamos chegar até a última posição, pois não existe outro elemento depois dela para fazer a comparação.

#3- fazer a troca com codiçoes 
# duas forma de fazer troca: 

      # Específica à linguagem Python:
      #Dadas duas variáveis existentes a e b, basta fazer: a, b = b, a

                #  aux = a
                #  a = b
                #  b = aux


def ordena_bubble_sort(lista):
    tamanho = len(lista)
    for j in range (tamanho-1):
      for i in range(tamanho -1): # indo até o penultimo indice
         if lista[i] > lista[i+1]:
          aux = lista[i]
          lista[i] = lista [i+1]
          lista[i+1] = aux
    return lista



lista = [6,8,2,3,5,4,1,7,9]

print(lista)

print(ordena_bubble_sort(lista))

 # forma direta Python:   lista[i] , lista[i+1] = lista[i+1] , lista[i]  
 # Varriavel de auxilio:  aux = lista[i] , lista[i] = lista[i+1] ,  lista[i+1]=aux
