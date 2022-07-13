from datetime import *
from models import *
from utils import *
import os

# -------------------- CREATE -------------------- #


# Cria um dicionário peça e o retorna
def criar_peca(id, tipo, tamanho, padrao, cor, data, situacao, preco):
    peca = {
        "id": id, "tipo": tipo, "tamanho": tamanho,
        "padrão": padrao, "cor": cor, "data": data, 
        "situação": situacao, "preço": preco, "estilos": []
    }

    return peca


# Responsável por REGISTRAR uma peça no guarda-roupa
def inserir_peca(tipo, tamanho, padrao, cor, data:date, situacao, preco, id= ""):

    # Se o id não for informado, crie o id
    if id == "":
        # Se a lista de peças estiver vazia, o id da nova peça será 1
        if len(ids_cadastrados) == 0:
            peca_id = 1
        else:
            # Pega o último id cadastrado e adiciona 1 para cadastrar a nova peça com id único
            last_index = len(ids_cadastrados) - 1
            ultimo_id = ids_cadastrados[last_index]
            peca_id = ultimo_id + 1
    # Se o id for informado, crie a peça com o id informado 
    else:
        peca_id = id

    peca = criar_peca(peca_id, tipo, tamanho, padrao, cor, data, situacao, preco) # retorna uma peça
    pecas.append(peca) # Registra a peça em pecas

    # Se id não estiver em ids_cadastrados, adicione-o
    if peca_id not in ids_cadastrados:
        ids_cadastrados.append(peca_id) # Cadastra o novo id na lista global


# Cria um estilo se não existir
def criar_estilo(nome_estilo, contador=0):
    if nome_estilo in estilos:
        raise Exception(f"O estilo {nome_estilo} já existe!")

    estilos[nome_estilo] = {
        "contador": contador,
        "peças": [
            [], # Peças tipo Superior
            [], # Peças tipo Inferior
            []  # Peças tipo calçado
        ]
    }


# -------------------- UPDATE -------------------- #


def adicionar_peca_a_estilo(id_peca: int, nome_estilo: str):
    peca = retorna_peca_por_id(id_peca)
    peca_index = indice_peca_em_estilos(peca)
    
    # Se estilo não existe, crie um
    if nome_estilo not in estilos:
        criar_estilo(nome_estilo)
    
    # Verifica se a peça já foi adicionada ao estilo
    if peca not in estilos[nome_estilo]["peças"][peca_index]:
        # Adiciona a peça ao estilo especificado na matriz de peças de acordo com o seu tipo
        estilos[nome_estilo]["peças"][peca_index].append(peca)
        
        # Adiciona o estilo à peça
        peca["estilos"].append(nome_estilo)

        print(f"\nPeça de id {id_peca} adicionada ao estilo {nome_estilo}!")
    else:
        print(f"Não foi possível adicionar peça de id {id_peca} ao estilo {nome_estilo}, pois a peça já pertence ao estilo.")


# Altera uma peça ao especificar o Id dela.
# Altera apenas os campos especificados e mantém os não especificados.
def alterar_peca(id, tipo="", tamanho="", padrao="", cor="", data="", situacao="", preco=""):
    peca = retorna_peca_por_id(id) # Retorna um erro se não existir

    # se algum campo não for especificado, usar a informação já encontrada na peça.
    if tipo == "":
        tipo = peca["tipo"]
    if tamanho == "":
        tamanho = peca["tamanho"]
    if padrao == "":
        padrao = peca["padrão"]
    if cor == "":
        cor = peca["cor"]
    if data == "":
        data = peca["data"]
    if situacao == "":
        situacao = peca["situação"]
    if preco == "":
        preco = peca["preço"]
    
    # Pega o índice da peça na lista pecas para poder alterá-la.
    index_peca = pecas.index(peca) # Sempre funciona, pois a peça passada sempre existirá em pecas.
    pecas[index_peca] = {
        "id": id,
        "tipo": tipo,
        "tamanho": tamanho,
        "padrão": padrao,
        "cor": cor,
        "data": data,
        "situação": situacao,
        "preço": preco
    }
    print(f"Peça de id {id} alterada com sucesso!")


