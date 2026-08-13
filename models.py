class Obreiro:
    def __init__(self, id=None, nome="", telefone="", ativo=1):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.ativo = ativo


class Escala:
    def __init__(self, id=None, data="", obreiro_id=None):
        self.id = id
        self.data = data
        self.obreiro_id = obreiro_id