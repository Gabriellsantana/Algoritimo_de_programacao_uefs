#Exercício 5: Classe de Produto com Calculadora de Valor de Estoque

#Problema : Escreva um programa em Python para criar uma Productclasse com três atributos de instância: namepreço, pricequantidade e quantityvalor. Adicione um método total_value()que retorne o valor total do estoque multiplicando o preço pela quantidade.


class Produto:
    def __init__(self,nome,quant,valor):
        self.nome = nome
        self.quant = quant
        self.valor = valor
    def valortotal(self):
        return self.quant*self.valor

dic ={}#dicionario

while True:
    op = input("[1] cadastra [2] sair: ")
    if op =="2":
        break
    else:
         nome = input("Nome Produto: ")
         quant = int(input("Qunatindade: "))
         preco = float(input("Preço R$: "))
         dic[nome] = Produto(nome,quant,preco) 

print()
for nome,produto in dic.items():
    print(f"Nome:{dic[nome].nome}\nQuantidade:{dic[nome].quant}\nR$:{dic[nome].valor}\n")
    print(produto.valortotal())