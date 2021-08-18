#Atualizando valores
Largura = 200
Altura = 240

larguraChange = 0
alturaChange = 0


'''def atua_valores(larguraDim, comprimentoSoma):
    larguraAtual = Largura - larguraDim
    compAtual = Altura - comprimentoSoma
    print(larguraAtual, compAtual)

atua_valores(30, 60)'''

input1 = input("diga X: ")
input2 = input("diga Y: ")

if input1 == "X":
    larguraChange = Largura - 20
    alturaChange = Altura - 20
    print(larguraChange)
if input2 == "Y":
    larguraChange = Largura - 20
    alturaChange = Altura - 20


def fodasi():
    x = larguraChange + 45
    print(x)

fodasi()
