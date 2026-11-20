#Exercício 1: Classe Retângulo com Área e Perímetro

#Problema : Escreva um programa em Python para criar uma Rectangleclasse com length`a` ` widthp` como atributos de instância, e dois métodos: area()um que retorna a área e perimeter()outro que retorna o perímetro.

class Retangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura
    def perimetro (self):
        return 2*(self.base+self.altura)


r1 = Retangulo(10,4)
r2 = Retangulo(48,8)
r3 = Retangulo(15,5)

print(f"Area: {r1.area()} e Perimetro: {r1.perimetro()}")
print(f"Area: {r2.area()} e Perimetro: {r2.perimetro()}")
print(f"Area: {r3.area()} e Perimetro: {r3.perimetro()}")