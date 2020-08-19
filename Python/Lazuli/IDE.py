from tkinter import *
from tkinter import filedialog
###### DICIONÁRIO:  KEYS COMO NUMEROS E ITENS COMO NOME DOS MESES ######
global dic
global resposta
dic = {'01':'Janeiro','02':'Fevereiro','03':'Março','04':'Abril','05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro','1':'Janeiro','2':'Fevereiro','3':'Março','4':'Abril','5':'Maio','6':'Junho','7':'Julho','8':'Agosto','9':'Setembro',}

###### FUNÇÕES ######
def restart_programa():

    botao_abrir['state'] = NORMAL
    botao_somar['state'] = DISABLED
    mes['state'] = DISABLED
    my_label.destroy()
    my_label2.destroy()
    resposta.destroy()

def abrir_arquivo():
    global my_label
    root.filename = filedialog.askopenfilename(title = "Coloque o arquivo no formato TXT", filetypes = (("Arquivos no formato TXT", "*.txt"), ("Todos os arquivos", "*.*")))
    my_label = Label(frame, text = "Show, agora coloca o número do mês")
    my_label.pack()
    botao_abrir['state']    = DISABLED
    botao_ok['state']    = NORMAL
    mes['state'] = NORMAL



def pegar_mes():
    global var_mes
    global my_label2

    var_mes = mes.get()
    if not var_mes  in dic:
        my_label2 = Label(frame3, text = "iiiih... isso que você digitou não tá legal não... \n Aposto que é o Marcos \n É número de 1 até 12 ta?!\n Reinicia lá em baixo e tenta de novo!!")
        my_label2.pack()   
        botao_ok['state']    = DISABLED
        botao_somar['state'] = DISABLED 

    else:     
        my_label2 = Label(frame3, text = dic[var_mes] + '!\n ' "Agora é só somar ali embaixo.")
        my_label2.pack()
        botao_ok['state']    = DISABLED
        botao_somar['state'] = NORMAL
    

def somar_os_creditos():

    filer = open(root.filename,"r") # arquivo a ser lido
    #filew = open ("Soma_creditos.txt", "w") # novo arquivo otimizado
    global soma
    
    soma = 0


    for line in filer:
        line = line.rstrip()
        nline = line.split('"')
        

        if(len(nline)== 0): continue  # linha vazia

        if(nline[1].lower() == "conta"): continue # pular primeira linha

         #somar somente o mes desejado
        date = nline[3]
        
        if len(var_mes) == 1: ## se a pessoa digitar 01 digito
            if not date[5] == var_mes: continue # se nao for o mes desejado
        elif len(var_mes) == 2:
            if not date[4:6] == var_mes: continue    
        if var_mes not in dic:
            my_label2 = Label(frame3, text = "iiiih... isso que você digitou não tá legal não... \n Aposto que é o Marcos\n é número de 1 até 12 ta?!")
            my_label2.pack()   
            break 

        pointer = nline[11]
        if(pointer == "C"):
            if(nline[7] == "RESG AUTOM"): continue

            soma = soma + float(nline[9])

    soma = round(soma,2)

    resposta = Label(frame2, text = "R$ "+ str(soma))
    resposta.pack()

    filer.close()


    #botao_abrir['state']    = DISABLED
    botao_somar['state']    = DISABLED
    #botao_reinicar['state'] = NORMAL


root = Tk()
root.title('Somar extratos com C do Mês desejado')

###### PRIMEIRO FRAME ########
frame = LabelFrame(root, text = "Passo 1: Abrir o aquivo no formato TXT", padx=20, pady = 40)
frame.pack(padx=50, pady = 50)

botao_abrir = Button(frame, text = "Abrir Extrato no Formato TXT", command = abrir_arquivo, state = NORMAL)
botao_abrir.pack()

######  FRAME DO MEIO ######

frame3 = LabelFrame(root, text = "Passo 2: Escrever o número do mês e clicar OK:", padx=20, pady = 40)
frame3.pack(padx=50, pady = 50)

#text box
mes = Entry(frame3, width = 10, state = DISABLED)
mes.pack( padx=4, pady=4 )
#botao ok
botao_ok = Button(frame3, text = 'OK', command = pegar_mes, state = DISABLED)
botao_ok.pack()


###### FRAME EMBAIXO
frame2 = LabelFrame(root, text = "Passo 3: Somar!", padx=20, pady = 40)
frame2.pack(padx=50, pady = 50)

#botao_abrir.grid(row = 0, column = 0)
botao_somar = Button(frame2, text = "Somar", command = somar_os_creditos, state = DISABLED)
botao_somar.pack()
botao_reinicar = Button(root, text = "Reiniciar", command = restart_programa, state = NORMAL)
botao_reinicar.pack()

root.mainloop()



