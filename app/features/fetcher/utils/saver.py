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
                "uriUltimoRelator": data["dados"]["statusProposicao"]["uriUltimoRelator"] if "statusProposicao" in data["dados"] else None,
            },
        }
        return data_saving

    @classmethod
    def save_author_data(cls, data):
        data_saving = {
            "nome": data["dados"]["nomeCivil"] if "nomeCivil" in data["dados"] else data["dados"]["nome"],
            "cpf": data["dados"]["cpf"] if "cpf" in data["dados"] else None,
            "foto": data["dados"]["ultimoStatus"]["urlFoto"] if "ultimoStatus" in data["dados"] else None,
            "sexo": data["dados"]["sexo"] if "sexo" in data["dados"] else None,
            "nascimento": data["dados"]["dataNascimento"] if "dataNascimento" in data["dados"] else None,
            "local_nascimento": f"{data['dados']['municipioNascimento']} - {data['dados']['ufNascimento']}" if "municipioNascimento" in data["dados"] else None,
            "escolaridade": data["dados"]["escolaridade"] if "escolaridade" in data["dados"] else None,
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
