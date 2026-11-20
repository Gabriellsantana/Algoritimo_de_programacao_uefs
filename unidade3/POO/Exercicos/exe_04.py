#Exercício 6: Conta bancária com proteção contra depósitos e sobregiro

#Problema: Escreva um programa em Python para criar uma classe chamada ContaBancaria, com um atributo chamado saldo e dois métodos: depositar(valor), que adiciona dinheiro ao saldo da conta, e sacar(valor), que retira dinheiro do saldo, mas impede que o saldo fique negativo.

#Objetivo : Aprender validação de dados e lógica condicional dentro de métodos de instância. Evitar o estouro de buffer é uma regra de negócios do mundo real, e implementá-la aqui ensina como as classes podem impor restrições aos seus próprios dados, uma ideia central por trás do encapsulamento em Programação Orientada a Objetos.

class ContaBancaria:
    def __init__ (self,saldo):
        self.saldo = saldo
    def depositar(self,dep):
        if dep > 0:
         self.saldo += dep
        else:
           print("valor invalido ")
    def sacar(self,sac):
        if self.saldo > 0:
            print(f"Saldo:R${self.saldo}")
            if sac > self.saldo:
                return print("saldo insuficiente para sacar . . .\n ")
            else:           
                 self.saldo -= sac 
                 return print(f"\nSaldo atual:${self.saldo}\nSaque:R$ {sac}")


conta = ContaBancaria(1)# crie objeto

while True:
    try:
     op = int(input("1- depositar\n2- sacar \n\n"))
     if op == 1:
        d = int(input("Valor R$: ")) 
        conta.depositar(d)
        print(conta.saldo)
     elif op == 2:
        s = int(input("Valor R$: ")) 
        print(conta.sacar(s))
    except:
        print("Opção invalida ")
