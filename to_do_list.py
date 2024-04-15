import os
import csv
from tarefa import tarefa

class to_do_list:
    def __init__(self, nome='tarefas.csv'):
        self.nome = nome
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        if not os.path.exists(self.nome):
            return []
        with open(self.nome, 'r', newline='') as file:
            leitor = csv.DictReader(file)
            return [tarefa(row['Nome'], row['Descricao'], row['Prioridade'], row['Feita']) for row in leitor]

    def salvar_tarefas(self):
        cabecalhos = ['Nome', 'Descricao', 'Prioridade', 'Feita']
        with open(self.nome, 'w', newline='') as file:
            escritor = csv.DictWriter(file, fieldnames=cabecalhos)
            escritor.writeheader()
            for tarefa in self.tarefas:
                escritor.writerow({'Nome': tarefa.get_nome(), 'Descricao': tarefa.get_descricao(), 'Prioridade': tarefa.get_prioridade(), 'Feita': tarefa.get_feita()})

    def criar_tarefas(self, tarefa: tarefa):
        self.tarefas.append([tarefa.get_nome(), tarefa.get_descricao(), tarefa.get_prioridade(), tarefa.get_feita()])
        self.salvar_tarefas()
        print("Tarefa adicionada.")

    def ler_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for index, tarefa in enumerate(self.tarefas, start=1):
                print(f"{index}. {tarefa.to_string()}")

    def atualizar_tarefas(self, index: int, tarefa: tarefa):
        if 0 < index <= len(self.tarefas):
            self.tarefas[index - 1] = tarefa
            self.salvar_tarefas()
            print("Tarefa atualizada.")
        else:
            print("Numero de tarefa invalido")

    def remover_tarefas(self, index: int):
        if 0 < index <= len(self.tarefas):
            del self.tarefas[index - 1]
            self.salvar_tarefas()
            print("Tarefa removida.")
        else:
            print("Numero de tarefa invalido.")
