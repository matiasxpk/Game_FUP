# EQUIPE:Francisco Matias Neto, Guilherme Frutuoso de Almeida, Ingrid Ferreira Gomes e Pedro Henrique Sousa Alcântara

# INIT

from pyasciiStrg import asciiObj1
from pyasciiStrg import asciiObj2
from pyasciiStrg import asciiObj3
from pyasciiStrg import asciiObj4
from pyasciiStrg import asciiObj5
from pyasciiStrg import asciiObj6
from pyasciiStrg import asciiObj7

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

#Dicionário com itens do jogo
game_dict = {
    'carta':"Carta: Hão de ser benditos´çsç[sççs-0o4dl´´d",
    'lanterna': "Lanterna 07-567",
    'algodao': "Algodão",
    'curativo': "Curativo",
    'giz': "Giz",
    'chave': "Chave",
    'fotografia' : asciiObj7(),
}

#Constantes do jogo
san_constantes = (
    100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 2, 0
)

desc_constantes = (
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 100
)

#Definindo e apresentando os status do usuário
def verStatus(dimSanidade, aumExp):
    sanidadeAtual = dimSanidade
    expAtual = aumExp
    while True:
        pergunta = input("Quer ver seus status? ").capitalize()
        if pergunta == "Sim":
            print(f".: -=- Sua sanidade atual é de: {sanidadeAtual}\n"
                  f"Sua porcetagem de exploração é de: {expAtual}% -=- :.")
            break
        if pergunta == "Não" or pergunta == "Nao":
            print("...")
            break
        else:
            print("Não entendi...")
    if sanidadeAtual <= 0:
        print("GOODBYE")
        return

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
            break
        else:
            print("Não entendi...")

#Localizações

def lugar_lounge():
    print('lounge')

