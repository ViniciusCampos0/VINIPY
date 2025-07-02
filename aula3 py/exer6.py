numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))

operacao = input("\nEscolha a operação matemática!\n\nSoma (+)\nSubtração (-)\nMultiplicação (*)\nDivisão (/): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("A soma é:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("A subtração é:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("A multiplicação é:", resultado)

elif operacao == "/":
        resultado = numero1 / numero2
        print("A divisão é:", resultado)

else:
    print("Informe um valor válido")
