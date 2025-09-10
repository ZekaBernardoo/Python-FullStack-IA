# modulo1_ex05.py
password = "Ebc9258#@!"

while True:
    try:
        opc = input("Digite sua senha: ")
    except ValueError:
        print("Erro: caracter invalido!")

    if opc == password:
        print("Acesso Permitido!")
        break
    else:
        print("Senha inválida.")
        
