placa = int(input("Digite os quatro dígitos da placa do veículo: "))

final = placa%10

if final == 1 or final == 2:
    print("o veículo não pode circular ás segundas-feiras")
elif final == 3 or final == 4:
    print("O veículo não pode circular ás terças-feiras")
elif final == 5 or final == 6:
    print("O veículo não pode circular ás quartas-feiras")
elif final == 7 or final == 8:
    print("O veículo não pode circular ás quintas-feiras")
else:
    print("O veículo não pode circular ás sextas-feiras")