def alterar_estilo():
    # Checa se existem estilos cadastrados
    if len(estilos) == 0:
        print("\nVocê ainda não cadastrou nenhum estilo!")
        return

    lista_nomes = list(estilos.keys()) # Lista de nomes de estilos
    nome_estilo = "" # Nome do estilo que será alterado

    while True:
        print("\nEstilos: ")
        # Enumera os estilos cadastrados e recebe a escolha do usuário
        for i in range(len(lista_nomes)):
            print("%d - %s" %((i+1), lista_nomes[i]))
        
        selecao = input("\nSelecione um estilo para alterar: ")

        # Recebe e trata o input do usuário aceitando o nome do estilo ou o número equivalente.
        try:
            selecao = int(selecao)
            selecao -= 1

            if selecao >= 0 and selecao < len(lista_nomes):
                nome_estilo = lista_nomes[selecao]
                break
            else:
                print("\nEntrada inválida")
                return
        
        # Se o input for uma string, verifica se está se é uma chave do dict estilos
        except ValueError as e:
            if selecao in lista_nomes:
                nome_estilo = selecao
            else:
                print("\nEstilo não cadastrado")
                return
        
        # Se algo der errado, printar entrada inválida
        except Exception as e:
            print("\nEntrada inválida, tente novamente.")
            continue

    # Checa se o usuário deseja remover alguma peça do estilo
    remover_peca = False
    alterou = False # Saber se o estilo foi alterado

    while True:
        resposta = input("\nDeseja remover peças do estilo %s? [s/n] " %nome_estilo)
        resposta = resposta.lower()

        if resposta == "s" or resposta == "sim":
            remover_peca = True
            break
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            remover_peca = False
            break
        else:
            print('\nResposta inválida! Digite "s" para sim ou "n" para não.')

    while remover_peca:
        # Lista as peças que estão no estilo
        pecas_estilo = []
        for tipo in estilos[nome_estilo]["peças"]:
            for peca in tipo:
                pecas_estilo.append(peca)
        
        # Testa se tem peças no estilo
        if len(pecas_estilo) == 0:
            print(f"Não existem peças no estilo {nome_estilo}")
            return

        print_pecas_filtradas(pecas_estilo)
    
        # Remove uma peça escolhida pelo usuário e trata possíveis entradas inválidas.
        try:
            id_peca = int(input("\nDigite o id da peça que deseja remover do estilo: "))
            remover_peca_do_estilo(id_peca, nome_estilo)
            print("\nPeça removida com sucesso!")
            alterou = True

        # Informa o caso do ID passado não ser inteiro.
        except ValueError:
            print("\nValor de ID inválido. Tente novamente!")
            continue
        # Informa os casos de erro gerais, como o ID inexistente.
        except Exception as e:
            print(f'\nErro ao remover peça do estilo: {e}. Tente novamente!')
            continue

        # Checa se o usuário deseja remover mais uma peça do estilo.
        while True:
            resposta = input("\nDeseja remover outra peça do estilo? [s/n] ")
            resposta = resposta.lower()

            if resposta == "s" or resposta == "sim":
                break
            elif resposta == "n" or resposta == "nao" or resposta == "não":
                remover_peca = False
                break
            else:
                print('\nResposta inválida! Digite "s" para sim ou "n" para não.')

    # Checa se o usuário deseja mudar o nome do estilo
    mudar_nome = False
    while True:
        resposta = input("\nDeseja mudar o nome do estilo %s? [s/n] " %nome_estilo)
        resposta = resposta.lower()

        if resposta == "s" or resposta == "sim":
            mudar_nome = True
            break
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            mudar_nome = False
            break
        else:
            print('\nResposta inválida! Digite "s" para sim ou "n" para não.')
 
    # Faz a mudança do nome do estilo
    if mudar_nome:
        novo_nome = ""

        while True:
            novo_nome = input("\nDigite o novo nome do estilo: ")

            # Trata o caso de já existir um estilo com o novo nome
            if novo_nome in lista_nomes:
                print("\nJá existe um estilo com esse nome. Tente novamente!")
                continue
            else:
                break
    
        # Cria uma nova chave no dicionário identica à já existente, mas com o nome novo, e remove a já existente.
        estilos[novo_nome] = estilos.pop(nome_estilo)
        alterou = True

        # Procura as peças que estão no estilo mudado, retira o nome antigo e coloca o novo.
        for peca in pecas:
            if nome_estilo in peca["estilos"]:
                peca["estilos"].remove(nome_estilo)
                peca["estilos"].append(novo_nome)

    while True:
        resposta = input("\nDeseja adicionar uma peça ao estilo %s? [s/n] " %nome_estilo)
        resposta = resposta.lower()

        if resposta == "s" or resposta == "sim":
            adicionar_peca = True
            break
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            adicionar_peca = False
            break
        else:
            print('\nResposta inválida! Digite "s" para sim ou "n" para não.')
    
    while adicionar_peca:
        try:
            listar_pecas()
            id = int(input("\ndigite o id da peça que deseja adicionar: "))
        except:
            print("\nId inválido.")
            break

        try:
            adicionar_peca_a_estilo(id, nome_estilo)
            alterou = True
        except Exception as e:
            print(e)
        
        resposta = input("\nDeseja adicionar outra peça ao estilo %s? [s/n] " %nome_estilo)
        resposta = resposta.lower()

        if resposta == "s" or resposta == "sim":
            adicionar_peca = True
        elif resposta == "n" or resposta == "não" or resposta == "nao":
            break
        else:
            print('\nResposta inválida! Digite "s" para sim ou "n" para não.')

    if alterou:
        print("\nEstilo alterado com sucesso!")
            
    

