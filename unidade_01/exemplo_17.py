diarias = int(input("Digite a quantidade de diárias: "))
tipo = input("Digite o tipo de hospedagem: ")

if tipo == "s" or tipo == "S":
    print("Valor a pagar R$ %.2f" %(diarias * 255.5))
elif tipo == "d" or tipo == "D":
    print("Valor a pagar R$ %.2f" %(diarias * 305.5))
elif tipo == "t" or tipo == "T":
    print("Valor a pagar R$ %.2f" %(diarias * 360.5))
else:
    print("Tipo de hospedagem inválida!")