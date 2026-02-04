'''
continuar = "s"
while continuar == "s":

    opcoes = int (input ("Escolha uma opção: \n [1] - Escolha um numero se e impar ou par \n [2] - Escolha 2 valores e diga quem e o maior entre eles ou se sao iguais \n [3] - Escolha um valor e calcule o dobro \n"))

    match opcoes :
        case 1:
            valor1 = int (input("Escolha o primeiro valor: "))
            if valor1 %2 == 0:
                print ("O valor e par")
            else:
                print ("O valor e impar")

        case 2:
            valor1 = int (input("Escolha o primeiro valor: "))
            valor2 = int (input("Escolha o segundo valor: "))
            if valor1 > valor2:
                print ("O primeiro valor e maior")
            elif valor1 < valor2:
                print ("O segundo numero e maior")
            else:
                print ("Os numeros sao iguais")

        case 3:
            valor1 = int (input("Escolha o primeiro valor: "))
            resultador_valor = valor1 * 2
            print (f"O valor do resultado e: {resultador_valor}")

        case _:
            print ("Opção incorreta")
    continuar = input ("Deseja continuar? (s/n)").lower().strip()
    ''''.lower() = deixa a letra maiuscula que o usuario digitou em minuscula .strip() = remove o espaço caso o usuario aperte sem querer''''
    if continuar != "s":
        print ("Programa Encerrado")
        break
        '''



nome = input("Nome: ")
while True:
    p1 = float(input("Prova 01 (0,0 e 10,0): ").replace (",", "."))
    if p1 >= 0.0 and p1 <= 10.0:
        break
    else:
        print ("Nota Invalida! Digite um valor entre 0,0 e 10,0")
while True:
    p2 = float(input("Prova 01 (0,0 e 10,0): ").replace (",", "."))
    if p2 >= 0.0 and p2 <= 10.0:
        break
    else:
        print ("Nota Invalida! Digite um valor entre 0,0 e 10,0")
    
md = (p1+p2)/2
if md >= 7:
    resultado = "Aprovado"
elif md >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"\nNome: {nome}")
print(f"Prova 01: {p1}")
print(f"Prova 02: {p2}")
print(f"Média: {md:.1f}")
print(f"Resultado: {resultado}")

