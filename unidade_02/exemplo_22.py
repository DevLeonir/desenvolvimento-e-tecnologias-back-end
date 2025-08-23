def calculaArea(base, altura):
    area = base * altura / 2
    return area

base = float(input("Digite a base do triângulo em cm: "))
altura = float(input("Digite a altura do triângulo em cm: "))

print("A área do triângulo é %.2f cm²"%calculaArea(base, altura))
print("Um método pode ser utilizado quantas vezes for necessário!!")
print(calculaArea(8, 5))
print(calculaArea(10, 10))
print(calculaArea(2, 5))