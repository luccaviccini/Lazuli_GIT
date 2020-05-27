filer = open("nomes_completos.txt","r") # arquivo a ser lido
filew = open ("iniciais.txt", "w") # novo arquivo otimizado



for nome in filer.readlines():
    split = nome.split()
    nonomes = len(split)
    iniciais = ""

    for i in range(nonomes):
        if(split[i] == "DE"):
            continue
        elif(split[i] == "DA"):
            continue
        elif(split[i] == "DO"):
            continue
        elif(split[i] == "DOS"):
            continue
        elif(split[i] == "DAS"):
            continue
        elif(split[i] == "E"):
            continue

        else:
            if(len(iniciais) == 0):
                iniciais = iniciais + split[i][0]
            else:
                iniciais = iniciais + "." + split[i][0]
    filew.write(iniciais + "\n")

filer.close()
filew.close()




















#print(line[0][0])
