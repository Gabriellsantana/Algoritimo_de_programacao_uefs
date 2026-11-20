# lista  class de dados multaveis ordenados com indice


sacola = []
print(type(sacola))

#metodos lista

#adiconado intens sempre no final  .append(item)
fruta = input("\nQual fruta deseja adicionar na sacola: ")

sacola.append(fruta)

print(f"sacola {sacola}")

#adiconado itens diretamente 
sacola.append(input("\nAdicione mais uma fruta na sacola: "))
print(f"sacola {sacola}")

#tirando item da sacola pelo sua etiqueta/indice e guardando
guarda = sacola.pop(int(input("\nQual fruta deseja retira: [indice]: ")))
print(sacola)
print(f"Você guardo a fruta {guarda}! ")

#Retirando item da sacola pelo seu nome mesmo/ valor
nome = input("\nQual a fruta deseja retira, informe o seu nome: ")
sacola.remove(nome)

if sacola:
    print(f"sacola {sacola}")
else:
    print("Sacola Vazia!!!")

#METODOS DA CLASSE LISTA FORA OS QUE JA ESTÃO ACIMA

# Lista.sort() = ordena valores da lista (valores de tipos iguais) 
#     lista = [c,d,a,b] , lista = [4,1,5,2,3]
#lista.sort , [a,b,c,d] ,         [1,2,3,4,5]

#Lista.insert (indice,valor) inserer valor no indice indicado
#lista[a,b,c]
#lista.insert(1,Z)
#lista[a,Z,b,c]


#Lista.reverse() inverte lista aocontrario 



