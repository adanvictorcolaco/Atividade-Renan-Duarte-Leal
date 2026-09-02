import unittest
from gerenciador import GerenciadorTarefas

class TestGerenciadorTarefas(unittest.TestCase):

    def setUp(self):
        # Executado antes de cada teste para garantir isolamento
        self.gerenciador = GerenciadorTarefas()

    def test_adicionar_e_listar_tarefa(self):
        # Act
        self.gerenciador.adicionar_tarefa("Estudar testes unitários")
        tarefas = self.gerenciador.listar_tarefas()

        # Assert
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["id"], 1)
        self.assertEqual(tarefas[0]["titulo"], "Estudar testes unitários")
        self.assertFalse(tarefas[0]["concluida"])

if __name__ == '__main__':
    unittest.main()