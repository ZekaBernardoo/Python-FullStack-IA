'''
- Objetivo: Escreva um progama que peça ao usuário um numero inteiro positivo
- e exiba a tabela de multiplicação para esses números, de 1 a  10.
- Ultilize um loop para eta tarefa.
'''
def entrada_usuario(): # Função que captura entrada via terminal
    
    while True: 
        try: # tratamento de exeção
            numero = int(input("Digite um número inteiro: "))
            
            if numero > 0: # tratando valores menores que Zero
                return numero
            else:
                print("Digite apenas numero inteiro e maior que Zero.")
                
        except ValueError:
            print("erro: Entrada Inválida!")
            continue # para voltar ao loop
        
def tabela_numeros(numero): # Função principal
    
    tabela = [] # lista vazia
    contador = 1 # contator
    
    while contador <= 10: # condição
        resultado = numero * contador # logica matematica
        tabela.append(f"{numero} X {contador}: {resultado}") # append armazena a entrada ao final da lista
        contador +=1 # incremento
        
    return tabela

def display(tabela):
    
    print("===========TABELA DE MULTIPLICAÇÃO========== ")
    for nat in tabela: # for pega cada intem e coloca em uma linha
        print(nat)
    
    print("=========FIM DA TABELA DE MULTIPLICAÇÃO==========")    

def multiplicar(): # função que engloba todas as funções
    numero = entrada_usuario()
    tabela = tabela_numeros(numero)
    display(tabela)

def menu():
    print("\n===========MENU===========")
    print(f"DIGITE 1 (MULTIPLICAR)")
    print(f"DIGITE 0 PARA SAIR..........")
    
    while True: # condição
        try:
            opc = input("ESCOLHA: ") # coleta entrada via terminal    
            if opc == '1':
                multiplicar()
                
            elif opc == '0':
                print("FINALIZANDO....")
                break
            else:
                print("ESCOLHA ENTRE AS OPÇÕES (1 MULTIPLICAR | (0)SAIR...)")
                
        except ValueError:
            print("erro: Entrada Inválida!")

# Bloco principal
if __name__ == "__main__":
    menu()