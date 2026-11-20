# Recursividade
#função que chama ele mesmo
#Caso base - onde acontece a para da função


#Fatoria de um numero
def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero*fatorial(numero -1)

n = 4
resultado = fatorial(n)
print(resultado)

#fibonacci
def fibonacci (num):
    if num <= 1:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num - 2)

x = 4
r = fibonacci(x-1)
print(r)