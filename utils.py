from models import *


# Dado uma peça, retorna o índice linha da matriz peças que ocupará em um estilo.
def indice_peca_em_estilos(peca: dict):
    # Peças do tipo superior ocuparão a linha de índice 0 da matriz peças que está em estilos.
    if peca["tipo"] == TIPO_SUPERIOR:
        peca_index = 0
    # Peças do tipo inferior ocuparão a linha de índice 1 da matriz peças que está em estilos.
    elif peca["tipo"] == TIPO_INFERIOR:
        peca_index = 1
    # Peças do tipo calçado ocuparão a linha de índice 2 da matriz peças que está em estilos.
    elif peca["tipo"] == TIPO_CALCADO:
        peca_index = 2
    else:
        raise Exception("Erro: Essa peça possui um tipo inválido")
    
    return peca_index


# retorna a peça pelo id. ATENÇÃO: se a peça não for encontrada, um erro será jogado
def retorna_peca_por_id(id):
    for item in pecas:
        if item["id"] == id:
            return item
    raise Exception(f"Peça de id {id} não está cadastrada!")


# Retorna True se o tipo da peça for o mesmo que o passado na função e False se diferente
def checa_tipo_peca(peca:dict, tipo):
    return peca["tipo"] == tipo


# Conta o número de peças que existem em um estilo.
def conta_numero_de_pecas_em_estilo(nome_estilo):
    count_pecas = 0

    # Itera sobre cada linha da matriz peças em um dado estilo.
    for linha in estilos[nome_estilo]["peças"]:
        count_pecas += len(linha)

    return count_pecas