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

Estrutura de pecas_doadas
pecas_doadas = [
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
"""


def inserir_peca(tipo, tamanho, padrao, cor, data:date, situacao, preco):
    # TODO: Assegurar a integridade de cada peça. ex: não cadastrar tamanhos que não existem, etc.

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
        raise Exception("Lista de ids com tamanho diferente de 3.")

    pecas = []

    for id in id_list:
        peca = retorna_peca_por_id(id)
        if checa_tipo_peca(peca, tipo) == False:
            raise Exception(f"Peça de id-{id} não é uma peça {tipo}!")
        
        pecas.append(peca)
    
    return pecas


# retorna a peça pelo id. ATENÇÃO: se a peça não for encontrada, um erro será jogado
def retorna_peca_por_id(id):
    for item in pecas:
        if item["id"] == id:
            return item
    raise Exception("id não existente!")


# Retorna True se o tipo da peça for o mesmo que o passado na função e False se diferente
def checa_tipo_peca(peca:dict, tipo):
    return peca["tipo"] == tipo


# Printa todas as peças passadas em uma lista, em formato organizado e com cabeçalho
def print_pecas_filtradas(pecas_filtradas:list):
    # Cabeçalho
    print("  Id     Tipo    Tamanho    Padrão       Cor        Data      Situação     Preço")

    for peca in pecas_filtradas:
        print_peca(peca)


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

    print_pecas_filtradas(pecas_filtradas)


# Lista peças de mesmo padrão
def listar_pecas_padrao(padrao):
    pecas_filtradas = []
    for peca in pecas:
        if peca["padrão"] == padrao:
            pecas_filtradas.append(peca)

    if len(pecas_filtradas) == 0:
        raise Exception(f"Não foram encontradas peças de tamanho {padrao}") 

    print_pecas_filtradas(pecas_filtradas)


# Lista as peças de mesmo tamanho e padrão, também lista com apenas tamanho ou padrão especificados
def listar_pecas_tamanho_padrao(tamanho="", padrao=""):
    # Se tamanho ou padrão não estiverem no formato especificado, será jogado um erro
    if tamanho != TAMANHO_P and tamanho != TAMANHO_M and tamanho != TAMANHO_G and tamanho != "":
        raise Exception("Tamanho de peça inválido")
    if padrao != PADRAO_FEMININO and padrao != PADRAO_MASCULINO and padrao != PADRAO_UNISSEX and padrao != "":
        raise Exception("Padrão de peça inválido")

    # passa TODAS as peças para print_pecas_filtradas
    if tamanho == "" and padrao == "":
        print_pecas_filtradas(pecas)

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
        
        print_pecas_filtradas(pecas_filtradas)


def listar_pecas_situacao(situacao):
    return # TODO: Se roupas à venda, mostrar em ordem de preço crescente, se doação, em ordem de aquisição.


def selecionar_estilo(nome):
    return # TODO: Deve listar os estilos e perguntar qual estilo o usuário quer escolher,
    # o programa apresentará as peças do estilo e pedirá a confirmação da seleção, se confirmado, incrementar o contador do estilo.


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
    return

def interface_usuario():
    """
    # carregar arquivo de peças e listas ao executar o programa

    0 -> Cadastrar Peça
    1 -> Cadastrar Estilo

    2 -> Pesquisar estilo por nome # Edson
    3 -> Listar peças por tamanho e padrão # Bruno (done)
    4 -> Listar peças para venda # Israel
    5 -> Listar peças para doação # Israel
    6 -> Listar estilos # Israel
    7 -> Listar peças doadas # Bruno (done)
    8 -> Listar peças vendidas # Edson
    9 -> Vender peça # Edson (histórico de vendas)
    10 -> Doar peça # Bruno (histórico de doações) (done)
    11 -> Alterar peça
    12 -> Alterar estilo
    13 -> Remover peça (done)
    14 -> Remover estilo

    # Depois
    15 -> Carregar arquivos (peças, estilos, historico_vendas, historico_doações)
    16 -> Salvar alterações (peças, estilos, historico_vendas, historico_doações)

    """
    return # Printar a interface pro usuário.


def remover_peca(id):
    for peca in pecas:
        if peca["id"] == id:
            # Remove o dicionário peca da lista pecas
            pecas.remove(peca)
            return
    raise Exception(f"Não foi possível remover a peça de id: {id}, pois ela não existe.")

# vender_para = nome do comprador.
def vender_peca(id, vender_para, preco):
    return

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
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_VERMELHO, date(2022, 2, 12), SITUACAO_VENDA, 0.0)
    inserir_peca(TIPO_SUPERIOR, TAMANHO_P, PADRAO_MASCULINO, COR_LARANJA, date(2022, 2, 12), SITUACAO_VENDA, 0.0)

    # print_pecas()
    # inserir_estilo("casual", [1,2,3], [4,5,6], [7,8,9])
    # print(estilos)
    # listar_pecas_tamanho_padrao(padrao=PADRAO_FEMININO, tamanho=TAMANHO_M)
    # doar_peca(1, "Coração de Jesus")
    # doar_peca(9, "César")
    # doar_peca(10, "Lar Criança Feliz")
    listar_pecas_doadas()


if __name__ == "__main__":
    main()