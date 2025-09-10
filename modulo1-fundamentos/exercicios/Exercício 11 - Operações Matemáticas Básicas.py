# Exercício 11 - Operações Matemáticas Básicas
# Objetivo: Pedir dois números e aplicar operações básicas: soma, subtração, multiplicação e divisão

# Solicita ao usuário que digite dois números
try:
    num1 = float(input("Digite o primeiro número: "))  # Converte entrada para float
    num2 = float(input("Digite o segundo número: "))
except ValueError:  # Caso o usuário digite algo inválido
    print("Você deve digitar apenas números!")
    exit()  # Encerra o programa

# Soma
soma = num1 + num2
print(f"Soma: {num1} + {num2} = {soma}")

# Subtração
subtracao = num1 - num2
print(f"Subtração: {num1} - {num2} = {subtracao}")

# Multiplicação
multiplicacao = num1 * num2
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")

# Divisão com verificação para evitar divisão por zero
if num2 != 0:
    divisao = num1 / num2
    print(f"Divisão: {num1} / {num2} = {divisao:.2f}")  # Formata com 2 casas decimais
else:
    print("Divisão: não é possível dividir por zero")