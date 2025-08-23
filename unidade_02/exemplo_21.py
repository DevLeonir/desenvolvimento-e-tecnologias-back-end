def imc(peso, altura):
    res = peso / altura ** 2
    return(res)

def despedida():
    print("Obrigado por usar este programa!")
    print("Até logo!")

peso = float(input("Digite o peso da pessoa, em kg: "))
altura = float(input("Digite a estatura da pessoa, em m: "))
print("O IMC é ", imc(peso, altura), "kg/m")
despedida()