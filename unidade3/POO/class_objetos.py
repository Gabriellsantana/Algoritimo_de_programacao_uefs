1 # class Classes são moldes para criar novos objetos
2 # As classes geram novos objetos ou (instâncias) que
3 # podem ter seus próprios atributos e métodos.
4 # Os objetos gerados pela classe podem usar seus dados
5 # internos para realizar várias ações.

#criando Classa - Mode
class Pessoas:
   def __init__(self,sexo,idade): #Metodo Contrutor 
      self.sexo =sexo   # atributos or metodos
      self.idade =idade # atributos or metodos


gabriel = Pessoas("Masculino",20) # iniciando/criando objeto
maria =Pessoas("Fmenino",25) # iniciando/criando objeto

print(gabriel.sexo,gabriel.idade)

print(maria.sexo)
print(maria.idade)
#-------------------------------------------------------------------------------------

#Madando dados e recebendo  dados
class Carro:
   def __init__(self,nome,cor,ano):#construtor do objeto
      self.nome = nome
      self.cor = cor
      self.ano = ano

   def acelerando(self):# comportamento especifico que obj pode realizar 
       print(f"{self.nome} esta acelerando . . .")

nome = input("Nome do carro: ")
cor = input("cor: ")
ano = input("Ano: ")

carro = Carro(nome,cor,ano)
carro.acelerando()

print()


#Matendo o metodo/ação / estado da class
class Camera:
   def __init__(self,camera, filmando = False):
      self.camera = camera
      self.filmando = filmando

   def filmar(self):#metodo acão
      self.filmando = True 
      print(f"{self.camera} esta Filmando")

c1 = Camera("Sony")
c2 = Camera("Aure")

print(c1.camera,c1.filmando)
print(c2.camera,c2.filmando)

c1.filmar()# estado de um ação atual

print(c1.camera,c1.filmando)#manteve a  açao isntansciada
print(c2.camera,c2.filmando)

#Atributos da class (variavel de class)
class identindade:
   ano_atual = 2026

   def __init__(self,nome,id):
      self.nome = nome
      self.id = id

   def nascimento(self):
      return (self.id -identindade.ano_atual)

p1 = identindade("Matheus",25)
p2 = identindade("Júlia",28)

print(p1.nome,p1.nascimento())
print(p2.nome,p2.nascimento())

#Var e __dict__ para atributos de instancia
print(p1.__dict__)# todos os dados de class é guardado dentro de um dicionario
print(vars(p1))

p1.__dict__["naturalidade"] ="Brasil-BA"
print(p1.__dict__)