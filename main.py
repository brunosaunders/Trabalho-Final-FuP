from cmath import e
from datetime import date
from models import *
from crud import *

# Variável para checar se existem alterações que precisam ser salvas.
informacao = {
    "alteradas": False
}

# ATENÇÃO
# Implementar os comandos usando as funções já criadas. Testar tudo a fim de encontrar possíveis bugs.
# Se encontrarem algum bug, tentem resolver e alertem sobre ele no grupo.


lista_cores = [COR_AMARELO,COR_AZUL,COR_BRANCO,COR_CINZA,COR_LARANJA,COR_PRETO,COR_ROSA,COR_ROXO,COR_VERDE,COR_VERMELHO,COR_VIOLETA]
lista_tipo = [TIPO_CALCADO,TIPO_INFERIOR,TIPO_SUPERIOR]
lista_padrao = [PADRAO_UNISSEX,PADRAO_MASCULINO,PADRAO_FEMININO]
lista_tamanho = [TAMANHO_G,TAMANHO_M,TAMANHO_P]
lista_situacao = [SITUACAO_DOACAO,SITUACAO_FICAR,SITUACAO_VENDA] 
mes_com30 = ["04","06","09","11"]
mes_com31 = ["01","03","05","07","08","10","12"]

# Cadastrar peça - Israel
def comando1():
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

    # Cadastro da data da peça 
    print("\nPonha a data da peça:")
    print("Insira o ano da peça:")
    # Cadastro do ano
    while True:
        try: 
            ano = input() 
            if len(ano) == 4 and int(ano) >=0: 
                break 
            else:
                print("Ponha um número de 4 digitos")
        except ValueError:
            print("Ponha um número") 
    print("\nInsira o mês da peça:")
    # Cadastro do mês
    while True:
        try:
            mes = input()
            if len(mes) == 2 and int(mes) <= 12 and int(mes) > 0:
                break
            else:
                print("ponha um número maior que zero de 2 digitos")
        except ValueError:
            print("Ponha um número")  
    print("\nInsira o dia da peça:")
    # Cadastro do dia considerando se o mês é de 30 dias, 31 dias ou se o ano é bissexto
    while True:
        try:
            dia = input()
            if len(dia) == 2 and int(dia) >= 1:
                if mes in mes_com30: 
                    if int(dia) <= 30:
                        break
                    else:
                        print("O mês selecionado só vai até 30")
                if mes in mes_com31: 
                    if int(dia) <=31:
                        break
                    else:
                        print("O mês selecionado só vai até 31")
                if mes == "02": 
                    if int(ano)%4 == 0:
                        if int(dia) <= 29:
                            break 
                        else:
                            print("No ano selecionado, o mês de fevereiro só vai até 29") 
                    else:
                        if int(dia) <= 28:
                            break 
                        else:
                            print("No ano selecionado, o mês de fevereiro só vai até 28")
            else:
                print("Ponha um número de 2 dígitos, maior que zero") 
        except ValueError:
            print("Ponha um número") 
    data = ano + "-" + mes + "-" + dia
    data_nova = datetime.fromisoformat(data).date() 

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
                if preco_novo >= 0:
                    break
                else:
                    print("Ponha um número maior que ou igual a zero:")
            except ValueError:
                print("Ponha um número:") 
    else:
        preco_novo == 0.0

    # Chamando a função inserir_peca
    inserir_peca(tipo_tratado, tamanho, padrao_tratado, cor_tratado, data_nova, situacao_tratado, preco_novo)


