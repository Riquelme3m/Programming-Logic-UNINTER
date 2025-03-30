print("Bem-vindo a Loja de Gelados do Rogério Mendes")
print("---------------------------------------------")
print("-------------------Cardápio------------------")
print("---------------------------------------------")
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC) |----")
print("---|    P    |   R$  9.00   |  R$ 11.00 |----")
print("---|    M    |   R$ 14.00   |  R$ 16.00 |----")
print("---|    G    |   R$ 18.00   |  R$ 20.00 |----")
print("---------------------------------------------")

#Variável para acumular o valor total do pedido
valorTotalPedido = 0.00
valorTotalPedido = round(valorTotalPedido, 2)
while(True):
    
    
        sabor = input("Entre com o sabor desejado (CP/AC): ")
        #Função para colocar o sabor em letras minúsculas
        sabor = sabor.lower()
        #Verifica se o sabor é válido
        if(sabor != "cp" and sabor != "ac"):
            print("Sabor inválido. Tente novamente.")
            print("\n")
            continue
            
        tamanho = input("Entre com o tamanho desejado (P/M/G): ")
        tamanho.lower()
        if(tamanho!="p" and tamanho!="m" and tamanho!="g"):
            print("Tamanho inválido. Tente novamente.")
            print("\n")
            continue
        
        #Lógica para determinar o valor do produto
        if(sabor=="cp"):
            if(tamanho=="p"):
                valorProduto=9.00
            elif(tamanho=="m"):
                valorProduto=14.00
            elif(tamanho=="g"):
                valorProduto=18.00
        elif(sabor=="ac"):
            if(tamanho=="p"):
                valorProduto=11.00
            elif(tamanho=="m"):
                valorProduto=16.00
            elif(tamanho=="g"):
                valorProduto=20.00
         
        #Valor total do pedido é incrementado de acordo com os produtos escolhidos       
        valorTotalPedido += valorProduto
        if(sabor=="ac"):
            nomePedidoEscolha = "Açaí"
        elif(sabor=="cp"):
            nomePedidoEscolha = "Cupuaçu"
            
        print(f"Você pediu um {nomePedidoEscolha} no tamanho {tamanho.upper()}: R$ {valorProduto:.2f}")
        print("\n")
        novoPedido = input(str("Deseja mais alguma coisa? (S/N): "))
        
        novoPedido = novoPedido.lower()
        
        if(novoPedido=="s"):
            continue
        else:
            print(f"O valor total a ser pago: R$ {valorTotalPedido:.2f}")
            break