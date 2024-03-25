import requests
import json
from utils.fetcher import UriFetcher
from utils.saver import Saver


max_pages = 20  # Substitua por seu número máximo de páginas
data_list = []
for page in range(1, max_pages + 1):
    fetch = UriFetcher.fetch_uris(
        f"https://dadosabertos.camara.leg.br/api/v2/proposicoes?ordem=ASC&ordenarPor=id&pagina={page}&itens=100"
    )

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