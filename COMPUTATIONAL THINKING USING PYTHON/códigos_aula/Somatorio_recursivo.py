#Somatorio (recursivo)
def somatorio(n):
    if n == 1:
        return 1
    else:
        return n +somatorio(n-1)
    
#teste
n = 6
print(f'Soma: {somatorio(n)}')