def lugar_corredor():
    print("CORREDOR")
    asciiObj3()
    print("Finalmente você saiu daquela sala escura,agora está na hora de buscar o caminho para o 'jardim'...")
    mngames_conc = 0
    while True:
        try:
            esc_direcao = input("Você quatro direções dentro do espaço para ir: Sul(S), Norte (N), Leste(L), Oeste(O)")
            if esc_direcao == "S":
                print("Vai retornar para aquela sala ?! faça o que quiser...")
                lugar_salaInicio()

            if esc_direcao == "N":
                esc_opc2 = input("Escolha uma dessas direções: Lounge(X), Minigame-Quadro(Y), Corredor(C)").upper()
                if esc_opc2 == "X":
                    if mngames_conc == 3:
                        lugar_lounge()
                    else:
                        print("Conclua os eventos da área antes de avamçar!")
                if esc_opc2 == "Y":
                    print("Um quadro...")
                    #MINIGAME
                    '''
                    Soon...
                    '''
                    x = input("MINIGAME: ")
                    if x == "MINIGAME":
                        mngames_conc += 1
                        if len(bolsa) == 3:
                            verStatus(san_constantes[1], desc_constantes[4])
                        elif len(bolsa) == 2 and game_dict['algodao'] not in bolsa:
                            verStatus(san_constantes[0], desc_constantes[3])
                        elif len(bolsa) == 2 and game_dict['algodao'] in bolsa:
                            verStatus(san_constantes[1], desc_constantes[3])
                        else:
                            verStatus(san_constantes[0], desc_constantes[2])
                if esc_opc2 == "C":
                    print("Retornando ao corredor...")

            if esc_direcao == "L":
                print("Que sala imensa, quantos momentos, quantas lembranças...")
                asciiObj6()
                while True:
                    esc_Sprincipal = input("Escolha uma dessas direções: Norte(N), Sul(S), Leste(L), Oeste(O)").upper()
                    if esc_Sprincipal == "N":
                        if game_dict['giz'] in bolsa:
                            print("Por aqui já está tudo feito.")
                        else:
                            print("Um quadro branco...")
                            print("Parece uma frase inacabada, tente descobrir o resto, talvez nos deixe mais perto do 'jardim'")
                            print("Do you remember when you said to me: ")
                            print("...")
                            enigma_mg = input("").capitalize()
                            if enigma_mg == "My friend,hope is a prison.":
                                mngames_conc += 1
                                print("É isto!Você consiguiu desvendar o enigma...e comprovar o quão triste estava sua amada")
                                print("Pegue seu giz de lembrança")
                                giz = game_dict['giz']
                                bolsa.append(giz)
                                print()
                                viz_bolsa()
                            if enigma_mg != "My friend,hope is a prison.":
                                print("Não é isso!Busque sinais pela a sala")
                    if esc_Sprincipal == "S":
                        print("Retornando ao corredor...")
                        break
                    if esc_Sprincipal == "L":
                        print("Uma televisão ligada!")
                        print("Há algo escrito em inglês na tela")
                        asciiObj7()
                        print("...")
                    if esc_Sprincipal == "O":
                        print("Uma poltrona com um livro sobre arquitetos")
                    else:
                        print()

            if esc_direcao == "O":
                print("O quarto de sua antiga amada. A cozinha está ao lado.")
                esc_opc4 = input("Escolha uma dessas direções: Cozinha(X), Quarto(Y),  Corredor(C)").upper()
                if esc_opc4 == "X":
                    print("COZINHA")
                    asciiObj4()
                    while True:
                        esc_Sprincipal = input(
                            "Escolha uma dessas direções: Norte(N), Sul(S), Leste(L), Oeste(O)").upper()
                        if esc_Sprincipal == "N":
                            print("A despensa da casa a esquerda e o fogção a direita")
                            esc_ramificacao = input("Escolha uma dessas direções: Fogão(F), Despensa(D)").upper()
                            if esc_ramificacao == "F":
                                print("Fogão")
                                print("Nada de valor por aqui")
                            if esc_ramificacao == "D":
                                print("Despensa")
                                esc_ramificacao = input("Escolha uma dessas direções: Patreleira(P), Cozinha(C)")
                                if esc_ramificacao == "P":
                                    if game_dict['chave'] in bolsa:
                                        print("Tudo vazio na patreleira")
                                    else:
                                        print("Uma pratelheira bem antiga")
                                        print("Uma chave!Pode ter alguma serventia...")
                                        chave = game_dict['chave']
                                        bolsa.append(chave)
                                        viz_bolsa()
                                if esc_ramificacao == "C":
                                    print("Retornando a cozinha")
                            else:
                                print("Não entendi...")
                        if esc_Sprincipal == "S":
                            print("Um jogo de vasilhas, não perca seu tempo por aqui!")
                        if esc_Sprincipal == "L":
                            esc_ramificacao = input("Escolha uma dessas direções: Armário(A), Geladeira(G), Corredor(C)").upper()
                            if esc_ramificacao == "A":
                                print("Esse armário foi presente seu!!!\n Há uma fotografia antiga nele")
                                fotografia = game_dict['fotografia']
                                bolsa.append(fotografia)
                                viz_bolsa()
                            if esc_ramificacao == "G":
                                print("Uma geladeira. Melhor! Mm estoque agridoce de remédios,pílulas e água\n Não perca seu tempo filho...")

                            if esc_ramificacao == "C":
                                print("Retornando ao corredor...")
                                break
                            else:
                                print("Não entendi")
                        if esc_Sprincipal == "O":
                            print()
                        else:
                            print()

                if esc_opc4 == "Y":
                    print("QUARTO DE DOLORES")
                    asciiObj5()

                if esc_opc4 == "C":
                    print("Retornando ao corredor...")
            else:
                print()
        except:
            print("Undefined")


