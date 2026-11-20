
def cadastra (dic,chave,consumo):
    consumo =[]
    if dic.get(chave):
        print("Já existe um cadastro")
    else:
        dias = int(input("Quantos dias desse mês: "))
        for i in range(dias):
            valor = int(input(f"Consumo do dia {i+1}: "))
            consumo.append(valor)
        dic[chave] = consumo
    return dic


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
resultado = cadastra(dic,chave,consumo)
print(resultado)