# -------------------- DELETE -------------------- #


# Remove um estilo do dicionário estilos.
def remover_estilo(nome_estilo):

    # Procura as peças que estão no estilo removido, se alguma estiver, retira o estilo de dentro da peça
    for peca in pecas:
        if nome_estilo in peca["estilos"]:
            peca["estilos"].remove(nome_estilo)

    estilos.pop(nome_estilo)


# Remove a peça por id, se o id não existir, não será possível encontrar a peça e um erro será jogado.
# Remove a peça de TODOS os estilos que ela fizer parte.
# Exclui o estilo que a peça fazia parte se o estilo não tiver mais nenhuma peça.
def remover_peca(id):
    peca = retorna_peca_por_id(id)
    pecas.remove(peca) # Remove o dicionário peca da lista pecas.
    print(f"Atenção: Peça de id {id} foi removida do Guarda Roupa Virtual.")

    # Para saber em qual índice da matriz remover a peça de estilos.
    index_peca = indice_peca_em_estilos(peca)

    # Remove a peça de todos os estilos que ela estiver
    for nome_estilo in peca["estilos"]:
        estilos[nome_estilo]["peças"][index_peca].remove(peca)
        print(f"Atenção: Peça de id {id} foi removida do estilo {nome_estilo}.")


def remover_peca_do_estilo(id_peca, nome_estilo):
    peca = retorna_peca_por_id(id_peca)
    peca_index = indice_peca_em_estilos(peca)

    # Verifica se a peça pertence ao estilo
    if peca in estilos[nome_estilo]["peças"][peca_index]:
        # Remove a peça do estilo especificado na matriz de peças de acordo com o seu tipo
        for i in range(len(estilos[nome_estilo]["peças"][peca_index])):
            if peca == estilos[nome_estilo]["peças"][peca_index][i]:
                estilos[nome_estilo]["peças"][peca_index].pop(i)
                break
        
        # Remove o estilo da peça
        peca["estilos"].remove(nome_estilo)
    else:
        print(f"Não foi possível remover a peça de id {id_peca} do estilo {nome_estilo}, pois a peça não pertence ao estilo.")


# adiciona informações da peça doada ao historico_pecas_vendidas.
def registrar_peca_vendida(peca:dict, vender_para, data_venda=datetime.today().date()):
    # adiciona informações da peça doada ao historico_pecas_vendidas.
    historico_pecas_vendidas.append({
        "id": peca["id"],
        "tipo": peca["tipo"],
        "tamanho": peca["tamanho"],
        "padrão": peca["padrão"],
        "cor": peca["cor"],
        "data_venda": data_venda, # Data de hoje no formato YYYY-MM-DD.
        "data_guarda_roupa": peca["data"],
        "vendido_para": vender_para,
        "preço": peca["preço"]
    })


# vender_para = nome do comprador.
# vende_peca remove a peça do guarda roupa.
def vender_peca(id, vender_para):
    peca = retorna_peca_por_id(id)
    if peca["situação"] != SITUACAO_VENDA:
        raise Exception("Peça não disponível para venda. Tente alterar a situação da peça antes em 'Alterar peça'.")
    
    # adiciona informações da peça doada ao historico_pecas_vendidas.
    registrar_peca_vendida(peca, vender_para)

    # remove peça do guarda roupa (pecas).
    remover_peca(id)


def registrar_peca_doada(peca:dict, doar_para, data_doada=datetime.today().date()):

    # adiciona informações da peça doada ao historico_pecas_doadas.
    historico_pecas_doadas.append({
        "id": peca["id"],
        "tipo": peca["tipo"],
        "tamanho": peca["tamanho"],
        "padrão": peca["padrão"],
        "cor": peca["cor"],
        "data_doação": data_doada, # Data de hoje no formato YYYY-MM-DD.
        "data_guarda_roupa": peca["data"],
        "doado_para": doar_para
    })

