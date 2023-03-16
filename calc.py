print("Calculadora de Equação do 1° e 2° Grau em R.")
print("Respeitando o formato ax² + bx + c. ")
print("____________________________________")

while True:
    a = int(input("Defina o valor de a: "))
    b = int(input("Defina o valor de b: "))
    c = int(input("Defina o valor de c: "))
    delta = b ** 2 - 4*a*c
    xMais = -b + (delta ** 1/2) / 2*a
    xMenos = -b - (delta ** 1/2) / 2*a
    eqPrimeiro = -c/b

    if a > 0:
        if delta > 0:
            print("Delta > 0, logo, a equação possui 2 raízes reais.")
            print(f'Delta = {delta}')
            print(f'x1 = {xMais}')
            print(f'x2 = {xMenos}')
        elif delta == 0:
            print("Delta = 0, logo, a equação possui 1 raíz real.")
            print(f'Delta = {delta}')
            print(f'x1 = {xMais}')
        else:
            print("Delta < 0, logo a equação do 2° Grau não possui raiz real.")
            print(f'Delta = {delta}')

    if a == 0:
        print("Equação do 1° Grau, a = 0.")
        print(f'x = {eqPrimeiro}')

    continuar = input("Quer continuar? (s)im ou (n)ão? ")
    if continuar == "s":
        print("Ok!")
    elif continuar == "n":
        print("Obrigado por usar a minha calculadora.")
        print("Gabriel Costa.")
        input("Pressione a tecla ENTER para fechar: ")
        break
