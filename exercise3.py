
#Função para determinar o tipo de serviço
def escolha_servico():
    
    while(True):
        
        print("Entre com o tipo de serviço desejado");
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        tipoServico = input(">>")
        tipoServico = tipoServico.lower()
        if tipoServico != "dig" and tipoServico != "ico" and tipoServico != "ipb" and tipoServico != "fot": 
            print("Escolha inválida, entre com o tipo do serviço novamente\n")
            
            continue
        else:
            if(tipoServico=="dig"):
                valorServico = 1.10
            elif(tipoServico=="ico"):
                valorServico = 1.00
            elif(tipoServico=="ipb"):
                valorServico = 0.40
            elif(tipoServico == "fot"):
                valorServico = 0.20
            break
    return valorServico      

def num_pagina():
    
   
    while(True):
        
        try:
            numeroDePaginas = int(input("Entre com o número de páginas: "))
            if(numeroDePaginas>=20000 or numeroDePaginas<0):
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.\n")
                continue
            else:
                break
        except ValueError:
            print("Por favor, entre com o número de páginas novamente\n")
            continue
    if(numeroDePaginas>=20 and numeroDePaginas<200): numeroDePaginas=numeroDePaginas - (numeroDePaginas*0.15)
    elif(numeroDePaginas>=200 and numeroDePaginas<2000): numeroDePaginas = numeroDePaginas - (numeroDePaginas*0.2)
    elif(numeroDePaginas>=2000 and numeroDePaginas<20000): numeroDePaginas = numeroDePaginas - (numeroDePaginas*0.25)
    return numeroDePaginas

def servico_extra():
    while(True):
        print("Deseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        servicoAdicional = str(input(">>"))
        
        if servicoAdicional!= "0" and servicoAdicional!= "1" and servicoAdicional!="2":
            continue
        else:
            if(servicoAdicional=="1"):valorServicoAdicional=15.00
            elif(servicoAdicional=="2"):valorServicoAdicional=40.00
            elif(servicoAdicional=="0"):valorServicoAdicional=0.00
            break
    
    
    return valorServicoAdicional

   
    
while(True):
        print("Bem vindo a Copiadora do Rogério Mendes\n")
        
        #Chama a função que pega o tipo ed serviço que o cliente deseja
        valorServico = escolha_servico()
        
        
        #Chama a função que pega o número de páginas
        numeroDePaginas = num_pagina()
        print("\n")
        #Chama a função que pega o tipo de serviço extra que o cliente deseja
        valorServicoAdicional  = servico_extra()
        
       
        
        
        preco = (valorServico*numeroDePaginas) + valorServicoAdicional
        print(f"Total R${preco:.2f} (servico: {valorServico} * páginas: {numeroDePaginas:.2f} + extra: {valorServicoAdicional:.2f})")
        break
        
