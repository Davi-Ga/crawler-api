import requests
import json
from utils.fetcher import UriFetcher
from utils.saver import Saver

fetch = UriFetcher.fetch_uris(
    "https://dadosabertos.camara.leg.br/api/v2/proposicoes?ordem=ASC&ordenarPor=id&pagina=1&itens=100"
)

data_list = []

for uri in fetch:
    data_dict = {}
    print(uri)
    uri = UriFetcher.fetch_uri_data(uri)
    data_proposition = Saver.save_proposition_data(uri)
    print(data_proposition)
    data_dict["proposicao"] = data_proposition

    if data_proposition["uris"]["uriUltimoRelator"] is not None:
        relator = UriFetcher.fetch_uri_data(
            data_proposition["uris"]["uriUltimoRelator"]
        )
        data_relator = Saver.save_author_data(relator)
        data_dict["relator"] = data_relator
    else:
        author = UriFetcher.fetch_author(data_proposition["uris"]["uriAutores"])
        data_author = Saver.save_author_data(author)
        data_dict["autor"] = data_author

    if data_proposition["uris"]["uriPropPrincipal"] is not None:
        principal_proposition = UriFetcher.fetch_uri_data(
            data_proposition["uris"]["uriPropPrincipal"]
        )
        data_principal_proposition = Saver.save_principal_proposition_data(
            principal_proposition
        )
        data_dict["proposicao_principal"] = data_principal_proposition

    data_list.append(data_dict)

with open("data.json", "w") as f:
    json.dump(data_list, f)
