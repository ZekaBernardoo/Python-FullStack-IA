# modulo1_ex08.py
try:
    numero = int(input("Digite um número: "))
    print("Número digitado:", numero)
except ValueError:
    print("Isso não é um número válido!")