# Alterar peça - Israel
def comando2():

    if len(pecas) == 0:
        print("\nNão existem peças para serem alteradas")
        return

    print("Ponha o id da peça que deseja alterar:")
    try:
        id_peca = int(input())
    except ValueError:
        print("Ponha um número") 

    peca_para_alteracao = "" # Inicializa para comparar depois
    #Identificando e armazenando em uma variável a peça
    for cada_peca in pecas: 
        if cada_peca["id"] == id_peca:
            peca_para_alteracao = cada_peca 

    # Verifica se alguma peça foi encontrada, caso não, retorna
    if peca_para_alteracao == "":
        print(f"\nPeça de id {id_peca} não encontrado!")
        return

    # Cada parte da data da peça sem alteração
    data_sem_alterar = str(peca_para_alteracao["data"])
    ano_sem_alterar = data_sem_alterar[:4] 
    mes_sem_alterar = data_sem_alterar[5:7] 
    dia_sem_alterar = data_sem_alterar[8:]

    # Pôr a alteração no tipo da peça
    print("Ponha o tipo da peça alterada: 'calçado', 'inferior' ou 'superior'")
    print("Caso não deseje alterar o tipo aperte enter.")
    while True:
        try:
            tipo_peca = input()
            tipo_peca_tratado = tipo_peca.lower()
            if tipo_peca_tratado in lista_tipo:
                break
            else:
                print("\nPonha o tipo 'calçado', 'inferior' ou 'superior'")  
        except ValueError: 
            print("\nPonha apenas letras") 
    
    # Alteração do tamanho da peça
    print("\nPonha o tamanho da peça alterada: 'p', 'm' ou 'g'")
    print("Caso não deseje alterar o tamanho aperte enter.")
    while True:
        try:
            tamanho_peca = input()
            tamanho_peca_tratado = tamanho_peca.lower()
            if tamanho_peca_tratado in lista_tamanho:               
                break
            else:
                print("\nPonha o tamanho: 'p', 'm' ou 'g'")  
        except ValueError: 
            print("\nPonha apenas letras") 

    # Alteração do padrão da peça  
    print("\nPonha o padrão da peça alterada: 'feminino', 'masculino' ou 'unissex'") 
    print("Caso não deseje alterar o padrão aperte enter.")   
    while True:
        try:
            padrao_peca = input()
            padrao_peca_tratado = padrao_peca.lower()
            if padrao_peca_tratado in lista_padrao:
                break
            else:
                print("\nPonha o padrão: 'feminino', 'masculino' ou 'unissex'")  
        except ValueError: 
            print("\nPonha apenas letras")

    # Alteração da cor da peça
    print("\nPonha a cor da peça alterada: ")
    print("Caso não deseje alterar a cor aperte enter.")
    while True:
        try:
            cor_peca = input()
            cor_peca_tratado = cor_peca.lower()
            if cor_peca_tratado in lista_cores or cor_peca_tratado == "":
                break
            else:
                print("Ponha a cor: 'vermelho', 'azul', 'amarelo', 'rosa', 'branco', 'cinza', 'verde', 'preto', 'roxo', 'violeta' ou 'laranja' ")  
        except ValueError: 
            print("Ponha apenas letras")
    
    # Altera a data da peça
    print("\nPonha a data da peça alterada:")
    print("Insira o ano da peça alterada:")
    print("Caso não deseje alterar a ano da peça aperte enter.")
    while True:
        try: 
            ano = input() 
            if len(ano) == 4 or ano =="": 
                break 
            else:
                print("\nPonha um número de 4 digitos")
        except ValueError:
            print("\nPonha um número") 

    print("\nInsira o mês da peça:")
    print("Caso não deseje alterar o mês da peça aperte enter")
    # alteração do mês
    while True:
        try:
            mes = input()
            if (len(mes) == 2 and int(mes) <= 12 and int(mes) > 0) or mes == "":
                break
            else:
                print("\nponha um número maior que zero de 2 digitos")
        except ValueError:
            print("\nPonha um número") 

    print("\nInsira o dia da peça:")
    # alteração do dia considerando se o mês é de 30 dias, 31 dias ou se o ano é bissexto
    while True:
        try:
            dia = input()
            if len(dia) == 2 and int(dia) >= 1:
                if mes != "": # Se o mês foi alterado
                    if mes in mes_com30: 
                        if int(dia) <= 30:
                            break
                        else:
                            print("\nO mês selecionado só vai até 30")
                    if mes in mes_com31: 
                        if int(dia) <=31:
                            break
                        else:
                            print("\nO mês selecionado só vai até 31")
                    if mes == "02": 
                        if ano != "": # Se o ano foi alterado
                            if int(ano)%4 == 0:
                                if int(dia) <= 29:
                                    break 
                                else:
                                    print(f"\nNo ano {ano}, o mês de fevereiro só vai até 29") 
                            else:
                                if int(dia) <= 28:
                                    break 
                                else:
                                    print(f"\nNo ano {ano}, o mês de fevereiro só vai até 28")
                        else: # Se o ano não foi alterado
                            if int(ano_sem_alterar)%4 == 0:
                                if int(dia) <= 29:
                                    break 
                                else:
                                    print(f"\nNo ano {ano}, o mês de fevereiro só vai até 29") 
                            else:
                                if int(dia) <= 28:
                                    break 
                                else:
                                    print(f"\nNo ano {ano}, o mês de fevereiro só vai até 28")
                else: # Se o mês não foi alterado 
                    if mes_sem_alterar in mes_com30: 
                        if int(dia) <= 30:
                            break
                        else:
                            print("\nO mês selecionado só vai até 30")
                    if mes_sem_alterar in mes_com31: 
                        if int(dia) <=31:
                            break
                        else:
                            print("\nO mês selecionado só vai até 31")
                    if mes_sem_alterar == "02": 
                        if ano != "": # Se o ano foi alterado 
                            if int(ano)%4 == 0:
                                if int(dia) <= 29:
                                    break 
                                else:
                                    print("\nNo ano selecionado, o mês de fevereiro só vai até 29") 
                            else:
                                if int(dia) <= 28:
                                    break 
                                else:
                                    print("\nNo ano selecionado, o mês de fevereiro só vai até 28")
                        else: # Se o ano não foi alterado
                            if int(ano_sem_alterar)%4 == 0:
                                if int(dia) <= 29:
                                    break 
                                else:
                                    print("\nNo ano selecionado, o mês de fevereiro só vai até 29") 
                            else:
                                if int(dia) <= 28:
                                    break 
                                else:
                                    print("\nNo ano selecionado, o mês de fevereiro só vai até 28")

            elif dia == "": # Se o dia não foi alterado
                break

            else:
                print("\nPonha um número de 2 dígitos, maior que zero") 
        except ValueError:
            print("\nPonha um número")  

    if dia == "" and mes == "" and ano == "": # Se nenhuma data foi alterada
        data_nova = ""
    elif dia != "" and mes == "" and ano == "": # Se apenas o dia foi alterado
        data = ano_sem_alterar + "-" + mes_sem_alterar + "-" + dia
        data_nova = datetime.fromisoformat(data).date() 
    elif dia == "" and mes != "" and ano == "": # Se apenas mês o foi alterado
        data = ano_sem_alterar + "-" + mes + "-" + dia_sem_alterar
        data_nova = datetime.fromisoformat(data).date()
    elif dia == "" and mes == "" and ano != "": # Se apenas o ano for alterado
        data = ano + "-" + mes_sem_alterar + "-" + dia_sem_alterar
        data_nova = datetime.fromisoformat(data).date()
    elif dia != "" and mes != "" and ano == "": # Se o dia for alterado e o mês também
        data = ano_sem_alterar + "-" + mes + "-" + dia
        data_nova = datetime.fromisoformat(data).date()
    elif dia != "" and mes == "" and ano != "": # Se o dia for alterado e o ano for alterado
        data = ano + "-" + mes_sem_alterar + "-" + dia
        data_nova = datetime.fromisoformat(data).date()
    elif dia == "" and mes != "" and ano != "": # Se o mês for alterado e o ano for alterado
        data = ano + "-" + mes + "-" + dia_sem_alterar
        data_nova = datetime.fromisoformat(data).date()
    else: # Se o dia, o mês e o ano forem alterados.
        data = ano + "-" + mes + "-" + dia
        data_nova = datetime.fromisoformat(data).date()

    # Alteração da situação da peça
    print("\nPonha a situação da peça alterada: 'venda', 'doação' ou 'ficar'")
    print("Caso não deseje alterar a situação aperte enter.") 
    while True:
        try:
            situacao_peca = input()
            situacao_peca_tratado = situacao_peca.lower()
            if situacao_peca_tratado in lista_situacao:
                break
            else:
                print("\nPonha a situação: 'venda', 'doação' ou 'ficar'")   
        except ValueError: 
            print("\nPonha apenas letras") 

    preco_peca_novo = 0.0 #Se a peça não for para venda o preço da peça será 0 
    # Se a situação da peça alterada for para venda, perguntar o preço da peça
    if situacao_peca_tratado == "venda":
        print("\nPonha o preço da peça:")
        print("Caso não deseje alterar o preço digite -1.")
        while True:
            try:
                preco_peca_novo = float(input()) 
                if preco_peca_novo >= 0:
                    break
                elif preco_peca_novo == -1:
                    break
                else:
                    print("\nPonha um valor maior que ou igual a zero:")
            except ValueError:
                print("\nPonha um número real para representar o preço:")
    # Se o usuário não desejar mudar o preço, envia para a função de modo que não altere o preço
    if preco_peca_novo == -1:
        preco_peca_novo == ""

    alterar_peca(id_peca,tipo= tipo_peca_tratado,tamanho= tamanho_peca_tratado, padrao= padrao_peca_tratado,cor=cor_peca_tratado,data=data_nova )
    return

