# ARQUIVO BINARIO  ,arquvio que é lido por maquina em código ewm bytes 

import pickle # biblioteca para comando binario mais simples


#open = abrir
#close() = fecha

#var_arquivo = open ("nome_do_arquivo","modo")
#b = binario + metodos (w,r,a)

# wb   cria arquvio Binario para escrita
var_arquivo = open ("teste.bin","wb") # criando arquivo WB

# rb: abre arquivo binário preexistente somente para leitura.

#ab : abre arquivo binário para leitura/escrita no final (append).

#rb+ : abre arquivo binário preexistente para leitura/escrita.

#wb+ : cria arquivo binário para leitura/escrita.


#Comando de escrita em pickle:

#dump (objeto , arquivo)  : escrever ou adiciona no arquivo
n = 10
pickle.dump(n,var_arquivo)

#load(refarquivo)   : ler arquivo e recupera os dados e traduiz de byts paar objeto original
var_arquivo = open("teste.bin","rb")
recuperando = pickle.load(var_arquivo) #10
var_arquivo.close()

print("dados ",recuperando)

nome ="Gabriel"
#adiconado novo informaçoes sem apga oque ja tinha
var_arquivo = open("teste.bin","ab") #appedando
pickle.dump(nome,var_arquivo)
var_arquivo.close()

var_arquivo = open("teste.bin","rb")
recuperando = pickle.load(var_arquivo)

print("Mais dados adicionados ",recuperando)

