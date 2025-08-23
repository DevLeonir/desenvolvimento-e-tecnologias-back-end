medias = []
nomes = []

x = int(input("Digite a quantidade de alunos: "))
for i in range(x):
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a 1ª"))
    n2 = float(input("Digite a 2ª"))
    media = (n1 + n2) / 2
    medias.append(media)
    nomes.append(nome)

n = int(input("Digite o nº do aluno que deseja exibir: "))
if medias[n] >= 6.0:
    print("O aluno %s foi APROVADO com média %.2f" %(nomes[n], medias[n]))
else:
    print("O aluno %s foi REPROVADO com média %.2f" %(nomes[n], medias[n]))