import pandas as pd

DATA_FILE = "data/dados.csv"
JSON_FILE = "data/dados.json"


def rename_columns():
    df = pd.read_csv(DATA_FILE, encoding="ISO-8859-1")
    df.rename(columns={"MÊS DISPONIBILIZAÇÃO": "mes_disponibilizacao",
                       "UF": "uf",
                       "CÓDIGO MUNICÍPIO IBGE": "codigo_municipio_ibge",
                       "NOME MUNICÍPIO": "nome_municipio",
                       "NIS BENEFICIÁRIO": "nis_beneficiario",
                       "CPF BENEFICIÁRIO": "cpf_beneficiario",
                       "NOME BENEFICIÁRIO": "nome_beneficiario",
                       "NIS RESPONSÁVEL": "nis_responsavel",
                       "CPF RESPONSÁVEL": "cpf_responsavel",
                       "NOME RESPONSÁVEL": "nome_responsavel",
                       "ENQUADRAMENTO": "enquadramento",
                       "PARCELA": "parcela",
                       "OBSERVAÇÃO": "observacao",
                       "VALOR BENEFÍCIO": "valor_beneficio"})

    df.to_json(JSON_FILE, orient="records")