# doar_para = nome da instituição ou pessoa que recebeu a doação.
# doar_peca remove a peça do guarda roupa.
def doar_peca(id, doar_para):
    peca = retorna_peca_por_id(id) # Impede a execução se o id não for encontrado.
    if peca["situação"] != SITUACAO_DOACAO:
        raise Exception("Peça não disponível para doação. Tente alterar a situação da peça antes em 'Alterar peça'.")
    
    # adiciona informações da peça doada ao historico_pecas_doadas.
    registrar_peca_doada(peca, doar_para)

    # remove peça do guarda roupa (pecas)
    remover_peca(id)


# -------------------- READ -------------------- #


# Printa todas as peças passadas em uma lista, em formato organizado e com cabeçalho.
def print_pecas_filtradas(pecas_filtradas:list):
    # Header
    print(" Id  |   Tipo   | Tamanho |  Padrão   |    Cor     |    Data     | Situação |   Preço")

    for peca in pecas_filtradas:
        print_peca(peca)


# Lista todas as peças.
def listar_pecas():
    if len(pecas) == 0:
        print("\nNenhuma peça foi cadastrada ainda.")
        return

    print("\nTodas as peças:")
    print_pecas_filtradas(pecas)


# Printa uma única peça.
def print_peca(peca:dict):
    print(f"{peca['id']:04d} | {peca['tipo']:8s} |    {peca['tamanho']}    | {peca['padrão']:9s} |   {peca['cor']:8s} | {peca['data']}  |   {peca['situação']:6s} |  {peca['preço']:7.2f}")


# Lista peças de mesmo tamanho.
def listar_pecas_tamanho(tamanho):
    pecas_filtradas = []

    for peca in pecas:
        if peca["tamanho"] == tamanho:
            pecas_filtradas.append(peca)

    if len(pecas_filtradas) == 0:
        raise Exception(f"Não foram encontradas peças de tamanho {tamanho}") 
    
    print(f"\nPeças de tamanho {tamanho}:")
    print_pecas_filtradas(pecas_filtradas)


# Lista peças de mesmo padrão
def listar_pecas_padrao(padrao):

    pecas_filtradas = []
    for peca in pecas:
        if peca["padrão"] == padrao:
            pecas_filtradas.append(peca)

    if len(pecas_filtradas) == 0:
        raise Exception(f"Não foram encontradas peças de padrão {padrao}") 
    
    print(f"\nPeças de padrão {padrao}:")
    print_pecas_filtradas(pecas_filtradas)


# Lista as peças de mesmo tamanho e padrão, também lista com apenas tamanho ou padrão especificados
def listar_pecas_tamanho_padrao(tamanho="", padrao=""):

    # Se tamanho ou padrão não estiverem no formato especificado, será jogado um erro
    if tamanho != TAMANHO_P and tamanho != TAMANHO_M and tamanho != TAMANHO_G and tamanho != "":
        raise Exception("Tamanho de peça inválido")
    if padrao != PADRAO_FEMININO and padrao != PADRAO_MASCULINO and padrao != PADRAO_UNISSEX and padrao != "":
        raise Exception("Padrão de peça inválido")

    # Lista todas as peças, pois não tem filtro
    if tamanho == "" and padrao == "":
        listar_pecas()

    # Peças serão listadas pelo padrão
    elif tamanho == "":
        listar_pecas_padrao(padrao)

    # Peças serão listadas pelo tamanho
    elif padrao == "":
        listar_pecas_tamanho(tamanho)

    # Peças serão listadas pelo tamanho e padrão
    else:
        pecas_filtradas = []

        for peca in pecas:
            if peca["tamanho"] == tamanho and peca["padrão"] == padrao:
                pecas_filtradas.append(peca)
        
        if len(pecas_filtradas) == 0:
            raise Exception(f"Não foram encontradas peças de tamanho {tamanho} e padrão {padrao}")
        
        # Lista as peças filtradas
        print(f"\nPeças filtradas por tamanho {tamanho} e padrão {padrao}:")
        print_pecas_filtradas(pecas_filtradas)


