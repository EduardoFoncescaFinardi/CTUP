#Fatorial de n(recursivo)
#n!
#f(n)!

#n = 6
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
#teste
n = 1000
print(f'Soma: {fatorial(n)}')