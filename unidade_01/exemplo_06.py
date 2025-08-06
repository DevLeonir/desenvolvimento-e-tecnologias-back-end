import math

raio = float(input("Digite o raio da circuferência em cm: "))
comprimento = 2 * math.pi * raio
area = math.pi * raio * raio

print("O comprimento da circuferência é igual a %.2f cm" % (comprimento))
print("A área da circuferência é igual a %.2f cm²" % (area))