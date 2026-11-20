# FUNÇÃO RANGE()

#O TIPO RANGE REPRESENTA UMA SEQUÊNCIA IMUTÁVEL DE NÚMEROS E É COMUMENTE USADO PARA PERCORRER UM NÚMERO DETERMINADO DE VEZES EM UM LAÇO FOR.

# É IMPORTANTE RESSALTAR QUE NA VERSÃO 3.X DO PYTHON, A FUNÇÃO RANGE() RETORNA UM OBJETO DO TIPO RANGE (UMA SEQUÊNCIA IMUTÁVEL) E NÃO MAIS UMA LISTA COM ELEMENTOS. POR ISSO, QUANDO VOCÊ QUISER VER OS NÚMEROS OU PRECISAR DE UMA LISTA DE VERDADE, CONVERTA O RETORNO COM A FUNÇÃO LIST().

#Quando você passa apenas um parâmetro para a função range() em Python, como em range(5), o Python assume que esse valor é o limite superior (o valor final) por uma questão de design da linguagem para simplificar o uso mais comum.

#A assinatura completa do range é range(start, stop[, step]). No entanto, os criadores do Python definiram que:

#• O parâmetro obrigatório é o stop.
#• Se o start não for enviado, ele assume o valor padrão de 0.
#• Se o step (passo) não for enviado, ele assume o valor padrão de 1.

# A FUNÇÃO PODE TER ATÉ TRÊS PARÂMETROS
inicio = 1
fim = 10
passo = 2

#range(inicio) start
print(list(range(1)))
print(list(range(inicio)))
print()

#range(inicio,fim) O fim (stop) nunca é incluído
print(list(range(1,10)))
print(list(range(inicio,fim)))
print()

#range(inicio,fim,passo) step
print(list(range(1,10,2)))
print(list(range(inicio,fim,passo)))
print()

#range(inicio,fim,,passo)
print(list(range(10,1,-1)))


#Passo negativo: contagem regressiva
#Com step negativo, o range anda para trás. Nesse caso o início precisa ser maior que o fim, e o fim continua exclusivo:

print(list(range(10, 0, -2)))    # para no 2: o 0 é o fim, e não entra

print(list(range(10, -1, -2)))   # para incluir o 0, o fim vira -1

print(list(reversed(range(1, 6))))

#AVANÇANDO

#Uma dúvida comum (e pergunta frequente de prova) é quando usar range() e quando usar enumerate():

#range() gera números. Use para repetir algo N vezes ou para produzir uma sequência numérica.

#enumerate() percorre uma coleção e entrega pares (índice, valor). Use quando você precisa do item e da posição dele.

#O padrão range(len(lista)) funciona, mas obriga a acessar lista[i] na mão. O enumerate faz o mesmo de forma mais legível:

frutas = ['maçã', 'banana', 'uva']

# Com range(len()): funciona, mas é mais verboso
for i in range(len(frutas)):
    print(i, frutas[i])

# Com enumerate: mais idiomático
for i, fruta in enumerate(frutas):
    print(i, fruta)

# enumerate também pode começar a contagem em 1
for posicao, fruta in enumerate(frutas, start=1):
    print(posicao, fruta)
