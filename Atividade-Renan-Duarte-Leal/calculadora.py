def calcular_media(notas):
    # Correção: divisão correta pelo número total de notas (len)
    return sum(notas) / len(notas)


def aplicar_desconto(preco, porcentagem):
    # Correção: cálculo correto do valor percentual de desconto
    return preco - (preco * (porcentagem / 100))


# Testes locais para confirmar a correção:
print("--- TESTANDO CÓDIGO CORRIGIDO ---")
print("Média esperada: 8.0 | Resultado:", calcular_media([10, 8, 6]))
print("Desconto esperado: 180.0 | Resultado:", aplicar_desconto(200, 10))