# Seleciona um estilo do guarda roupa para ser usado, e incrementa o seu contador em 1
def selecionar_estilo():
    nomes = list(estilos.keys()) # Retorna uma lista com todas as chaves do dicionário 'estilos'
    estilo = ""
    mudar = True # Inicia como True para entrar no loop

    # Caso no qual nenhum estilo foi cadastrado
    if len(nomes) == 0:
        print("Você ainda não cadastrou nenhum estilo!")
        return

    # Enquanto o usuário quiser mudar sua opção de estilo, executar o que se segue
    while mudar:
        print("\nQual estilo deseja usar?")

        # Enumera os estilos cadastrados e recebe a escolha do usuário
        for i in range(len(nomes)):
            print("%d - %s" %((i+1), nomes[i]))
        
        selecao = input("\nSelecione um estilo: ")

        # Recebe e trata o input do usuário aceitando o nome do estilo ou o número equivalente.
        try:
            selecao = int(selecao)
            selecao -= 1

            if selecao >= 0 and selecao < len(nomes):
                estilo = nomes[selecao]
            else:
               print("Entrada inválida, tente novamente.")
               continue
        
        # Se o input for uma string, verificar se está em nomes (se é uma chave do dict estilos)
        except ValueError as e:
            if selecao in nomes:
                estilo = selecao
            else:
                print("Estilo não cadastrado, tente novamente.")
                continue
        
        # Se algo der errado, printar entrada inválida
        except Exception as e:
            print("Entrada inválida, tente novamente.")
            continue

        print("\nVocê escolheu o estilo %s\n" %estilo)

        # Checa se o usuário quer mudar o estilo
        while True:
            resposta = input("Deseja confirmar escolha do estilo %s? [s/n] " %estilo)

            if resposta == "s" or resposta == "sim":
                mudar = False
                break
            elif resposta == "n" or resposta == "não":
                mudar = True
                break
            else:
                print('\nResposta inválida! Digite "s" para sim ou "n" para não.')
    
    # Incrementa 1 ao contador do estilo escolhido
    estilos[estilo]["contador"] += 1

    print("\nEssas são as opções de peças desse estilo:")

     # Lista as peças que estão no estilo escolhido e separadas por tipo
    for tipo in estilos[estilo]["peças"]:
        if len(tipo) > 0:
            print("\nPeças do tipo %s\n" %tipo[0]["tipo"])
            print_pecas_filtradas(tipo)


# Função para listar peças para venda
def listar_pecas_para_venda():
    lista_venda = []                                
    lista_venda_ordenada = [] 
    lista_precos = []

    # Estrutura de repetição para checar cada peça. Se a situação da peça for para venda, armazena essa peça em uma lista. 
    # Armazena, nessa mesma estrutura de repetição os preços de cada peça para venda em uma lista.  
    for i in range(len(pecas)): 
        if pecas[i]["situação"] == SITUACAO_VENDA:
            lista_venda.append(pecas[i]) 
            lista_precos.append(pecas[i]["preço"])

    # Ordenação, com o método de lista sorted, para organizar a lista de preços em ordem crescente  
    lista_precos_ordenada = sorted(lista_precos)

    # Estrutura de repetição para procurar a peça com os preços da lista organizada 
    for preco in lista_precos_ordenada:
        j = 0

        # While para procurar a peça, com estrutura condicional para não repetir a mesma peça 
        while j < len(lista_venda):
            if lista_venda[j]["preço"] == preco:

                # Se a peça não tivar na lista_venda_ordenada ela é adicionada nessa lista
                if lista_venda[j] not in lista_venda_ordenada: 
                    lista_venda_ordenada.append(lista_venda[j])
                    break 

            j += 1


    # Estrutura condicional: Se não houver nenhuma peça para venda, imprime uma mensagem, senão chama a função print_pecas_filtradas. 
    if len(lista_venda_ordenada) == 0:
        print("Não foram encontradas peças para venda")
        return 

    print("Listando peças para venda com ordem crecente de preços:")
    print_pecas_filtradas(lista_venda_ordenada)


# Função listar peças para doação 
def listar_pecas_para_doacao():
    lista_doacao = [] 
    lista_datas = []
    lista_doacao_ordenada = []

    # Estrutura de repetição para checar cada peça. Se a situação da peça for para doação, armazena essa peça em uma lista.
    # Armazena, a mesma estrutura de repetição as datas de cada peça para doação.
    for i in range(len(pecas)):
        if pecas[i]["situação"] == SITUACAO_DOACAO:
            lista_doacao.append(pecas[i])
            lista_datas.append(pecas[i]["data"]) 

    # Método sorted de listas para organizar as datas da mais recente para a mais antiga.
    lista_datas_ordenada = sorted(lista_datas,reverse = True)

    # Estrutura de repetição para procurar a peça com cada data da lista organizada de datas.  
    for datas in lista_datas_ordenada:
        j = 0 

        # While para procurar a peça, com estrutura condicional para não repetir a mesma peça. 
        while j < len(lista_doacao):
            if lista_doacao[j]["data"] == datas:

                # Se a peça não tivar na lista_doacao_ordenada ela é adicionada nessa lista.
                if lista_doacao[j] not in lista_doacao_ordenada: 
                    lista_doacao_ordenada.append(lista_doacao[j])
                    break 
            j += 1

    # Estrutura condicional: Se não houver nenhuma peça para venda, imprime uma mensagem, senão chama a função print_pecas_filtradas.
    if len(lista_doacao_ordenada) == 0:
        print('Não foram encontradas peças para doação')
        return 

    print('Listando peças para doação:')
    print_pecas_filtradas(lista_doacao_ordenada)

