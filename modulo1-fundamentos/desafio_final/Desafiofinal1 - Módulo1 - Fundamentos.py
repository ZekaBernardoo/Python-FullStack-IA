# Desafio Final - Módulo 1: Fundamentos de Python
# Objetivo: Coletar números do usuário e analisar maior, menor e média

# Função para coletar números do usuário
def coletar_numeros():
    numeros = []  # Lista para armazenar os números digitados
    while True:   # Loop infinito, será interrompido quando o usuário digitar 'sair'
        try:
            n = input("Digite um número (ou 'sair' para encerrar): ")  # Entrada do usuário
            if n.lower() == 'sair':  # Verifica se o usuário quer encerrar
                break
            numeros.append(float(n))  # Converte para float e adiciona à lista
        except ValueError:  # Caso o usuário digite algo que não seja número
            print("Digite um número válido!")  # Mensagem de erro
    return numeros  # Retorna a lista de números coletados

# Função para analisar os números coletados
def analisar_numeros(numeros):
    if not numeros:  # Verifica se a lista está vazia
        print("Nenhum número digitado.")
        return
    maior = max(numeros)  # Descobre o maior número
    menor = min(numeros)  # Descobre o menor número
    media = sum(numeros)/len(numeros)  # Calcula a média
    # Exibe os resultados
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Média: {media:.2f}")  # Formata média com 2 casas decimais

# Bloco principal do programa
if __name__ == "__main__":
    # Chama função de coleta
    numeros = coletar_numeros()
    # Chama função de análise
    analisar_numeros(numeros)