# Remover peça - Israel
def comando3():
    # Pede ao usuario o id da peça que deseja remover e chama a função remover_peca
    print("Digite o id da peça que deseja remover:")
    while True:
        try:
            id_para_remover = int(input())
            if id_para_remover > 0:
                break
            else:
                print("Ponha um id válido")
        except ValueError:
            print("Ponha um número") 
    remover_peca(id_para_remover) 
    return   


# Cadastrar estilo - Edson
def comando4():
    # Cria um estilo novo com o nome dado pelo usuário e informa possíveis erros no processo.
    try:
        nome_estilo = input("\nDigite o nome do estilo: ")
        criar_estilo(nome_estilo)
    except Exception as e:
        print(f"\nAviso: {e}")
        return

    # Checa se o usuário deseja inserir peças ao estilo recém criado.
    inserir = False
    while True:
        resposta = input("\nDeseja inserir peças ao estilo? [s/n] ")
        resposta = resposta.lower()

        if resposta == "s" or resposta == "sim":
            inserir = True
            break
        elif resposta == "n" or resposta == "nao" or resposta == "não":
            inserir = False
            break
        else:
            print('\nResposta inválida! Digite "s" para sim ou "n" para não.')

    while inserir:
        # Mostra ao usuário as peças existentes no guarda-roupa
        listar_pecas()
        # Insere uma peça escolhida pelo usuário no estilo e trata possíveis entradas inválidas.
        try:
            id_peca = int(input("\nDigite o id da peça que deseja inserir no estilo: "))
            adicionar_peca_a_estilo(id_peca, nome_estilo)
            print("\nPeça adicionada com sucesso!")
        # Informa o caso do ID passado não ser inteiro.
        except ValueError:
            print("\nValor de ID inválido. Tente novamente!")
            continue
        # Informa os casos de erro gerais, como o ID inexistente.
        except Exception as e:
            print("\n%s" %e)

        # Checa se o usuário deseja inserir mais uma peça ao estilo.
        while True:
            resposta = input("\nDeseja inserir outra peça ao estilo? [s/n] ")
            resposta = resposta.lower()

            if resposta == "s" or resposta == "sim":
                break
            elif resposta == "n" or resposta == "nao" or resposta == "não":
                inserir = False
                break
            else:
                print('\nResposta inválida! Digite "s" para sim ou "n" para não.')

    print(f"\nEstilo {nome_estilo} criado com sucesso!")


