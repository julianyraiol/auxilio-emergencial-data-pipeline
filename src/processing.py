import dask.dataframe as dd
import logging

from connection import ElasticConnection
from elasticsearch import Elasticsearch, helpers


DATA_FILE = "../data/dados.csv"
JSON_FILE = "../data/dados.json"

logging.getLogger().setLevel(logging.INFO)

def rename_columns():

    logging.info("RENOMEANDO COLUNAS")
    df = dd.read_csv(DATA_FILE, encoding="latin-1", sep=";")
    df.columns = ["mes_disponibilizacao", "uf", "codigo_municipio_ibge", "nome_municipio", "nis_beneficiario", "cpf_beneficiario", "nome_beneficiario", "nis_responsavel", "cpf_responsavel", "nome_responsavel", "enquadramento", "parcela", "observacao", "valor_beneficio"]


    logging.info("CRIANDO NOVO JSON")
    dd.to_json(df, JSON_FILE, orient="records", force_ascii=False)

if __name__ == "__main__":
    rename_columns()

