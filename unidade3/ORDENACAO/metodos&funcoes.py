
#metod de ordenações


#Função sorted
# terá como retorno uma nova lista ordenada: por isso a nescesiade de salvar em uma var
lista = [56,3,9,32,1,6,3]
print("\nFUNÇÃO SORTED()")
print(f"List: {lista}")

novaLista= sorted(lista)
print(f"List: {novaLista} Nova lista ordenada\n")


#método list.sort().
#Ele modificará a lista localmente (e retornará None para evitar confusão). 
print("\nMetódo sort()")
l = [9,8,7,6,5,4,3,2,1]
n = ["e","a","c","d","b","f","g","h"]

print(f"List:{l}")
print(f"List:{n}\n")

l.sort()
n.sort()
print(type(l.sort()))
print(type(l))
print(f"\n{l}")
print(f"{n}\n")

#Usualmente este método é menos conveniente que a função sorted() - mas, se a lista original não for posteriormente útil, esta maneira será levemente mais eficiente.

#Outra diferença é que o método list.sort() é aplicável apenas às listas. Em contrapartida, a função sorted() aceita qualquer iterável.