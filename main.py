from datetime import date
import datetime

# Constantes Tipo
TIPO_CALCADO = "calçado"
TIPO_INFERIOR = "inferior"
TIPO_SUPERIOR = "superior"

# Constantes Tamanho
TAMANHO_P = "p"
TAMANHO_M = "m"
TAMANHO_G = "g"

# Constantes Padrão
PADRAO_FEMININO = "feminino"
PADRAO_MASCULINO = "masculino"
PADRAO_UNISSEX = "unissex"

# Constantes Cor
COR_VERMELHO = "vermelho"
COR_AZUL = "azul"
COR_AMARELO = "amarelo"
COR_ROSA = "rosa"
COR_BRANCO = "branco"
COR_CINZA = "cinza"
COR_VERDE = "verde"
COR_PRETO = "preto"
COR_ROXO = "roxo"
COR_VIOLETA = "violeta"
COR_LARANJA = "laranja"

# Constantes Situação
SITUACAO_VENDA = "venda"
SITUACAO_DOACAO = "doação"
SITUACAO_FICAR = "ficar"

pecas = []
estilos = {}
historico_pecas_doadas = []
historico_pecas_vendidas = []

""""
Estrutura de pecas
pecas = [
    {
        "id": 0,
        "tipo": "calçado",
        "tamanho": "p",
        "padrão": "unissex,
        "cor": "amarelo",
        "data": date(),
        "situação": "venda",
        "preço": 39.99
    },
]

Estrutura de estilos
estilos = {
  "nome": {
      "contador": 0,
      "peças": [
          [superior1, superior2, superior3],
          [inferior1, inferior2, inferior3],
          [calçado1, calçado2, calçado3]
        ]    
    }
}

Estrutura de historico_pecas_doadas
historico_pecas_doadas = [
    {
        "id": 1,
        "tipo": "calçado",
        "tamanho": "m",
        "padrão": "masculino",
        "cor": "azul",
        "data_doação": date(),
        "data_guarda_roupa": date(),
        "doado_para": "Lar Carla Alcântara"
    }
]

Estrutura de historico_pecas_vendidas
historico_pecas_vendidas = [
    {
        "id": 1,
        "tipo": "calçado",
        "tamanho": "m",
        "padrão": "masculino",
        "cor": "azul",
        "data_doação": date(),
        "data_guarda_roupa": date(),
        "vendido_para": "José Almeida Campos",
        "preço": 52.90
    }
]
"""


def inserir_peca(tipo, tamanho, padrao, cor, data:date, situacao, preco):
    # Integridade das peças é garantida na interface do usuário.

    id = len(pecas) + 1
    peca = {
        "id": id, "tipo": tipo, "tamanho": tamanho,
        "padrão": padrao, "cor": cor, "data": data, 
        "situação": situacao, "preço": preco
    }
    pecas.append(peca)


# Cria um novo estilo com 3 peças de cada tipo, se alguma peça não existir, será jogado um erro,
# Se alguma lista de id tiver peça de tipo diferente do especificado, será jogado um erro.
def inserir_estilo(nome, calcados_id:list, inferiores_id:list, superiores_id:list):
    calcados = retorna_3pecas_mesmo_tipo(calcados_id, TIPO_CALCADO)
    inferiores = retorna_3pecas_mesmo_tipo(inferiores_id, TIPO_INFERIOR)
    superiores = retorna_3pecas_mesmo_tipo(superiores_id, TIPO_SUPERIOR)
        
    estilos[nome] = {"contador": 0, "peças": [superiores, inferiores, calcados]}


# Com uma lista de ids, seleciona 3 peças e assegura que possuem o mesmo tipo especificado na função
def retorna_3pecas_mesmo_tipo(id_list:list, tipo):
    if len(id_list) != 3:
        raise Exception("Erro: Lista de ids com tamanho diferente de 3.")

    pecas = []

    for id in id_list:
        peca = retorna_peca_por_id(id)
        if checa_tipo_peca(peca, tipo) == False:
            raise Exception(f"Erro: Peça de id-{id} não é uma peça do tipo {tipo}!")
        
        pecas.append(peca)
    
    return pecas


# retorna a peça pelo id. ATENÇÃO: se a peça não for encontrada, um erro será jogado
def retorna_peca_por_id(id):
    for item in pecas:
        if item["id"] == id:
            return item
    raise Exception(f"Erro: id {id} não existente!")


