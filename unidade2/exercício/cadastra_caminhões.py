#Um sistema precisa registrar o consumo diário de combustível de caminhões durante o mês.

#O dicionário deve ter:
#- Chave: tupla contendo placa e mês.
#- Valor: lista contendo os consumos diários.


def cadastra (dic,chave,consumo):
    if dic.get(chave):
        print("Já existe um cadastro")
    else:
        dias = int(input("Quantos dias desse mês: "))
        for i in range(dias):
            valor = int(input(f"Consumo do dia {i+1}: "))
            consumo.append(valor)
        dic[chave] = consumo
    return dic

def maior_consumo(dic):
    for chave in dic:
      maior = 0
      for consumo in dic[chave]:
       if consumo > maior:
        maior = consumo
       return maior

def media_caminhao(dic,chave):
    soma = 0
    for chave in  dic :
       for consumo in dic[chave]:
          soma += consumo
          media = soma/len(consumo)
          print(f"Media do caminhão {chave}: foi {media}")
    

   
#programa principal
chave =()
consumo = []
dic = {}

while True:
  op = int(input("Cadastra [1] sim [2] não "))
  if op == 1:
    placa = input("Qual placa do caminhão: ")
    mes = input("mês de consumo: ")
    chave = (placa,mes)
    cadastra(dic,chave,consumo)
  else:
     print("Encerrado")
     break

cadastro = cadastra(dic,chave,consumo)
maior = maior_consumo(cadastra(dic,chave,consumo))
c = media_caminhao(dic,chave)
print(cadastro)
print(f"Maior consumo foi {maior}")
print(c)