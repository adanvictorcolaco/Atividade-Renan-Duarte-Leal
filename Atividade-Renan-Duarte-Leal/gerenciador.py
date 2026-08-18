class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo):
        nova_tarefa = {"id": len(self.tarefas) + 1, "titulo": titulo, "concluida": False}
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        return self.tarefas