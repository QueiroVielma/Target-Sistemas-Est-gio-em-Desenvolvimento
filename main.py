import math

def exercicio_fibonacci():
    entrada = int(input("Informe um número: "))

    if verifica(entrada):
        print(f"O número {entrada} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {entrada} NÃO pertence à sequência de Fibonacci.")

def pertence_fibonacci(num:int)-> bool:
    raiz = int(math.sqrt(num))
    return raiz * raiz == num  

def verifica(num:int)->bool:
    return pertence_fibonacci(5*num*num + 4) or pertence_fibonacci(5*num*num - 4)

def contar_letra_a(texto):
    contador = 0
    for caractere in texto:
        if caractere.lower() == 'a':
            contador += 1

    if contador > 0:
        print(f"A letra 'a' aparece {contador} vez(es) na string.")
    else:
        print("A letra 'a' não esta na string.")

def achar_a ():
    frase = "A Amazônia é uma área incrível."
    contar_letra_a(frase)

