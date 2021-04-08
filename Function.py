def somar_os_creditos():

    filer = open("C:\\Users\Lucca\Downloads\exemplo1.txt","r") # arquivo a ser lido
    #filew = open ("Soma_creditos.txt", "w") # novo arquivo otimizado
    global soma
    global resposta
    global var_mes 
    var_mes = '02'
    dic = {'01':'Janeiro','02':'Fevereiro','03':'Março','04':'Abril','05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro','1':'Janeiro','2':'Fevereiro','3':'Março','4':'Abril','5':'Maio','6':'Junho','7':'Julho','8':'Agosto','9':'Setembro',}
    lista_nao_somar_debitos =  ['PAG BOLETO', 'ENVIO TEV']
    lista_nao_somar_creditos = ['RESG AUTOM', 'ENVIO TEV']
    soma = 0


    for line in filer:
        line = line.rstrip()
        nline = line.split('"')
        

        if(len(nline)== 0): continue  # linha vazia

        if(nline[1].lower() == "conta"): continue # pular primeira linha continua o for

         #somar somente o mes desejado
        date = nline[3]
        
        if len(var_mes) == 1: ## se a pessoa digitar 01 digito
            if not date[5] == var_mes: continue # se nao for o mes desejado
        elif len(var_mes) == 2:
            if not date[4:6] == var_mes: continue    
        if var_mes not in dic:
            print("iiiih... isso que você digitou não tá legal não... \n Aposto que é o Marcos\n é número de 1 até 12 ta?!")
             
            break 

        pointer = nline[11]
        if(pointer == "C"):
            if(nline[7] in lista_nao_somar_creditos): continue      
            soma_creditos = soma_creditos + float(nline[9])

        elif(pointer == "D"):
            if(nline[7] in lista_nao_somar_debitos): continue      
            soma_debitos = soma_debitos + float(nline[9])

            soma = soma + valor
    soma = round(soma,2)
    print("R$" + str(soma))

    filer.close()
    
somar_os_creditos() 