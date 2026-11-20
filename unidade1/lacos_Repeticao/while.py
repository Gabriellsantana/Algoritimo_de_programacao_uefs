#Equanto faça
# laço de repetição ultilizado com frequencia qunado não se sabe quntas vezes sera necessario roda ou tmabém quando se sebe

#programa que mostra frese "Hello Wolord " 5 venzes na tela

#inicio
quant = 0 # variavel de controle sendo inciada
#Enquanto
while quant < 5:#faça
    print("Hello World")

    quant +=1 #variavel de contrele sendo atulizada a cada loop
#fim enquanto 

#
op = 0
while op != 3:
  print("\n\n----Menu----")
  print("[1] Inicia")
  print("[2] lista")
  print("[3] sair")
  op =int(input())
print("Menu encerrado. . . . ........")

#
while True:
   print("\n\nOutra opção de menu")
   print("[1] Inicia")
   print("[2] lista")
   print("[3] sair")
   op =int(input())
   if op == 3:
      break

# USANDO WHILE PARA TRATA ERRO DO USUSUARIO COM NETREDA INVALIDAS

n = int(input("\nCrie um  senha de numeros: "))

senha = int(input("\nConfirme sua senha: "))
while n != senha:
   print("\nSenha Invalidaa")
   senha = int(input("\nConfirme sua senha: "))

print("\n\nsenhas criada com sucesso!!!\n")

#While pode ser usado com else
x = 0
while x < 4:
   print("estou quantando  ")
   x +=1
else:
   print("\n terminei")