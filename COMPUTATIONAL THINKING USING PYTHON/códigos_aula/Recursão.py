#Recursão 

#somatório na matemática
#f(4) = 1 + 2 + 3 + 4 = 10
#f(5) = 1 + 2 + 3 + 4 + 5 = 15

#f(x) = f(x-1) + x
#(1,3,5,7,9)

#Exercicio 1 - somar uma lsita de números (sem recursão)

def somaNumeros(lista):
    soma = 0 
    for i in lista:
        soma += i
    return soma

#main
lista = [1, 3, 5, 7, 9]
print(f'Soma: {somaNumeros(lista)}')

#Função Recursiva
#somar o primeiro elemento da listsa - lista [0]
# e como com o restante da lista lista [1:] 

#(((1 + 3) + 5) + 7)+ 9
#(1 + (3+) (5 +) + (7 + 9))
#(1 + (3 + (5 + 16)))
#(1 + (3 + 21))
# (1 + 24)
#(25)

def somarRecursivo(lista):
    if len(lista) == 1: #caso base
        return lista [0]
    else:
        return lista[0] + somarRecursivo(lista[1:])
 
#teste
print(f'Soma: {somarRecursivo(lista)}')