# Printa informações da peça juntamente com seu estilo
def print_peca_em_estilo(nome_estilo, peca):
    print(f"{nome_estilo:15s} | {peca['id']:04d} |  {peca['tipo']:8s}   |    {peca['tamanho']}    |  {peca['padrão']:9s}  |  {peca['cor']:8s} | {peca['data']} |   {peca['situação']:6s} | {peca['preço']:7.2f}")


# Função para listar as peças organizadas por estilo
def print_lista_estilos(lista_estilos):
    estilos_sem_pecas = []

    for nome_estilo in lista_estilos:
        # Se o estilo não possuir peça alguma, salve em estilos_sem_pecas
        if conta_numero_de_pecas_em_estilo(nome_estilo) == 0:
            estilos_sem_pecas.append(nome_estilo)

    # Se forem diferentes, existe pelo menos 1 estilo com peças dentro e devemos printá-las
    if len(lista_estilos) != len(estilos_sem_pecas):

        # Header
        print(f"\n{'Estilos':^16}|  Id  |     Tipo    | Tamanho |    Padrão   |    Cor    |    Data    | Situação |   Preço")

        #Estrutura de repetição para percorrer cada elemento da lista de estilos organizada
        for nome_estilo in lista_estilos:

            #  Estrutura de repetição para percorrer cada linha da matriz peças
            for j in range(len(estilos[nome_estilo]["peças"])):
                if len(estilos[nome_estilo]["peças"][j]) != 0:
                    for i in range(len(estilos[nome_estilo]["peças"][j])):
                        peca = estilos[nome_estilo]["peças"][j][i]

                        # Printa informações de cada peça em um dado estilo
                        print_peca_em_estilo(nome_estilo, peca)

    # Printa os estilos sem peças
    if len(estilos_sem_pecas) != 0:
        print("\nEstilos sem peças: ", end="")
        for estilo in estilos_sem_pecas:
            print(estilo, end=" ")    


# Função para listar as peças por estilo.
def listar_estilos():
    lista_estilos_disponiveis = list(estilos.keys())

    if len(lista_estilos_disponiveis) == 0:
        print("\nNenhum estilo foi cadastrado ainda :/ ")
        return

    lista_contadores = []
    lista_estilos_organizada = [] 

    # Estrutura de repetição para pegar cada estilo disponível e adicionar em uma lista os contadores de cada estilo
    for nome in lista_estilos_disponiveis: 
        lista_contadores.append(estilos[nome]["contador"])

    # Com o método de lista, organiza os contadores em ordem crescente
    lista_contadores_crescente = sorted(lista_contadores) 

    # Estrutura de repetição para pôr em uma lista organizada cada estilo de acordo com a ordem crescente do contador
    for j in lista_contadores_crescente:
        for nome in lista_estilos_disponiveis:
            if estilos[nome]["contador"] == j:

                # Se um estilo não estiver ainda na lista organizada ele é posto nela 
                if estilos[nome] not in lista_estilos_organizada:
                    lista_estilos_organizada.append(nome) 

    lista_estilos_sem_rep = []
    
    for estilo in (lista_estilos_organizada):
        if estilo not in lista_estilos_sem_rep:
            lista_estilos_sem_rep.append(estilo)

    print_lista_estilos(lista_estilos_sem_rep)


# Lista todas as peças doadas
def listar_pecas_doadas():
    if len(historico_pecas_doadas) == 0:
        print("\nPeças doadas:\nNenhuma peça foi doada até o momento :/")
        return
    
    # Header da tabela de peças doadas (notação ^ do format permite centralizar o conteúdo em determinado espaço)
    print("\nPeças doadas:")
    print(f"{'Instituição/Pessoa':^35} {'Tipo':^10} {'Tamanho':^10} {'Padrão':^6} {'Cor':^13}  {'Data Doação'}  {'Data Cadastro'}")
    
    for peca in historico_pecas_doadas:
        print(f"{peca['doado_para']:35s}  {peca['tipo']:10s}  {peca['tamanho']:^6}  {peca['padrão']:10s}  {peca['cor']:8s}   {peca['data_doação']}     {peca['data_guarda_roupa']}")


