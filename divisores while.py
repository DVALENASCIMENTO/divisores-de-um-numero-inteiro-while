#Implemente um script em python de modo que o usuário informe um número e o programa imprima
# como resultado todos os divisores daquele número. Este exercício deve ser implementado
# utilizando o comando while.
# Autor: Diego Vale do Nascimento - 12/10/2022
#Divisores de 60: (1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60).

a = 1
n = int(input('Digite um número inteiro: '))
while a <= n:
    i = n % a
    a = a + 1
    if i == 0:
        print('{} '.format(a - 1), end='')

