# entrad e siada de dodos

#função "Print" par escreve ou mostra dado na tela

#exebindo texto na tela
print("Meu nome é Gabriel")

nome = "Gabriel"
#exebido dado variavel nome na tela
print(nome)

#A função print tem alguams formataçoes para exebiçãod e dados:
# mais ultilizada f"{}" ou %d , %f ,%c  %(valor1,valor2)
x =10
print(" %d é o valor da variavel X"%x)
print(f"{x} é o valor da variavel X")

#Função "input" para receber dados digitados

nome = input()# nesse caso  usar combinado com "Print" para exebir msg para user

# por padrão se não especifica o tipo o input receber dado como string
nome = input('Qual o seu nome?')
# especificando que dado que ser recebido é do tipo int(input())
raio = int(input('Digite o raio do círculo'))
media = float(input('Digite a media: '))