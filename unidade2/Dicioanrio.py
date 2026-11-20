# d.get(chave, [padrão]): Retorna o valor da chave. Se ela não existir, retorna None (ou o valor padrão definido), evitando erros do tipo KeyError.

# d.keys(): Retorna uma visualização (view) com todas as chaves do dicionário.

# • d.values(): Retorna uma visualização com todos os valores do dicionário.

#• d.items(): Retorna uma visualização com tuplas no formato (chave, valor)

#• d.pop(chave, [padrão]): Remove a chave especificada e retorna o seu valor. Se a chave não existir e um padrão for informado, retorna o padrão; caso contrário, gera KeyError.

#• d.popitem(): Remove e retorna o último par (chave, valor) inserido no dicionário (em formato de tupla).


#• d.clear(): Esvazia o dicionário por completo, deixando-o com {}.

#items() → Retorna pares chave-valor
#clear() → Limpa o dicionário
#update() → Atualiza ou mescla com outro dicionário
#pop() → Remove e retorna o valor de uma chave específica
#popitem() → Remove o último par inserido
#copy() → Cria uma cópia superficial do dicionário
#get() → Retorna o valor de uma chave sem gerar erro, podendo definir valor padrão

#Dicionario caica com etiquetas

dados = {
    "Nome":"Gabriel",
    "Idade": 18,
    "Estado":"Bhaia"
}
print(type(dados))
print(dados)

# get() verifica se um cahave existe e tem valor / retorna none por padrão se não hover ou e possivel esepcisa o valor ex dic.get(chave, instrução)

print(dados.get(1))
print(dados.get("Gabriel","Não existe essa chave"))
print(dados.get("Gabriel",False))
print(dados.get("Nome"))

# atribuidno no valores 
dados["Nome"] = "João"
dados["Idade"] = input(f"Qual idade do {dados["Nome"]}: ")
print(dados)

#crinado novas chaves e valores
dados[input("Crie uma chave: ")] = input("valor da chave: ")
print(dados)

#crinado novas chaves e valores
salario = "Salario"
valor = float(input("Qual valor do salario: "))
dados[salario] = valor
print(dados)
print()

#metodo keys() retorna apenas as chaves  dic[chave, chave , . . . .]
print(dados.keys())#return list lista da chaves
#metodo Values() rotorna apenas o valores dic[valor, valor , . . . .]
print(dados.values()) #return list lista dos valoures

print(dados.items()) #return uma tuplas , porque ele pega os dois valores (chave:valor)
