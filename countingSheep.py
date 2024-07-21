import random # Importa o modulo random

# Inicializa as variaveis
black_sheep = 4 # Numero inicial de ovelhas pretas
white_sheep = 2 # Numero inicial de ovelhas brancas
maior_numero = 0 # Variavel para armazenar o maior numero de ovelhas

# Define a funcao para gerar o numero de ovelhas no pasto
def ovelhas_no_pasto(min, ovelhas_max):
    return random.randint(min, ovelhas_max)

while True:
    num_aleatorio = ovelhas_no_pasto(6, 150)
    if num_aleatorio >= 150:
        break
    black_sheep += 2
    white_sheep += 1
    
    if black_sheep >= white_sheep:
        maior_numero = black_sheep
    else:
        maior_numero = white_sheep
    
    print(f"Brancas: {white_sheep}", f"Pretas: {black_sheep}", sep=" ** ")

print(maior_numero)