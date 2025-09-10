# Caixa eletronico
# - verificar saldo / Depositar dinheiro / Sacar dinheiro / Sair
# Obs: começar conta com saldo de R$ 200.00

def saldo_atual(saldo):  # função que mostra o saldo
    print(f"Saldo atual R$ {saldo :.2f}") 
    return saldo


def depositar_dinheiro(saldo): # função para depositar dinheiro
    while True:
        try:
            valor = float(input("Valor para depósito R$: "))
        except ValueError:
            print("Erro: entrada inválida.")
            continue
        
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor :.2f} realizado com sucesso!")
        else:
            print("Valor precisa ser maior que zero!")
        
        return saldo
    
    
def sacar_dinheiro(saldo):  # função para sacar dinheiro
    while True:
        try:
            valor = float(input("Valor para saque R$: "))
        except ValueError:
            print("Erro: entrada inválida.")
            continue
        
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor :.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente")
    
        return saldo
    

def menu():
    saldo = 200.00  # saldo inicial 
    
    while True:
        print("\n========== CAIXA ELETRÔNICO ==========")
        print("1 - VER SALDO")
        print("2 - DEPOSITAR DINHEIRO")
        print("3 - SACAR DINHEIRO")
        print("0 - SAIR")
        
        opc = input("ESCOLHA: ")
        
        if opc == "1":
            saldo_atual(saldo)
        elif opc == "2":
            saldo = depositar_dinheiro(saldo)   # recebe o novo saldo
        elif opc == "3":
            saldo = sacar_dinheiro(saldo)       # recebe o novo saldo
        elif opc == "0":
            print("ENCERRANDO PROGRAMA....")
            break
        else:
            print("ESCOLHA UMA OPÇÃO VÁLIDA!")
            

# Bloco principal do programa
if __name__ == "__main__":
    menu()
