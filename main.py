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
    'lanterna': "Lanterna 07-567",
    'algodao': "Algodão",
    'curativo': "Curativo",
}

san_constantes = (
    0, 3, 5, 7, 11, 17, 33
)

desc_constantes = (
    0, 4, 6, 8, 20
)

def user_stats(dimSanidade, descobrimento):
    print("ESTASTÍSTICAS")
    san = 100 - dimSanidade
    desc = 0 + descobrimento

    print(f"----Sua sanidade é de {san}----Sua porcentagem de descobrimento do local é de {desc}----")



#Funções de ações e eventos do jogo
#SÓ SERÃO CHAMADAS SE O LAÇO NO FIM DO CÓDIGO TIVER UMA CONFIRMAÇÃO PERANTE A PERGUNTA

#Função para a vizualização dos itens da bolsa,dependendo da resposta do usuário
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

#Localizações
def lugar_B():
    print()

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
                    print()
                    user_stats(san_constantes[2], desc_constantes[1])

            if esc_direcao == "2":
                lanterna = game_dict['lanterna']
                if lanterna in bolsa:
                    print()
                else:
                    print("Uma lanterna!!!!!")
                    bolsa.append(lanterna)
                    print("Você agora está visualizando a porta")
                    print()
                    viz_bolsa()
                    user_stats(san_constantes[0], desc_constantes[4])

                expl_ou_ava = input("Quer avançar além da porta ou quer continuar explorando a sala?\n (Digite A para avançar)-(Digite E para continuar explorando)").upper()
                print()
                algodao = game_dict['algodao']
                curativo = game_dict['curativo']
                if expl_ou_ava == "A" and algodao in bolsa:
                    print("Epa!Vai aonde sangrando desse jeito!")
                    print("Procure algo para estancar a sangria")
                if expl_ou_ava == "A" and algodao not in bolsa or curativo in bolsa:
                    lugar_B()
                    break
                elif expl_ou_ava == "E":
                    print("Continue explorando")
                else:
                    print("Não entendi...")

            if esc_direcao == "3":
                algodao = game_dict['algodao']
                if algodao in bolsa:
                    print("Você quer se F*D*R de novo???")
                else:
                    print("CUIDADO PRA NÃO SE CORTAR!!!!!!...")
                    print("O chão estava cheio de cacos de vidro, você deveria ter prestado mais atenção!")
                    print("Voce não vai conseguir prosseguir se não estancar essa m&rd@!")
                    print()
                    user_stats(san_constantes[1], desc_constantes[0])
                    print("Ufa, um algodão, mas não será suficiente")
                    bolsa.append(algodao)
                    print("Vamos, procure por um curativo ou algo do tipo agora")

            if esc_direcao == "4":
                algodao = game_dict['algodao']
                if algodao in bolsa:
                    print()
                    curativo = game_dict['curativo']
                    print("Ufa!Um curativo")
                    bolsa.append(curativo)
                else:
                    print("Uma bolsa com medicamentos, nada mais interessante no local...")

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