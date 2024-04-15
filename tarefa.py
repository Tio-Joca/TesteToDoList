class tarefa:

    def __init__(self, nome: str, descricao: str, prioridade: int, feita: bool):
        self.nome = nome
        self.descricao = descricao
        self.prioridade = prioridade
        self.feita = feita

    def set_nome(self, nome: str):
        self.nome = nome

    def set_descricao(self, descricao: str):
        self.descricao = descricao

    def set_prioridade(self, prioridade: int):
        self.prioridade = prioridade

    def set_feita(self, feita: bool):
        self.feita = feita

    def get_nome(self) -> str:
        return self.nome
    
    def get_descricao(self) -> str:
        return self.descricao
    
    def get_prioridade(self) -> int:
        return self.prioridade
    
    def get_feita(self) -> bool:
        return self.feita
    
    def to_string(self) -> str:
        return f"Tarefa: {self.nome}\n   Descricao: {self.descricao}\n   Prioridade: {self.prioridade}\n   Feita: {self.feita}"