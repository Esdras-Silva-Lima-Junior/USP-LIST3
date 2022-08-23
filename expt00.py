#Neste programa irei fazer um calculo para saber se o número digitado pelo usuário é primo ou não, para isso usei laços de repetição e if para condicionais:

#Criando variaveis, variaveis booleanas e entradas de dados:
n = int(input("Digite um número inteiro: "))
cond = True
i = 2

#Criando um laço de repetição para fazer o calculo até que alguma das condicionais seja atendidas:
while cond:
    calc = n % i
    if n == 2:
        print("primo")
        cond = False
    else:
        if (i >= n) and not (n < i):
            print("primo")
            cond = False
        else:
            if ((n % i) == 0) or n < i:
                print("não primo")
                cond = False
            else:
                i = i + 1
#Fim-se :D