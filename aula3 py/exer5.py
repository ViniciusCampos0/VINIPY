idade = int(input("Qual a sua idade? "))

if idade >=5 and idade <=7:
    print("Infatil A")

elif idade >=8 and idade <=11:
    print("Infantil B")

elif idade >=12 and idade <=13:
    print("Juvenil A")

elif idade >=14 and idade <=17:
    print("Juvenil B")

elif idade <5:
    print("Digite um valor igual ou superior a 5")
    
else:
    print("Maior da idade!")

