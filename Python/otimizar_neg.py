### Esse script pega uma sequência de números/ variáveis
### positivas e negativas e separa todos os positivos dentro de um parentesis
### e todos os negativos em outro parentesis, depois de um sinal de =;



filer = open("proc_mari.txt","r") # arquivo a ser lido
filew = open ("proc_mari_otimizado.txt", "w") # novo arquivo otimizado
# cnt = 0
for line in filer.readlines(): # para cada linha do arquivo, executar:
    if(len(line.strip()) == 0): # se nao tiver nada na linha, sair do for!
        break

    # print("Linha %d" %cnt)
    # cnt = cnt +1
    aux = line.split('=')[0] # guardando qual aux está pegando

    temp_line = line.split('=')[1] # separando depois do =
    temp_line = ''.join(temp_line) # criando uma linha temporária, para juntar tudo depois do =
    nline2 = temp_line.split(';')[0] # pegando tudo antes do ;

    positivo = [] # lista para as variáveis que são positivas
    negativo = [] # lista para as variáveis que são negativas

    flag = 1 # flag criado para identificar positivos e negativos

    for i in nline2:

        if(i == '+'):
            flag = 1
        if (i == '-'):
            flag = 0
            negativo.extend('+')
            continue
        if (flag == 1):
            positivo.extend(i)
        if (flag == 0):
            negativo.extend(i)

    positivo = ''.join(positivo)
    negativo = ''.join(negativo)

    filew.write(aux + "=" + " " + "("+positivo +")" + " " + "-" + " " + "(" + negativo + ")" + ";" "\n")
filer.close()
filew.close()
