# While usando condições complexas - 1º exemplo
x,y = 3,25

print("Visualização do Loop:")
print("-" * 30)

while x < 10 and y > 10:
    # "barra" visual mostrando valores de x e y
    barra_x = "█" * x
    barra_y = "█" * (y -10)  # ajustando escala
    
    print(f"X: {x:2} {barra_x} | Y: {y:2} {barra_y}")
    
    x += 1 # incremento
    y -= 1 # decremento

print("-" * 30)
print("Loop completo!")
print(f"Valores finais - X: {x} e Y: {y}")
print("="*50)  

#================================================================================  
# While usando condições complexas - 2º exemplo
print("TENTE ADIVINHAR OS NUMERO SECRESTOS (1-10)")
numero_secreto1 = 5
numero_secreto2 = 7
tentativas = 3
adivinhou1 = False
adivinhou2 = False

while tentativas > 0 and (not adivinhou1 == True or not adivinhou2 == True): 
    # enquanto tentativa for maior que 0 e diferente de false continuar    
    print(f"Tentativas restantes: {tentativas}")
    
    palpite1 = int(input("Adivinhe o primeiro número:(1-10) :"))
    palpite2 = int(input("Adivinhe o primeiro número:(1-10) :"))
    
    # se palpite for iqual ao numero secreto
    if palpite1 == numero_secreto1:
        print(f"Parabéns você acerto! - {palpite1}")
        adivinhou1 = True
        
    # se palpite for iqual ao numero secreto
    if palpite2 == numero_secreto2:
        print(f"Parabéns você acerto! - {palpite2}")
        adivinhou2 = True 
        
    # Se não adivinho exibe novamente    
    if not adivinhou1 or not adivinhou2:
        print("Tente novamente!")
        tentativas -=1 # reduzindo as tentavias restantes
    
    if adivinhou1 == True and adivinhou2 == True:
        print("Parabens você adinvinho ambos os números")
    else:
        print(f"Você não adivinhou os números - Eles eram: {numero_secreto1} e {numero_secreto2}")