# ----------  P R O T Ó T I P O  ----------//

print("O personagem acorda em um determindado espaço")

# primeira tomada de decisão

print()
print("Atordoado,o personagem se levanta e nota que está em um lugar escuro e com alguns ruídos")
print()
print("Os ruídos vêm de uma determinda porta")


def luz_on():
    if choice == 1:
        print("O personagem acende a luz e ver apenas um rápido vulto")


def open_door():
    if choice == 2:
        print("O personagem tenta abrir a porta, mas ela está trancada")

#exemplo de uma progressão após uma determinada decisão
def break_door():
    print("A porta não abre, o personagem precisa de algo para quebrar")
    tools_box = ['Mini-machado', 'Pé de cabra', 'Martelo']

    handler_loop2 = False
    while not handler_loop2:
            try:
                tool_choice = float(
                    input("Pense e escolha- 1 p/ o mini-machado, 2 p/ o pé de cabra e 3 p/ o martelo:: "))
                if tool_choice == 1:
                    print(f"O personagem escolheu o {tools_box[0]}")
                    print("Ele não conseguiu quebrar a porta")
                if tool_choice != 2:
                    while True:
                        print("Escolha novamente, você precisa de algo mais forte!")
                        tool_choice = float(
                            input("Pense e escolha- 1 p/ o mini-machado, 2 p/ o pé de cabra e 3 p/ o martelo:: "))
                        if tool_choice == 2:
                            print("Finalmente quebrou!")
                            break
                if tool_choice == 2:
                    print(f"O personagem escolheu o {tools_box[1]}")
                    print("Ele conseguiu quebrar a porta!!!!")
                    break
                if tool_choice == 3:
                    print(f"O personagem escolheu o {tools_box[2]}")
                    print("Ele não conseguiu quebrar a porta")
                else:
                    print("Escolha dentro dos valores estabelecidos")
            except:
                print("--ERRO--Sintaxe desconhecida pelo o jogo")

handler_loop1 = False
while not handler_loop1:
    try:
        choice = float(input(
            "Você quer ligar luz e ver ao seu redor:DIGITE 1 ou quer abrir a porta e ir atrás do ruído:DIGITE 2 \n"
            "ESCOLHA-- "))
        if choice == 1:
            luz_on()
            break
        if choice == 2:
            open_door()
            break_door()
            break
        else:
            print("Escolha dentro dos valores estabelecidos")
    except:
        print("--ERRO--Sintaxe desconhecida pelo o jogo")


