import random # Importing random module

# Initialyze the variables
black_sheep = 4 # Initial number of blacksheep
white_sheep = 2 # Initial number of white sheep
maior_numero = 0 # Variable to store the largest number of sheep

# Defines the function to generate the number of sheep in the pasture
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
