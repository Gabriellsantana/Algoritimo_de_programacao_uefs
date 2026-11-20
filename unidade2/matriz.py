#Matriz  = lista de lista

#lista = [[],[],[]]
# acessa elementode um matriz   , nota[linha][coluna]

#Matriz nota Aluno
nota =[]

for i in range (3):
  linha = []
  for c in range(4):
    linha.append(0)
  nota.append(linha)


for linha in nota:
  for coluna in linha:
    print(nota ,end ="") 