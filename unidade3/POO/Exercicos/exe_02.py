#Exercício 4: Turma de alunos com média de notas

#Problema : Escreva um programa em Python para criar uma Studentclasse que armazene as notas de um aluno namee uma lista de suas notas marks. Adicione um método average()que calcule e retorne a média de todas as notas.

class Alunos:
    def __init__(self,nome,notas):
        self.nome = nome
        self.notas = notas
    def media (self):
       soma = 0
       for i in self.notas:
          soma+=i
       return soma/3


nota = []

for i in range(3):
  nota.append(float(input(f"Nota Av{i+1} :  ")))

a1 = Alunos("João",nota)

print(a1.nome,a1.notas)
print(f"\nMedia:{a1.media():.2f}")

if a1.media() >= 5:
   print("Aprovado\n")
else:
   print("Reprovado\n")
