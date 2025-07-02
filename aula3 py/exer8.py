peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
calculo = peso / (altura ** 2)

if calculo < 17:
    print("Muito abaixo do peso")
elif 17 <= calculo < 18.5:
    print("Abaixo do peso")
elif 18.5 <= calculo < 25:
    print("Parabéns, peso ideal")
elif 25 <= calculo < 30:
    print("Acima do peso")
elif 30 <= calculo < 35:
    print("Obesidade grau 1")
elif 35 <= calculo < 40:
    print("Obesidade grau 2 (severa)")
elif calculo >= 40:
    print("Obesidade grau 3 (mórbida)")


print(f"Seu IMC é {calculo:.2f}")