# Alterar estilo - Edson
def comando5():
    alterar_estilo()


# Remover estilo - Edson
def comando6():
    nome_estilo = input("\nDigite o nome do estilo: ")

    # Remove o estilo entrado pelo usuário se existir no dicionário de estilos.
    if nome_estilo in estilos.keys():
        remover_estilo(nome_estilo)
        print('\nEstilo "%s" foi removido do sistema!' %nome_estilo)
    else:
        print('\nEstilo "%s" não está cadastrado!' %nome_estilo)


# Listar todas as peças - Bruno
def comando7():
    listar_pecas()


# Listar peças por tamanho e padrão - Bruno
def comando8():

    # Ordenando os comandos para chamá-los com o input do usuário
    padrao = ["", PADRAO_FEMININO, PADRAO_MASCULINO, PADRAO_UNISSEX]
    tamanho = ["", TAMANHO_P, TAMANHO_M, TAMANHO_G]

    while True:
        print("Para filtar por tamanho digite: ")
        print("1 -> Tamanho P")
        print("2 -> Tamanho M")
        print("3 -> Tamanho G")
        print("0 -> Não filtrar por tamanho")

        try:
            resposta_tamanho = int(input("\nSeu comando: "))
        except:
            # Usuário digitou algo que não pode ser convertido pra int
            print("\nAtenção: Insira apenas 0,1,2 ou 3.")
            continue
        
        # Usuário digitou um número válido
        if resposta_tamanho in [0,1,2,3]:
            break

        # Usuário digitou um número fora do intervalo
        print("\nAtenção: Insira apenas 0,1,2 ou 3.")
    
    while True:
        print("Para filtrar por padrão digite: ")
        print("1 -> Padrão Feminino")
        print("2 -> Padrão Masculino")
        print("3 -> Padrão Unissex")
        print("0 -> Não filtrar por padrão")

        try:
            resposta_padrao = int(input("\nSeu comando: "))
        except:
            # Usuário digitou algo que não pode ser convertido pra ints
            print("\nAtenção: Insira apenas 0,1,2 ou 3.")
            continue
        
        # Usuário digitou um número válido
        if resposta_padrao in [0,1,2,3]:
            break

        # Usuário digitou um número fora do intervalo
        print("\nAtenção: Insira apenas 0,1,2 ou 3.")
    
    # Com as respostas, chama listar_pecas_tamanho_padrao para expor o resultado ao usuário
    try:
        listar_pecas_tamanho_padrao(tamanho[resposta_tamanho], padrao[resposta_padrao])

    # Se algo der errado, printa a mensagem de erro
    except Exception as e:
        print(f"\n{e}")


