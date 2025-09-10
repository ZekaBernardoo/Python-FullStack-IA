import json
import os

# Caminho para o JSON (na raiz do repositório)
arquivo_json = os.path.join(os.path.dirname(__file__), "../progresso.json")

def atualizar_modulo(modulo, status, cor):
    try:
        with open(arquivo_json, "r") as f:
            progresso = json.load(f)
    except FileNotFoundError:
        progresso = {}

    progresso[modulo] = {"status": status, "cor": cor}

    with open(arquivo_json, "w") as f:
        json.dump(progresso, f, indent=2)
    
    print(f"{modulo} atualizado para {status} ({cor})")

# Exemplo de uso
if __name__ == "__main__":
    # Atualize os módulos que você concluiu
    atualizar_modulo("modulo1", "Concluído", "green")
    atualizar_modulo("modulo2", "Em andamento", "yellow")
