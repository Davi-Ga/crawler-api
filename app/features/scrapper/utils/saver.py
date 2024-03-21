class Saver:

    @classmethod
    def save_proposition_data(cls, data):
        data_saving = {
            "ementa": data["dados"]["ementa"] if "ementa" in data["dados"] else None,
            "ementaDetalhada": (
                data["dados"]["ementaDetalhada"]
                if "ementaDetalhada" in data["dados"]
                else None
            ),
            "keywords": data["dados"]["keywords"],
            "uris": {
                "uriAutores": data["dados"]["uriAutores"],
                "uriPropPrincipal": data["dados"]["uriPropPrincipal"] if "uriPropPrincipal" in data["dados"] else None,
                "uriUltimoRelator": data["dados"]["statusProposicao"]["uriUltimoRelator"] if "uriUltimoRelator" in data["dados"]["statusProposicao"] else None,
            },
        }
        return data_saving

    @classmethod
    def save_author_data(cls, data):
        data_saving = {
            "nome": data["dados"]["nomeCivil"],
            "cpf": data["dados"]["cpf"],
            "foto": data["dados"]["ultimoStatus"]["urlFoto"],
            "sexo": data["dados"]["sexo"],
            "nascimento": data["dados"]["dataNascimento"],
            "local_nascimento": f"{data['dados']['municipioNascimento']} - {data['dados']['ufNascimento']}",
            "escolaridade": data["dados"]["escolaridade"],
        }
        return data_saving

    @classmethod
    def save_principal_proposition_data(cls, data):
        data_saving = {
            "ementa": data["dados"]["ementa"],
            "situacao": data["dados"]["statusProposicao"]["descricaoSituacao"],
            "tipo": data["dados"]["descricaoTipo"],
            "keywords": data["dados"]["keywords"],
        }
        return data_saving
