#Criei este programa "Descascar" o número digitado, pegando número por número e somando eles no final

#Aqui criei a entrada de dados e as variaveis necessarias para o funcionamento do programa:
n = int(input("Digite o número a ser somado: "))
s = 0
soma = 0

#Aqui criei um laço while para "Descascar" o número digitado e apagar o último número, após isso eu somei eles:
while n > 0:
    s = n % 10
    n = n // 10
    soma = soma + s
print(soma)
#Fim-se :D