# Retorna True se o tipo da peça for o mesmo que o passado na função e False se diferente
def checa_tipo_peca(peca:dict, tipo):
    return peca["tipo"] == tipo


# Printa todas as peças passadas em uma lista, em formato organizado e com cabeçalho
def print_pecas_filtradas(pecas_filtradas:list):
    # Cabeçalho
    print("  Id     Tipo    Tamanho    Padrão       Cor        Data      Situação     Preço")

    for peca in pecas_filtradas:
        print_peca(peca)


# Lista todas as peças
def listar_pecas():
    print("\nTodas as peças:")
    print_pecas_filtradas(pecas)


# Printa uma única peça
def print_peca(peca:dict):
    print(f"{peca['id']:4d}   {peca['tipo']:8s}     {peca['tamanho']}     {peca['padrão']:9s}    {peca['cor']:8s}  {peca['data']}     {peca['situação']:6s}   {peca['preço']:7.2f}")


# Lista peças de mesmo tamanho
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
        
        print(f"\nPeças filtradas por tamanho {tamanho} e padrão {padrao}:")
        print_pecas_filtradas(pecas_filtradas)


def listar_pecas_situacao(situacao):
    return # TODO: Se roupas à venda, mostrar em ordem de preço crescente, se doação, em ordem de aquisição.
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
    # Estrutura de repetição para checar cada peça. Se a situação da peça for para doação, armazena essa peça em uma lista
    # Armazea, a mesma estrutura de repetição as datas de cada peça para doação 
    for i in range(len(pecas)):
        if pecas[i]["situação"] == SITUACAO_DOACAO:
            lista_doacao.append(pecas[i])
            lista_datas.append(pecas[i]["data"]) 
    # Método sorted de listas para organizar as datas da mais recente para a mais antiga
    lista_datas_ordenada = sorted(lista_datas,reverse = True)
    # Estrutura de repetição para procurar a peça com cada data da lista organizada de datas  
    for datas in lista_datas_ordenada:
        j = 0 
        # While para procurar a peça, com estrutura condicional para não repetir a mesma peça 
        while j < len(lista_doacao):
            if lista_doacao[j]["data"] == datas:
                # Se a peça não tivar na lista_doacao_ordenada ela é adicionada nessa lista
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
        # TODO: listar as peças de cada estilo

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

        print("\nVocê escolheu o estilo %s" %estilo)

        # Checa se o usuário quer mudar o estilo
        while True:
            resposta = input("Deseja confirmar escolha do estilo %s? [s/n] " %estilo)

            if resposta == "s" or resposta == "sim":
                mudar = False
                break
            elif resposta == "n" or resposta == "não":
                estilos[estilo]["contador"] += 1
                mudar = True
                break
            else:
                print('\nResposta inválida! Digite "s" para sim ou "n" para não.')
    
    # Incrementa 1 ao contador do estilo escolhido
    estilos[estilo]["contador"] += 1
    print("\nEstilo %s escolhido com sucesso!" %estilo)



def listar_estilos():
    return # TODO: Listar estilos em ordem crescente de usos.

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
    if len(historico_pecas_vendidas) > 0:
        print("\nPeças vendidas:")
        print(f"{'Comprador':^35} {'Tipo':^10} {'Tamanho':^10} {'Padrão':^6} {'Cor':^13} {'Preço':^10}  {'Data de Venda'}  {'Data de Cadastro'}")
        
        for peca in historico_pecas_vendidas:
            print(f"{peca['vendido_para']:35s}  {peca['tipo']:10s}  {peca['tamanho']:^6}  {peca['padrão']:10s}  {peca['cor']:8s} {peca['preço']:10}   {peca['data_venda']}     {peca['data_guarda_roupa']}")
    else:
        print("\nPeças vendidas:\nNenhuma peça foi vendida até o momento >:(")
        return

def interface_usuario():
    """
    # carregar arquivo de peças e listas ao executar o programa

    0 -> Cadastrar Peça
    1 -> Cadastrar Estilo

    2 -> Pesquisar estilo por nome # Edson (done)
    3 -> Listar peças por tamanho e padrão # Bruno (done)
    4 -> Listar peças para venda # Israel (done)
    5 -> Listar peças para doação # Israel (done)
    6 -> Listar estilos # Israel
    7 -> Listar peças doadas # Bruno (done)
    8 -> Listar peças vendidas # Edson (done)
    9 -> Vender peça # Edson (histórico de vendas) (done)
    10 -> Doar peça # Bruno (histórico de doações) (done)
    11 -> Alterar peça (done)
    12 -> Alterar estilo
    13 -> Remover peça (done)
    14 -> Remover estilo

    # Depois
    15 -> Carregar arquivos (peças, estilos, historico_vendas, historico_doações)
    16 -> Salvar alterações (peças, estilos, historico_vendas, historico_doações)

    """
    return # Printar a interface pro usuário.

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

