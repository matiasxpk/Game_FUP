# EQUIPE:Francisco Matias Neto, Guilherme Frutuoso de Almeida, Ingrid Ferreira Gomes e Pedro Henrique Sousa Alcântara

# INIT

# Lendo arquivo com a história
handler = open(
    r'C:\Users\Usuario\Desktop\Python_Folder\MyProjects\FUP-AVA\Game_FUP\storyER.txt')
print(handler.read())
handler = open(
    r'C:\Users\Usuario\Desktop\Python_Folder\MyProjects\FUP-AVA\Game_FUP\storyER2.txt')
print(handler.read())
print()

#Variáveis bases para o andar do game
bolsa = []

game_dict = {
    'carta':"Hão de ser benditos, os tempos que não me lembro mais \n E os passos perdidos registr$%$%$%$%$%$%$$%$%$4",
    'lanterna': "Lanterna 07-567"
}

def user_stats(sanidade, descobrimento):
    print("ESTASTÍSTICAS")

#Funções de ações e eventos do jogo
#SÓ SERÃO CHAMADAS SE O LAÇO NO FIM DO CÓDIGO TIVER UMA CONFIRMAÇÃO PERANTE A PERGUNTA

def viz_bolsa():
    while True:
        pergunta = input("Quer vizualizar os itens da bolsa?('Sim ou Não')").capitalize()
        if pergunta == "Sim":
            print(bolsa)
            break
        elif pergunta == "Não":
            print(bolsa)
            break
        else:
            print("Não entendi...")

def lugar_A():
    print("SALA")
    print("A sala está escura, procure algo para realmente enxergar uma saída")

    while True:
        try:
            esc_direcao = input("Você quatro direções dentro do espaço para ir: Sul(1), Norte (2), Leste(3), Oeste(4)")
            if esc_direcao == "1":
                carta = game_dict['carta']
                if carta in bolsa:
                    print("Você já veio aqui, não há mais nada")
                else:
                    bolsa.append(carta)
                    print(game_dict['carta'])
                    viz_bolsa()
            if esc_direcao == "2":
                print("Uma lanterna!!!!!")
                lanterna = game_dict['lanterna']
                bolsa.append(lanterna)
                print("Você agora está visualizando a porta")
                expl_ou_ava = input("Quer avançar além da porta ou quer continuar explorando a sala?\n (Digite A para avançar)-(Digite E para continuar explorando)").upper()
                viz_bolsa()
                if expl_ou_ava == "A":
                    lugar_B()
                    break
                else:
                    print("Continue explorando")
            if esc_direcao == "3":
                print("CUIDADO PRA NÃO SE CORTAR!!!!!!...")
                print("O chão estava cheio de cacos de vidro, você deveria ter prestado mais atenção!")
                print("Voce não vai conseguir prosseguir se não estancar essa m&rd@!")
        except:
            print("Undefined")
#Função para iniciar o jogo,depois da resposta abaixo
def game_inicio():
    print("Acorde Padre!")
    print("...")
    import asciiStrg as pics
    lugar_A()

#Laço para começar ou não o jogo
while True:
    try:
        conf_user = str(
            input("Você realmente quer comerçar o jogo?('Sim' para começar/ 'Não' para sair) "))
        conf_user = conf_user.capitalize()
        if conf_user == "Sim" or conf_user == "S":
            game_inicio()
            break
        elif conf_user == "Não" or conf_user == "Nao" or conf_user == "N":
            print("GOODBYE")
            break
        else:
            print("Não entendi, digite novamente")
    except:
        print("Undefined")
        break