# Listar estilos - Bruno
def comando9():
    listar_estilos()
    return


# Pesquisar estilo por nome - Israel
def comando10():
    selecionar_estilo()
    return


# Listar peças para venda - Israel
def comando11():
    listar_pecas_para_venda()
    return


# Listar peças para doação - Israel
def comando12():
    listar_pecas_para_doacao()
    return


# Vender peça - Edson
def comando13():
    # Vende a peça passada pelo usuário e trata possíveis erros no processo.
    try:
        id_peca = int(input("\nDigite o id da peça: "))
        vender_para = input("Digite o nome do comprador da peça: ")
        vender_peca(id_peca, vender_para)
        print("\nPeça vendida com sucesso!")

        # Informações alteradas apenas se a venda deu certo
        informacao["alteradas"] = True
    # Informa o caso do ID passado não ser inteiro.
    except ValueError:
        print("\nValor de ID inválido. Tente novamente!")
    # Informa os casos de erro gerais, como o ID inexistente.
    except Exception as e:
        print("\n%s" %e)


# Doar peça - Edson
def comando14():
    # Doa a peça passada pelo usuário e trata possíveis erros no processo.
    try:
        id_peca = int(input("\nDigite o id da peça: "))
        doar_para = input("Digite o nome do comprador da peça: ")
        doar_peca(id_peca, doar_para)
        print("\nPeça doada com sucesso!")

        # Informações alteradas apenas se a doação deu certo
        informacao["alteradas"] = True
    # Informa o caso do ID passado não ser inteiro.
    except ValueError:
        print("\nValor de ID inválido. Tente novamente!")
    # Informa os casos de erro gerais, como o ID inexistente.
    except Exception as e:
        print("\n%s" %e)


