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

# Variáveis globais para armazenar peças, estilos e históricos de peças.
pecas = []
estilos = {}
historico_pecas_doadas = []
historico_pecas_vendidas = []
ids_cadastrados = [] # Lista de inteiros não nulos e não negativos

""""
Estrutura de pecas
pecas = [
    {
        "id": 0,
        "tipo": "calçado",
        "tamanho": "p",
        "padrão": "unissex",
        "cor": "amarelo",
        "data": date(),
        "situação": "venda",
        "preço": 39.99
        "estilos": ["casual", "esportivo", "clássico"]
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