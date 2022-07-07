from datetime import date
from models import *
from crud import *


# ATENÇÃO
# Implementar os comandos usando as funções já criadas. Testar tudo a fim de encontrar possíveis bugs.
# Se encontrarem algum bug, tentem resolver e alertem sobre ele no grupo.


# Cadastrar peça - Israel
# def comando1():
#     return


# # Alterar peça - Israel
# def comando2():
#     return


# # Remover peça - Israel
# def comando3():
#     return


# # Cadastrar estilo - Edson
# def comando4():
#     return


# # Alterar estilo - Edson
# def comando5():
#     return


# # Remover estilo - Edson
# def comando6():
#     return


# # Listar todas as peças - Bruno
# def comando7():
#     return


# # Listar peças por tamanho e padrão - Bruno
# def comando8():
#     return


# # Listar estilos - Bruno
# def comando9():
#     return


# # Pesquisar estilo por nome - Israel
# def comando10():
#     return


# # Listar peças para venda - Israel
# def comando11():
#     return


# # Listar peças para doação - Israel
# def comando12():
#     return


# # Vender peça - Edson
# def comando13():
#     return


# # Doar peça - Edson
# def comando14():
#     return


# # Listar peças vendidas - Edson
# def comando15():
#     return


# # Listar peças doadas - Bruno
# def comando16():
#     return


# # Salvar alterações - Edson
# def comando17():
#     return


# # Carregar arquivos - Israel
# def comando18():
#     return


# # Finalizar programa - Bruno
# def comando0():
#     return


# def menu_comandos():
#     print("\nDigite: ")
#     print(" 1 --> Cadastrar uma peça")
#     print(" 2 --> Alterar uma peça")
#     print(" 3 --> Remover uma peça")
#     print(" 4 --> Cadastrar um estilo")
#     print(" 5 --> Alterar um estilo")
#     print(" 6 --> Remover um estilo")
#     print(" 7 --> Listar todas as peças")
#     print(" 8 --> Listar peças por tamanho e padrão")
#     print(" 9 --> Listar estilos")
#     print("10 --> Pesquisar estilo por nome")
#     print("11 --> Listar peças para venda")
#     print("12 --> Listar peças para doação")
#     print("13 --> Vender uma peça")
#     print("14 --> Doar uma peça")
#     print("15 --> Listar peças vendidas")
#     print("16 --> Listar peças doadas")
#     print("17 --> Salvar alterações")
#     print("18 --> Carregar arquivos")
#     print(" 0 --> Finalizar programa")
    

# def interface_usuario():
#     comando = -1

#     print("\n\n---------- Bem vindo ao Guarda-Roupa Virtual ----------")
#     while comando != 0:
#         menu_comandos()

#         try:
#             comando = int(input("\nO que deseja fazer? "))
#         except:
#             print("\n\nATENÇÃO: Digite apenas um número do menu")
#             continue

#         # Pega o comando do usuário e o executa
#         if comando == 1:
#             comando1()
#         elif comando == 2:
#             comando2()
#         elif comando == 3:
#             comando3()
#         elif comando == 4:
#             comando4()
#         elif comando == 5:
#             comando5()
#         elif comando == 6:
#             comando6()
#         elif comando == 7:
#             comando7()
#         elif comando == 8:
#             comando8()
#         elif comando == 9:
#             comando9()
#         elif comando == 10:
#             comando10()
#         elif comando == 11:
#             comando11()
#         elif comando == 12:
#             comando12()
#         elif comando == 13:
#             comando13()
#         elif comando == 14:
#             comando14()
#         elif comando == 15:
#             comando15()
#         elif comando == 16:
#             comando16()
#         elif comando == 17:
#             comando17()
#         elif comando == 18:
#             comando18()
#         elif comando == 0:
#             comando0()
#         else:
#             print("ATENÇÃO: Digite apenas um número do menu")
        
#     # Saiu do while, acabou o programa
#     print("\nGuarda-Roupa Virtual encerrado")

    
def main():
    inserir_peca(TIPO_CALCADO, TAMANHO_M, PADRAO_MASCULINO, COR_CINZA, date(2022, 6, 22), SITUACAO_DOACAO, 0.0)
    inserir_peca(TIPO_CALCADO, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_CALCADO, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    criar_estilo("clássico")
    adicionar_peca_a_estilo(pecas[0]["id"],"clássico")
    adicionar_peca_a_estilo(pecas[1]["id"],"clássico")
    adicionar_peca_a_estilo(pecas[2]["id"],"romântico")
    adicionar_peca_a_estilo(pecas[3]["id"],"romântico")
    listar_por_estilo()
    # interface_usuario()


if __name__ == "__main__":
    main()