from to_do_list import to_do_list
from tarefa import tarefa

def main():
    to_do = to_do_list()

    print("TO DO List")
    
    while True:
        print("Digite uma das seguintes opcoes para utilizar o programa")
        print("1) Adicionar tarefa")
        print("2) Listar tarefas")
        print("3) Atualizar tarefa")
        print("4) Remover tarefa")
        print("5) Sair")

        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            adiciona_tarefa(to_do)
        elif choice == 2:
            mostra_tarefas(to_do)
        elif choice == 3:
            atualiza_tarefa(to_do)
        elif choice == 4:
            remover_tarefa(to_do)
        elif choice == 5:
            print("Programa encerrado.")
            break
        else:
            print("opcao invalida.")

def adiciona_tarefa(to_do: to_do_list):
    nome = str(input("Digite o titulo da tarefa: "))
    descricao = str(input("Digite a descricao da tarefa: "))
    prioridade = int(input("Digite o indice de prioridade da tarefa (1 sendo a mais baixa ate 3): "))

    while prioridade < 1 or prioridade > 3:
        print("Prioridade invalida!")
        prioridade = int(input("Digite o grau de prioridade da tarefa (1 sendo a mais baixa ate 3): "))
    
    nova_tarefa = tarefa(nome, descricao, prioridade, False)
    to_do.criar_tarefas(nova_tarefa)
    
def mostra_tarefas(to_do: to_do_list):
    to_do.ler_tarefas()

def atualiza_tarefa(to_do: to_do_list):
    to_do.ler_tarefas()
    if to_do.tarefas:
        index = int(input("Digite o indice da tarefa que voce deseja atualizar: "))
        nome = str(input("Digite o titulo atualizado da tarefa: "))
        descricao = str(input("Digite a descricao atualizada da tarefa: "))
        prioridade = int(input("Digite o grau de prioridade atualizado da tarefa: "))
        verificador = int(input("Digite 0 se a tarefa nao foi feita ou 1 se a tarefa foi feita"))
        while verificador < 0 or verificador > 1:
            print("opcao invalida")
            verificador = int(input("Digite 0 se a tarefa nao foi feita ou 1 se a tarefa foi feita"))

        to_do.atualizar_tarefas(index, tarefa(nome, descricao, prioridade, bool(verificador)))

def remover_tarefa(to_do: to_do_list):
    to_do.ler_tarefas()
    if to_do.tarefas:
        index = int(input("Digite o indice da tarefa que voce deseja excluir: "))
        to_do.remover_tarefas(index)

if __name__ == "__main__":
    main()
