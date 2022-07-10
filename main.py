from datetime import date
from models import *
from crud import *


# ATENÇÃO
# Implementar os comandos usando as funções já criadas. Testar tudo a fim de encontrar possíveis bugs.
# Se encontrarem algum bug, tentem resolver e alertem sobre ele no grupo.


# Cadastrar peça - Israel
def comando1():
    # Definindo listas das variáveis já disponíveis
    lista_cores = [COR_AMARELO,COR_AZUL,COR_BRANCO,COR_CINZA,COR_LARANJA,COR_PRETO,COR_ROSA,COR_ROXO,COR_VERDE,COR_VERMELHO,COR_VIOLETA]
    lista_tipo = [TIPO_CALCADO,TIPO_INFERIOR,TIPO_SUPERIOR]
    lista_padrao = [PADRAO_UNISSEX,PADRAO_MASCULINO,PADRAO_FEMININO]
    lista_tamanho = [TAMANHO_G,TAMANHO_M,TAMANHO_P]
    lista_situacao = [SITUACAO_DOACAO,SITUACAO_FICAR,SITUACAO_VENDA]
    lista_estilos = list(estilos.keys())
    estilos_peca_nova = []
    lista_num_estilos = []

    # Cadastro do tipo da peça
    print("Ponha o tipo da peça: 'calçado', 'inferior' ou 'superior'")
    while True:
        try:
            tipo = input()
            tipo_tratado = tipo.lower()
            if tipo_tratado in lista_tipo:
                break
            else:
                print("Ponha o tipo 'calçado', 'inferior' ou 'superior'")  
        except ValueError: 
            print("Ponha apenas letras")

    # Cadastro do tamanho da peça
    print("\nPonha o tamanho da peça: 'p', 'm' ou 'g'")
    while True:
        try:
            tamanho = input()
            tamanho_tratado = tamanho.lower()
            if tamanho_tratado in lista_tamanho:               
                break
            else:
                print("Ponha o tamanho: 'p', 'm' ou 'g'")  
        except ValueError: 
            print("Ponha apenas letras")

    # Cadastro do padrão da peça
    print("\nPonha o padrão da peça: 'feminino', 'masculino' ou 'unissex'")    
    while True:
        try:
            padrao = input()
            padrao_tratado = padrao.lower()
            if padrao_tratado in lista_padrao:
                break
            else:
                print("Ponha o padrão: 'feminino', 'masculino' ou 'unissex'")  
        except ValueError: 
            print("Ponha apenas letras")
    
    # Cadastro da cor da peça
    print("\nPonha a cor da peça ")
    while True:
        try:
            cor = input()
            cor_tratado = cor.lower()
            if cor_tratado in lista_cores:
                break
            else:
                print("Ponha a cor: 'vermelho', 'azul', 'amarelo', 'rosa', 'branco', 'cinza', 'verde', 'preto', 'roxo', 'violeta' ou 'laranja' ")  
        except ValueError: 
            print("Ponha apenas letras")

    #Cadastro da situação da peça
    print("\nPonha a situação da peça: 'venda', 'doação' ou 'ficar'") 
    while True:
        try:
            situacao = input()
            situacao_tratado = situacao.lower()
            if situacao_tratado in lista_situacao:
                break
            else:
                print("Ponha a situação: 'venda', 'doação' ou 'ficar'")   
        except ValueError: 
            print("Ponha apenas letras")
    # Se a situação da peça for para venda, perguntar o preço da peça
    if situacao_tratado == "venda":
        print("\nPonha o preço da peça:")
        while True:
            try:
                preco_novo = float(input()) 
                break
            except ValueError:
                print("Ponha um número real para representar o preço:")
    
    #Cadastro dos estilos da peça
    print("\nQuantos estilos a peça está inserida: ")
    while True:
        try:
            n = int(input())
            if n >= 0:
                break 
            else:
                print("Ponha um número maior que ou igual a zero:")
        except:
            print("Ponha um número:")
    for j in range(n):
        for i in range(len(lista_estilos)):
            print("Digite %d para esolher o estilo "%(i+1), lista_estilos[i])
        print("digite 0 se a peça não faz parte desses estilos")
        while True:
            try:
                num_estilo =int(input())
                for i in range(len(lista_estilos)):
                    if num_estilo == i+1:
                        lista_num_estilos.append(num_estilo)
                        break 
                    if num_estilo == 0:
                        comando4()
                        estilos_peca_nova.append() #Adicionar depois de feita a parte do Edson
                        break
                print("Digite um dos números válidos")
            except ValueError:
                print("Digite apenas números") 
        print(" ")

    for i in num_estilo:
        # Estrutura condicional para tirar possíveis estilos repetidos
        if lista_estilos[i-1] not in estilos_peca_nova:
            estilos_peca_nova.append(lista_estilos[i-1])

    if len(pecas) != 0:
        id_novo = pecas[len(pecas)-1]["id"] + 1 
    else:
        id_novo = 1  
        
    peca_nova = {
         "id": id_novo
        ,"tipo": tipo_tratado
        ,"tamanho": tamanho_tratado 
        ,"padrão": padrao_tratado
        ,"cor": cor_tratado
        ,"data": date.today()
        ,"situação": situacao_tratado
        ,"preço": preco_novo  
        ,"estilos": estilos_peca_nova } 
    pecas.append(peca_nova) 