# Listar peças vendidas - Edson
def comando15():
    listar_pecas_vendidas()


# Listar peças doadas - Bruno
def comando16():
    listar_pecas_doadas()
    return


# Salvar alterações - Edson
def comando17():
    try:
        salvar_alteracoes()
        print("Alterações salvas com sucesso!")
    except Exception as e:
        print("\nErro ao salvar alterações:", e)


# Carregar arquivos - Israel
def comando18():
    try:
        carregar_arquivos()
        print("Arquivos carregados com sucesso!")
    except Exception as e:
        print("\nErro ao carregar arquivos:", e)


# Finalizar programa - Bruno
def comando0():
    if informacao["alteradas"]:
        print("\nALERTA: Você não salvou suas alterações")

        while True:
            resposta = input("Deseja salvar suas alterações ao sair? [S/N] ")

            if resposta.lower() == "s" or resposta.lower() == "sim":
                comando17() # Salvar alterações
                print("\nInformações salvas")
                return
            elif resposta.lower() == "n" or resposta.lower() == "não" or resposta.lower() == "nao":
                print("\nSaindo sem salvar...")
                return
            else:
                print("\nDigite apenas sim ou não")

        
    


def menu_comandos():
    # Guarda comandos em string para particioná-la e iterar sobre os comandos
    comandos = "Cadastrar uma peça|Alterar uma peça|Remover uma peça|Cadastrar um estilo|Alterar um estilo|Remover um estilo|Listar todas as peças|Listar peças por tamanho e padrão|Listar estilos|Pesquisar estilo por nome|Listar peças para venda|Listar peças para doação|Vender uma peça|Doar uma peça|Listar peças vendidas|Listar peças doadas|Salvar alterações|Carregar arquivos|Finalizar programa"
    comandos = comandos.split('|') # Transforma a string em uma lista de strings

    # Número de linhas de comandos printadas
    linhas_comandos = len(comandos)//3

    print("\nDigite: ")
    for i in range(linhas_comandos):

        # Se primeira linha, printar 4 colunas de comandos
        if i == 0:
            print(f"{i+1:2d} --> {comandos[i]:19s} | {linhas_comandos+i+1:2d} --> {comandos[linhas_comandos+i]:33s} | {(linhas_comandos*2)+i+1:2d} --> {comandos[(linhas_comandos*2)+i]:24s} | {0} --> {comandos[(linhas_comandos*3)+i]}")
            continue

        # Printar 3 colunas de comandos
        print(f"{i+1:2d} --> {comandos[i]:19s} | {linhas_comandos+i+1:2d} --> {comandos[linhas_comandos+i]:33s} | {(linhas_comandos*2)+i+1:2d} --> {comandos[(linhas_comandos*2)+i]:24s} |")
    

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
            informacao["alteradas"] = True
        elif comando == 2:
            comando2()
            informacao["alteradas"] = True
        elif comando == 3:
            comando3()
            informacao["alteradas"] = True
        elif comando == 4:
            comando4()
            informacao["alteradas"] = True
        elif comando == 5:
            comando5()
            informacao["alteradas"] = True
        elif comando == 6:
            comando6()
            informacao["alteradas"] = True
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
            informacao["alteradas"] = False # False porque não existe mais alterações não salvas
        elif comando == 18:
            comando18()
        elif comando == 0:
            comando0()
            print("\nGuarda-Roupa Virtual encerrado")
            return
        else:
            print("ATENÇÃO: Digite apenas um número do menu")
        
        input("\nDigite qualquer coisa para continuar: ")

    
def main():
    carregar_arquivos()
    # inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_DOACAO, 0.0)
    # inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_DOACAO, 0.0)
    # inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    # inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_DOACAO, 0.0)
    # inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_DOACAO, 0.0)
    # inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    
    interface_usuario()

if __name__ == "__main__":
    main()