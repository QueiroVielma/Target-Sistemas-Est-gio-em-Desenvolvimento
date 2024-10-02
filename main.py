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
