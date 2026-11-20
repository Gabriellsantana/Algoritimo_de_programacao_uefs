#Operadores relacionais

# maior que
print (f"Dez é maior que cinco 10 > 5 :{10 > 5}")
#menor quer
print (f"Dez é menor que cinco 10 < 5 :{10 < 5}")
# comparaçao de igualdede
print (f"Dez é igual a cinco 10 == 5 :{10 == 5}")
# é diferente
print (f"Dez é diferente ou não igual a cinco 10 != 5 :{10 != 5}")
#ex
print(27 > 5) # verdadeiro
print(12 >= 10 + 5 - 3) # Verdadeiro
print(10 != 15 - 3 - 2) # Falso

# operadores logico para mais de um teste

#"E" / verdedadeiro e verdaderio = true , verdadeiro e falso = false , falso e falso = false - ex: Traga isso E traga aquilo 

print("\nOperador 'and' condição 'E' condição")
print(10 > 5 and 10 < 20)
print(10 == 5 and 10 < 20)

#"Ou" or  ou um coisa ou outra , verdade ou verdade = true , falso ou verdade = true , falso ou falso = false

print("\nOperador 'or' condição 'Ou' condição")
print(10 > 5 or 10 < 20)
print(10 == 5 or 10 < 20)

#"Not"  não , nega uma coisa , se for direta  not direita 

print("\nOperador 'not'  não (condição 'Ou' condição)")
print(not(10 > 5 and 10 < 20)) # verdaderio   / not  false
print(not(10 == 5 or 10 < 20)) # verdaderio   / not  false


# estrutur se  e senão    se isso : faça isso    senão: faça isso 
if 10 > 5:
    print("\nSim 10 é maior que  5")

if not(10 > 5):
    print()
else:
    print("10 continua maior que 5 mais você me pediu para nega isso!\n")
