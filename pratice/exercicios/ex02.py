'''
programa que calcula o dobro, o triplo e a raiz quadrada de um número
'''

n = int(input('Digite um número: '))

d = n * 2
t = n * 3
r = n ** (1/2)

print(f'O dobro de {n} é {d}, o triplo é {t} e a raiz quadrada é {r:.2f}.')