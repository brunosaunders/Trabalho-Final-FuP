from datetime import date
from models import *
from crud import *


def interface_usuario():
    """
    # carregar arquivo de peças e listas ao executar o programa

    0 -> Cadastrar Peça
    1 -> Cadastrar Estilo

    2 -> Pesquisar estilo por nome # Edson (done) ---> TODO: listar peças de cada estilo
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
    
    listar_pecas()
    adicionar_peca_a_estilo(3, "casual")
    adicionar_peca_a_estilo(3, "romântico")
    adicionar_peca_a_estilo(6, "casual")
    adicionar_peca_a_estilo(7, "romântico")
    remover_peca(3)
    remover_peca(7)

if __name__ == "__main__":
    main()