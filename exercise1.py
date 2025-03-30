print("Bem-vindo a Loja do Rogério Mendes")
valorProduto = float(input("Entre com o valor do produto: "))
quantidadeProduto = int(input("Entre com a quantidade do produto: "))
valorTotalSemDesconto = valorProduto * quantidadeProduto

#Lógica para calcular o desconto
if valorTotalSemDesconto < 2500:
    desconto = 0
elif valorTotalSemDesconto >= 2500 and valorTotalSemDesconto < 6000:
    desconto = 0.04
elif valorTotalSemDesconto >= 6000 and valorTotalSemDesconto < 10000:
    desconto = 0.07
elif valorTotalSemDesconto >= 10000:
    desconto = 0.11

valorTotalComDesconto = valorTotalSemDesconto - (valorTotalSemDesconto * desconto)
print("O valor SEM desconto: ", valorTotalSemDesconto)
print("O valor COM desconto: ", valorTotalComDesconto)