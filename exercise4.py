

#Declaração do incrementador representandos os id's e do dicionário para armazenar os livros

lista_livro = [] 
id_global = 0


def cadastrar_livro(id):
    print("--------------------------------------------")
    print("---------- MENU CADASTRAR LIVRO ------------")
    print(f"Id do livro: {id}")
    nome = input("Por favor entre com o nome do livro: ")
    autor = input("Por favor entre com o autor do livro: ")
    editora = input("Por favor entre com a editora do livro: ")
    livro = {"id":id,"nome":nome,"autor":autor,"editora":editora}
    lista_livro.append(livro)
    


def consultar_livro():
    
    while True:
        print("--------------------------------------------")
        print("---------- MENU CONSULTAR LIVRO ------------")
        print("Escolha a opção desejada:")
        print("1. Consultar Todos os Livros\n2. Consultar por Id\n3. Consultar Livro(s) por autor\n4. Retornar")
        opcao = input(">>")
        print("------------")
        if opcao == "1":
            for livro in lista_livro:
                print("id: ",livro["id"])
                print("nome: ",livro["nome"])
                print("autor: ",livro["autor"])
                print("editor: ",livro["editora"])
                print("\n")
            print("------------")
        elif opcao == "2":
            id_consulta = int(input("Digite o id do livro: "))
            encontrados = [livro for livro in lista_livro if livro["id"] == id_consulta]
            if encontrados:
                for livro in encontrados:
                    if livro["id"] == id_consulta:
                        print("id: ",livro["id"])
                        print("nome: ",livro["nome"])
                        print("autor: ",livro["autor"])
                        print("editor: ",livro["editora"])
                        print("\n")
                        break
            else:
                print("Nenhum livro encontrado para este id")
            print("------------")
        
        
        
        elif opcao == "3":
            autor_consulta = input("Digite o autor do livro: ")
            print("------------")
            encontrados = [livro for livro in lista_livro if livro["autor"] == autor_consulta]
            if encontrados:
                for livro in encontrados:
                    print("id: ",livro["id"])
                    print("nome: ",livro["nome"])
                    print("autor: ",livro["autor"])
                    print("editor: ",livro["editora"])
                    print("\n")
                print("------------")
                    
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida")
            continue


def remover_livro():
    while True:
        id_remover = int(input("Digite o id do livro a ser removido: "))
        for livro in lista_livro:
            if livro["id"] == id_remover:
                lista_livro.remove(livro)
                print("Livro removido com sucesso!")
                return
        print("Id inválido.")
        continue
        
        

print("Bem-vindo à Livraria do Rogério Mendes")
while(True):
    
   
    print("--------------------------------------")
    print("---------- MENU PRINCIPAL ------------")
    print("Escolha a opção desejada:")
    print("1. Cadastrar Livro\n2. Consultar Livro(s)\n3. Remover Livro\n4. Sair")
    option = input(">>")
    if(option == "1"):
        id_global += 1
        cadastrar_livro(id_global)
        
    elif(option == "2"):
        consultar_livro()
    elif(option == "3"):
        remover_livro()
    elif(option == "4"):
        break
    else:
        print("Opção inválida")
        continue

        
