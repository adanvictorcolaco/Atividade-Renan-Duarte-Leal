# Atividade em Dupla - Colaboração Git/GitHub

## Integrantes
* Adan Victor Colaço
* [Marcos]

---

## 3. Planejamento dos Fluxos de Trabalho e Divisão de Tarefas

Simulação do fluxo de desenvolvimento colaborativo dividida em correções de bugs e novas funcionalidades:

| Módulo | Tipo | Descrição | Responsável | Branch |
| :--- | :--- | :--- | :--- | :--- |
| `calculadora.py` | Correção | Ajustar divisão do cálculo da média | Integrante A | `fix/bug1` |
| `calculadora.py` | Correção | Corrigir a fórmula do desconto proporcional | Integrante B | `fix/bug2` |
| `gerenciador.py` | Feature | Método de buscar tarefa por título | Integrante A | `feat/funcionalidade1` |
| `gerenciador.py` | Feature | Método de marcar tarefa como concluída | Integrante B | `feat/funcionalidade2` |

---

## Regras e Fluxo do Git
1. Todo o desenvolvimento ocorre em branches derivadas da `dev`.
2. Para cada alteração é aberto um **Pull Request (PR)** para a branch `dev`.
3. Os PRs exigem aprovação/revisão obrigatória do colega de dupla antes do merge.