def listar_pecas_vendidas():

    # Sem vendas
    if len(historico_pecas_vendidas) == 0:
        print("\nNenhuma peça foi vendida até o momento >:(")
        return

    print("\nPeças vendidas:")
    print(f"{'Comprador':^35} {'Tipo':^10} {'Tamanho':^10} {'Padrão':^6} {'Cor':^13} {'Preço':^7} {'Data de Venda'}  {'Data de Cadastro'}")
    
    # Printa informações de cada venda
    for peca in historico_pecas_vendidas:
        print(f"{peca['vendido_para']:35s}  {peca['tipo']:10s}  {peca['tamanho']:^6}  {peca['padrão']:10s}  {peca['cor']:8s} {peca['preço']:7.2f}   {peca['data_venda']}      {peca['data_guarda_roupa']}")



# -------------------- ARQUIVOS -------------------- #

# Salva todas as alterações feitas.
def salvar_alteracoes():
    salvar_ids()
    salvar_pecas()
    salvar_estilos()
    salvar_historico_pecas_vendidas()
    salvar_historico_pecas_doadas()

# Salva todas as alterações feitas.
def carregar_arquivos():
    carregar_ids()
    carregar_pecas()
    carregar_estilos()
    carregar_historico_pecas_vendidas()
    carregar_historico_pecas_doadas()

# Salva as peças em um arquivo.txt separado por vírgula
# Guarda o id, tipo, tamanho, padrão, cor, data, situação, preço e estilos da peça 
def salvar_pecas():
    with open(".pecas.txt","w") as file:

        # Header do arquivo
        file.write("id,tipo,tamanho,padrão,cor,data,situação,preço,[estilos]\n")

        # Estrutura de repetição para pegar cada peça da lista pecas
        for peca in pecas:
            linha = ""

            # Pega cada chave do dicionario e adiciona seus valores no acumulador linha
            for variavel in peca:
                linha += f"{peca[variavel]}" + ","

            # Retira a última virgula 
            linha = linha.strip(",") 

            file.write(linha + "\n")
            
def carregar_pecas():
    try:
        with open(".pecas.txt","r") as file:

        # Lê o arquivo e retorna uma lista com todas as linhas de dados
            linhas = file.read().split("\n")[1:] # [1:] para descartar a primeira linha (Header)
            linhas.pop() # Eliminar linha vazia no final

            for linha in linhas:

                valores = linha.split(",")
                
                # Guarda os valores da venda em variáveis explícitas
                id_peca = int(valores[0])
                tipo = valores[1]
                tamanho = valores[2]
                padrao = valores[3]
                cor = valores[4]
                data = datetime.fromisoformat(valores[5]).date() # Transforma Str em um objeto datetime
                situacao = valores[6]
                preco = float(valores[7])

                inserir_peca(tipo,tamanho,padrao,cor,data,situacao,preco,id = id_peca)

    except IOError:
        # Se não existir o arquivo, não faz nada
        return

# Salva todos os estilos em arquivo estilos.txt separando cada valor por vírgula
# Guarda nome do estilo, contador e todos os ids de peças, sem diferenciar por tipo
def salvar_estilos():
    with open(".estilos.txt", "w") as file: # Fecha o arquivo ao sair da identação

        # Header do arquivo
        file.write("estilos,contador,[id_peças]\n")

        for estilo in estilos:
            linha = ""

            linha += f"{estilo},"
            linha += f"{estilos[estilo]['contador']},"
            
            # Acessa a matriz de peças no estilo
            for i in range(len(estilos[estilo]["peças"])):
                for j in range(len(estilos[estilo]["peças"][i])):

                    # Pega o id de cada peça da matriz peças
                    peca_id = estilos[estilo]["peças"][i][j]["id"]

                    linha += f"{peca_id},"

            # Remove a última vírgula à direita.
            linha = linha.strip(",")

            # Escreve a linha no arquivo, saltando a linha.
            file.write(linha + "\n")


# Lê o arquivo estilos.txt e carrega seus dados no dicionário estilos (variável global)
# Carregar_estilos deve ser chamado após carregar_pecas
# Se arquivo oculto existir, carrega-o
def carregar_estilos():
    try:
        with open(".estilos.txt", "r") as file:

            linhas = file.read().split("\n") # Cria lista ao separar a string por "enters"
            linhas.pop() # Remove linha vazia

            # Itera sobre cada linha do arquivo
            for linha in linhas[1:]: # Não pega o Header
                valores = linha.split(",") # Lista de valores

                estilo = valores[0]
                contador = int(valores[1])

                # Cria o estilo no dicionário estilos com seu contador
                criar_estilo(estilo, contador)

                # Itera sobre o restante dos valores (ids de peças contidas no estilo)
                for peca_id in valores[2:]:
                    
                    # id está como string, precisa ser convertido
                    peca_id = int(peca_id)

                    # Adiciona as peças ao estilo
                    # IMPORTANTE: as peças devem estar carregadas em pecas
                    adicionar_peca_a_estilo(peca_id, estilo)

    # Se arquivo não existir, não faz nada
    except IOError:
        return
            

