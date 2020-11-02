mapping_auxilio = {
    "mappings": {
        "properties": {
            "mes_disponibilizacao": {"type": "long"},
            "uf": {"type": "text"},
            "codigo_municipio_ibge": {"type": "long"},
            "nome_municipio": {"type": "text"},
            "nis_beneficiario": {"type": "long"},
            "cpf_beneficiario": {"type": "text"},
            "nome_beneficiario": {"type": "text"},
            "nis_responsavel": {"type": "keyword"},
            "cpf_responsavel": {"type": "text"},
            "nome_responsavel": {"type": "text"},
            "enquadramento": {"type": "text"},
            "parcela": {"type": "text"},
            "observacao": {"type": "text"},
            "valor_beneficio": {"type": "text"}
        }
    }
}