# Alterar peça - Israel
def comando2():
    print("Ponha o id da peça que deseja alterar:")
    try:
        id_peca = int(input())
    except ValueError:
        print("Ponha um número")
    tipo_peca  = 
    alterar_peca(id_peca,tipo_peca,tamanho_peca,padrao_peca,cor_peca,data_peca,situacao_peca,preco_peca)
    return





# Remover peça - Israel
def comando3():
    return


# Cadastrar estilo - Edson
def comando4():
    return


# Alterar estilo - Edson
def comando5():
    return


# Remover estilo - Edson
def comando6():
    return


# Listar todas as peças - Bruno
def comando7():
    return


# Listar peças por tamanho e padrão - Bruno
def comando8():
    return


# Listar estilos - Bruno
def comando9():
    return


# Pesquisar estilo por nome - Israel
def comando10():
    return


# Listar peças para venda - Israel
def comando11():
    return


# Listar peças para doação - Israel
def comando12():
    return


# Vender peça - Edson
def comando13():
    return


# Doar peça - Edson
def comando14():
    return


# Listar peças vendidas - Edson
def comando15():
    return


# Listar peças doadas - Bruno
def comando16():
    return


# Salvar alterações - Edson
def comando17():
    return


# Carregar arquivos - Israel
def comando18():
    return


# Finalizar programa - Bruno
def comando0():
    return


def menu_comandos():
    print("\nDigite: ")
    print(" 1 --> Cadastrar uma peça")
    print(" 2 --> Alterar uma peça")
    print(" 3 --> Remover uma peça")
    print(" 4 --> Cadastrar um estilo")
    print(" 5 --> Alterar um estilo")
    print(" 6 --> Remover um estilo")
    print(" 7 --> Listar todas as peças")
    print(" 8 --> Listar peças por tamanho e padrão")
    print(" 9 --> Listar estilos")
    print("10 --> Pesquisar estilo por nome")
    print("11 --> Listar peças para venda")
    print("12 --> Listar peças para doação")
    print("13 --> Vender uma peça")
    print("14 --> Doar uma peça")
    print("15 --> Listar peças vendidas")
    print("16 --> Listar peças doadas")
    print("17 --> Salvar alterações")
    print("18 --> Carregar arquivos")
    print(" 0 --> Finalizar programa")
    

def interface_usuario():
    comando = -1

    print("\n\n---------- Bem vindo ao Guarda-Roupa Virtual ----------")
    while comando != 0:
        menu_comandos()

        try:
            comando = int(input("\nO que deseja fazer? "))
        except:
            print("\n\nATENÇÃO: Digite apenas um número do menu")
            continue

        # Pega o comando do usuário e o executa
        if comando == 1:
            comando1()
        elif comando == 2:
            comando2()
        elif comando == 3:
            comando3()
        elif comando == 4:
            comando4()
        elif comando == 5:
            comando5()
        elif comando == 6:
            comando6()
        elif comando == 7:
            comando7()
        elif comando == 8:
            comando8()
        elif comando == 9:
            comando9()
        elif comando == 10:
            comando10()
        elif comando == 11:
            comando11()
        elif comando == 12:
            comando12()
        elif comando == 13:
            comando13()
        elif comando == 14:
            comando14()
        elif comando == 15:
            comando15()
        elif comando == 16:
            comando16()
        elif comando == 17:
            comando17()
        elif comando == 18:
            comando18()
        elif comando == 0:
            comando0()
        else:
            print("ATENÇÃO: Digite apenas um número do menu")
        
    # Saiu do while, acabou o programa
    print("\nGuarda-Roupa Virtual encerrado")

    
def main():
    inserir_peca(TIPO_CALCADO, TAMANHO_M, PADRAO_MASCULINO, COR_CINZA, date(2022, 6, 22), SITUACAO_VENDA, 121.7)
    inserir_peca(TIPO_CALCADO, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_CALCADO, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    
    print(historico_pecas_vendidas)
    listar_pecas_vendidas()
    carregar_historico_pecas_vendidas()
    listar_pecas_vendidas()
    # interface_usuario()


if __name__ == "__main__":
    main()