# Remove a peça por id, se o id não existir, não será possível encontrar a peça e um erro será jogado.
def remover_peca(id):
    peca = retorna_peca_por_id(id)
    pecas.remove(peca) # Remove o dicionário peca da lista pecas.
    print(f"Atenção: Peça de id {id} foi removida do Guarda Roupa Virtual.")

# vender_para = nome do comprador.
def vender_peca(id, vender_para):
    peca = retorna_peca_por_id(id)
    if peca["situação"] != SITUACAO_VENDA:
        raise Exception("Peça não disponível para venda. Tente alterar a situação da peça antes em 'Alterar peça'.")
    
    # adiciona informações da peça doada ao historico_pecas_doadas.
    historico_pecas_vendidas.append({
        "id": id,
        "tipo": peca["tipo"],
        "tamanho": peca["tamanho"],
        "padrão": peca["padrão"],
        "cor": peca["cor"],
        "data_venda": datetime.datetime.today().date(), # Data de hoje no formato YYYY-MM-DD
        "data_guarda_roupa": peca["data"],
        "vendido_para": vender_para,
        "preço": peca["preço"]
    })

    # remove peça do guarda roupa (pecas)
    remover_peca(id)

# doar_para = nome da instituição ou pessoa que recebeu a doação.
# doar_peca remove a peça do guarda roupa.
def doar_peca(id, doar_para):
    peca = retorna_peca_por_id(id) # Impede a execução se o id não for encontrado.
    if peca["situação"] != SITUACAO_DOACAO:
        raise Exception("Peça não disponível para doação. Tente alterar a situação da peça antes em 'Alterar peça'.")
    
    # adiciona informações da peça doada ao historico_pecas_doadas.
    historico_pecas_doadas.append({
        "id": id,
        "tipo": peca["tipo"],
        "tamanho": peca["tamanho"],
        "padrão": peca["padrão"],
        "cor": peca["cor"],
        "data_doação": datetime.datetime.today().date(), # Data de hoje no formato YYYY-MM-DD
        "data_guarda_roupa": peca["data"],
        "doado_para": doar_para
    })

    # remove peça do guarda roupa (pecas)
    remover_peca(id)

    
def main():
    # TODO: Criar interface para interagir com o usuário
    # Lembrar de usar Try catch para inserir_estilo()

    inserir_peca(TIPO_CALCADO, TAMANHO_M, PADRAO_MASCULINO, COR_CINZA, date(2022, 6, 22), SITUACAO_FICAR, 0.0)
    inserir_peca(TIPO_CALCADO, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_CALCADO, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_G, PADRAO_UNISSEX, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 270.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 330.0)
    inserir_peca(TIPO_INFERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 3330.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_UNISSEX, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 30.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_G, PADRAO_UNISSEX, COR_BRANCO, date(2022, 2, 12), SITUACAO_VENDA, 15.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_VERMELHO, date(2022, 2, 12), SITUACAO_DOACAO, 0.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_LARANJA, date(2021, 5, 10), SITUACAO_DOACAO, 0.0)
    # listar_pecas_para_doacao()
    # print_pecas()
    # inserir_estilo("casual", [1,2,3], [4,5,6], [7,8,9])
    # print(estilos)
    # listar_pecas_tamanho_padrao(padrao=PADRAO_FEMININO, tamanho=TAMANHO_M)
    # doar_peca(1, "Coração de Jesus")
    # doar_peca(9, "César")
    # doar_peca(10, "Lar Criança Feliz")
    # listar_pecas_para_venda()
    # listar_pecas()
    #alterar_peca(3, data=date(2002,6,15), preco=5.21)
    #remover_peca(4)
    #listar_pecas()

    # vender_peca(8, "Genivaldo Borges")
    # vender_peca(2, "Zé do Bar")
    # listar_pecas_vendidas()

    inserir_estilo("casual", [1,2,3], [4,5,6], [7,8,9])
    inserir_estilo("esportivo", [1,2,3], [4,5,6], [7,8,9])
    selecionar_estilo()


if __name__ == "__main__":
    main()