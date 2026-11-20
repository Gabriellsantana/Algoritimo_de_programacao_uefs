

#Escreva um programa que contenha uma função recursiva que calcule be em que b e e são números inteiros positivos.


def elevado (b,e):
    if e == 0:
        return 1
    else:
      return b* elevado(b,e-1)

r = elevado(5,2)
print(r)