#Este programa mostra o fatorial de um número

#Importando count para usalo:
from itertools import count

#Criando variaveis e entrada de dados:
number = int(input("Digite um número para descobrir seu fatorial: "))
result = 1
count = 1

#Criando um laço para fazer o calculo e imprimindo na tela o resultado
while count <= number:
    result = result * count
    count = count + 1
print(result)
#Fimse :D