# Salva o histórico de pecas em um arquivo oculto
def salvar_historico_pecas_vendidas():

    # Abre o arquivo e fecha automaticamente
    with open(".historico_vendas.txt", "w") as file:

        # Header
        file.write("id,tipo,tamanho,padrão,cor,data_doação,data_guarda_roupa,vendido_para,preço\n")

        # Salva cada venda ao arquivo
        for venda in historico_pecas_vendidas:
            linha = ""

            # itera sobre as chaves do dicionário de venda para adicionar os valores de cada atributo da venda
            for atributo in venda:
                linha += f"{venda[atributo]},"
            
            linha = linha.strip(",") # Remove a última vírgula da linha

            file.write(linha + "\n") # Escreve os dados no arquivo e salta uma linha


# Carrega o histórico de peças de arquivo oculto existir
def carregar_historico_pecas_vendidas():

    try:
        with open(".historico_vendas.txt", "r") as file:

            # Lê o arquivo e retorna uma lista com todas as linhas de dados
            linhas = file.read().split("\n")[1:] # [1:] para descartar a primeira linha (Header)
            linhas.pop() # Eliminar linha vazia no final

            for linha in linhas:

                valores = linha.split(",")
                
                # Guarda os valores da venda em variáveis explícitas
                id = int(valores[0])
                tipo = valores[1]
                tamanho = valores[2]
                padrao = valores[3]
                cor = valores[4]
                data_venda = datetime.fromisoformat(valores[5]).date() # Transforma Str em um objeto datetime
                data_guarda_roupa = datetime.fromisoformat(valores[6]).date()
                vendido_para = valores[7]
                preco = float(valores[8])

                # Cria peça para poder registrar a venda (mas não adiciona a peça ao guarda-roupa)
                peca = criar_peca(id, tipo, tamanho, padrao, cor, data_guarda_roupa, SITUACAO_VENDA, preco)

                registrar_peca_vendida(peca, vendido_para, data_venda)

    # Se não existir o arquivo, não faz nada
    except IOError:
        return


# Salva os ids em arquivo oculto
def salvar_ids():
    with open(".ids.txt", "w") as file:
        for id in ids_cadastrados:
            file.write(f"{id}\n")


# Carrega os ids se arquivo oculto existir
def carregar_ids():
    try:
        with open(".ids.txt", "r") as file:
            ids = file.read().split("\n")
            ids.pop()

            # 
            for id in ids:
                ids_cadastrados.append(int(id))

    # Se o arquivo não existir, não faz nada
    except IOError:
        return


# Salva o histórico de peças doadas em um arquivo oculto
def salvar_historico_pecas_doadas():

    # Abre o arquivo e fecha automaticamente
    with open(".historico_doacoes.txt", "w") as file:

        # Header
        file.write("id,tipo,tamanho,padrão,cor,data_doação,data_guarda_roupa,doado_para\n")

        # Salva cada doação no arquivo
        for doacao in historico_pecas_doadas:
            linha = ""

            # itera sobre as chaves do dicionário de doação para adicionar os valores de cada atributo da doação
            for atributo in doacao:
                linha += f"{doacao[atributo]},"
            
            linha = linha.strip(",") # Remove a última vírgula da linha

            file.write(linha + "\n") # Escreve os dados no arquivo e salta uma linha


# Carrega o histórico de peças doadas de arquivo oculto se existir
def carregar_historico_pecas_doadas():

    try:
        with open(".historico_doacoes.txt", "r") as file:

            # Lê o arquivo e retorna uma lista com todas as linhas de dados
            linhas = file.read().split("\n")[1:] # [1:] para descartar a primeira linha (Header)
            linhas.pop() # Eliminar linha vazia no final

            for linha in linhas:

                valores = linha.split(",")
                
                # Guarda os valores da doação em variáveis explícitas
                id = int(valores[0])
                tipo = valores[1]
                tamanho = valores[2]
                padrao = valores[3]
                cor = valores[4]
                data_doacao = datetime.fromisoformat(valores[5]).date() # Transforma Str em um objeto datetime
                data_guarda_roupa = datetime.fromisoformat(valores[6]).date()
                doado_para = valores[7]

                # Cria peça para poder registrar a doação (mas não adiciona a peça ao guarda-roupa)
                peca = criar_peca(id, tipo, tamanho, padrao, cor, data_guarda_roupa, SITUACAO_DOACAO, 0.0)

                registrar_peca_doada(peca, doado_para, data_doacao)

    # Se não existir o arquivo, não faz nada
    except IOError:
        return


