from src.connection import ElasticConnection
from src.mapping import mapping_auxilio
import dask.dataframe as dd

from glob import glob

import json
import logging
from elasticsearch import Elasticsearch, helpers

JSON_FILE = "data/dados_1.csv"

logging.getLogger().setLevel(logging.INFO)


def create_index_candidatos():

    logging.info("CRIANDO INDEX NO ELASTICSEARCH")
    es_client = ElasticConnection()
    es_client.create_index("auxilio-emergencial", mapping_auxilio)

def ingest_index_candidatos():
    es_client = ElasticConnection()
    
    files_json = glob('data/dados.json/*.part')

    contents = []
    # for json_f in files_json:
    json_f = "data/dados.json/010.part"
    logging.info("PROCESSANDO ARQUIVO")
    for line in open(json_f, 'r'):
        contents.append(json.loads(line))
    
    logging.info("INSERINDO DADOS NO INDEX")
    helpers.bulk(es_client.client, contents, index="auxilio-emergencial")

if __name__ == '__main__':
    create_index_candidatos()
    ingest_index_candidatos()