def lugar_salaInicio():
    print("SALA DE ENTRADA")
    asciiObj2()
    print("A sala está escura, procure algo para realmente enxergar uma saída")

    while True:
        try:
            esc_direcao = input("Você quatro direções dentro do espaço para ir: Sul(S), Norte (N), Leste(L), Oeste(O)")

            if esc_direcao == "S":
                carta = game_dict['carta']
                if carta in bolsa:
                    print("Você já veio aqui, não há mais nada")
                else:
                    bolsa.append(carta)
                    print("Uma carta com água por cima...")
                    print(game_dict['carta'])
                    viz_bolsa()
                    print()
                    if game_dict['carta'] and (game_dict['algodao'] not in bolsa and game_dict['lanterna'] not in bolsa):
                        verStatus(san_constantes[0], desc_constantes[1])
                    if game_dict['lanterna'] in bolsa and game_dict['algodao'] in bolsa:
                        verStatus(san_constantes[1], desc_constantes[3])
                    elif (game_dict['lanterna'] in bolsa and not game_dict['algodao'] in bolsa) or (game_dict['algodao'] in bolsa and not game_dict['lanterna']in bolsa):
                        if game_dict['algodao'] in bolsa:
                            verStatus(san_constantes[1], desc_constantes[2])
                        else:
                            verStatus(san_constantes[0], desc_constantes[2])

            if esc_direcao == "N":
                lanterna = game_dict['lanterna']
                if lanterna in bolsa:
                    print()
                else:
                    print("Uma lanterna!!!!!")
                    bolsa.append(lanterna)
                    print("Você agora está visualizando a porta")
                    print()
                    viz_bolsa()
                    print()
                    if game_dict['lanterna'] and (game_dict['algodao'] not in bolsa and game_dict['carta'] not in bolsa):
                        verStatus(san_constantes[0], desc_constantes[1])
                    if game_dict['carta'] in bolsa and game_dict['algodao'] in bolsa:
                        verStatus(san_constantes[1], desc_constantes[3])
                    elif (game_dict['carta'] in bolsa and not game_dict['algodao'] in bolsa) or (game_dict['algodao'] in bolsa and not game_dict['carta']in bolsa):
                        if game_dict['algodao'] in bolsa:
                            verStatus(san_constantes[1], desc_constantes[2])
                        else:
                            verStatus(san_constantes[0], desc_constantes[2])

                expl_ou_ava = input("Quer avançar além da porta ou quer continuar explorando a sala?\n (Digite A para avançar)-(Digite E para continuar explorando)").upper()
                print()
                if expl_ou_ava == "A" and game_dict['algodao'] in bolsa and game_dict['curativo'] not in bolsa:
                    print("Epa!Vai aonde sangrando desse jeito!")
                    print("Procure algo para estancar a sangria")
                if expl_ou_ava == "A" and game_dict['algodao'] not in bolsa or game_dict['curativo'] in bolsa:
                    lugar_corredor()
                    break
                elif expl_ou_ava == "E":
                    print("Continue explorando")
                elif expl_ou_ava != "A" and expl_ou_ava != "E":
                    print("Não entendi...")

            if esc_direcao == "L":
                algodao = game_dict['algodao']
                if algodao in bolsa:
                    print("Você quer se F*D*R de novo???")
                else:
                    print("CUIDADO PRA NÃO SE CORTAR!!!!!!...")
                    print("O chão estava cheio de cacos de vidro, você deveria ter prestado mais atenção!")
                    print("Voce não vai conseguir prosseguir se não estancar essa m&rd@!")
                    print()
                    if game_dict['algodao'] and (game_dict['carta'] not in bolsa and game_dict['lanterna'] not in bolsa):
                        verStatus(san_constantes[1], desc_constantes[1])
                    if game_dict['lanterna'] in bolsa and game_dict['carta'] in bolsa:
                        verStatus(san_constantes[1], desc_constantes[3])
                    elif (game_dict['lanterna'] in bolsa and not game_dict['carta'] in bolsa) or (game_dict['carta'] in bolsa and not game_dict['lanterna']in bolsa):
                        if game_dict['carta'] in bolsa:
                            verStatus(san_constantes[1], desc_constantes[2])
                        else:
                            verStatus(san_constantes[0], desc_constantes[2])
                    print("Ufa, um algodão, mas não será suficiente")
                    bolsa.append(algodao)
                    print("Vamos, procure por um curativo ou algo do tipo agora")

            if esc_direcao == "O":
                algodao = game_dict['algodao']
                if algodao in bolsa:
                    print()
                    curativo = game_dict['curativo']
                    print("Ufa!Um curativo")
                    bolsa.append(curativo)
                else:
                    print("Uma bolsa com medicamentos, nada mais interessante no local...")
            else:
                print("Digite um dos valores citados")
        except:
            print("Undefined")

#Função para iniciar o jogo,depois da resposta abaixo
def game_inicio():
    print(".\n"
          ".\n"
          ".\n"
          "RESUMO E REGRAS:\n"
          "Seu personagem é composto com um SANIDADE que começa de 100 e pode zerar, o que consequentemente resulta em 'game-over'\n"
          "Ele também dispõe de uma PORCENTAGEM DE EXPLORAÇÃO,que aumenta quando você encotra itens e situações especifícas"
          f"Sua bolsa: {bolsa}"
          f"Seu status inicial: {san_constantes[0], desc_constantes[0]}")
    print()
    print("Acorde Padre!")
    print("...")
    asciiObj1()
    lugar_salaInicio()

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