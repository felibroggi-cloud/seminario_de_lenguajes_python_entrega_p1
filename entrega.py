import random

categorias = {
    "categoria_1": [
        "python",
        "programa",
        "variable",
        "funcion"
    ],
    "categoria_2": [
        "bucle",
        "cadena",
        "entero",
        "lista"
    ]
}

print("¡Bienvenido al Ahorcado!")
print()

print ("Categorias disponibles: ")
for i in categorias:
    print (f"  {i}")
print ()


# Comprobacion de si la categoria elegida coincide con las categorias existentes (si no, reintentar)
categoria_elegida_con_exito = False
while not categoria_elegida_con_exito:
    categoria_elegida = input ("Ingrese la categoria que guste: ")
    for i in categorias:
        if categoria_elegida == i:
            categoria_elegida_con_exito = True
            break
    if not categoria_elegida_con_exito:
        print ("Entrada invalida.")


# Declaro 'words' como la lista de todas las palabras de la categoria elegida en un orden aleatorio
cant_palabras = len(categorias[categoria_elegida])
words = random.sample(categorias[categoria_elegida], cant_palabras)

for word in words:
    guessed = []
    attempts = 6

    print ()    

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print(f"¡Ganaste!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        if len(letter) != 1 or letter < 'a' or letter > 'z':
            print ("Entrada invalida.")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
        
        print()

    else:
        print(f"¡Perdiste! La palabra era: '{word}'")
    
    print (f"Puntuacion: {attempts}.")
    print ()

    if word != words[cant_palabras - 1]:
        jugar_de_nuevo = input ("Queres jugar otra ronda? ")
        match jugar_de_nuevo:
            case "si" | "Si" | "sI" | "SI":
                print ("Iniciando nueva ronda")
            case _:
                break
    else:
        print ("Jugaste con todas las palabras de la categoria!")
enter = input ("Programa finalizado. Presione enter para cerrar.")