def perguntar() :
    return input("O que deseja realizar?\n" +
              "<I> - Para Inserir um USUARIO\n" +
              "<P> - Para Pesquisar um usuario\n" +
              "<E> - Para Excluir um usuario\n" +
              "<L> - Para Listar um usuario: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = input("Digite o nome:").upper(),
    input("Digite a última data de acesso: "),
    input("Qual a última estação acessada: ").upper()

    salvar(dicionario)

def pesquisar(dicionario):
    busca = input("\nDigite o login que deseja buscar: ")
    for elemento in dicionario.items():
        if busca == dicionario[elemento]:
            print("seu login é", dicionario[busca])

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))