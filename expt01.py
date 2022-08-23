#Neste programa vou fazer com que o laço while verifique se o número digitado pelo usuário possui números adjacentes (Números repetidos):

#Criando entrada de dados e uma variavel booleana:
n = int(input("Digite um número inteiro: "))
cond = True

#Criando o laço de repetição para fazer o calculo e verificar se bate com as condicionais determinadas abaixo:
while cond:
    num1 = n % 10
    n = n // 10
    num2 = n % 10
    if n == 0:
        print("não")
        cond = False
    else:
        if num1 == num2:
            print("sim")
            cond = False
#Fim-se :D