sanidade = 100
exploracao = 0

def verStatus():
    while True:
        ver_status = input("Quer ver seus status? ").capitalize()
        if ver_status == "Sim":
            print(sanidade, exploracao)
            break
        if ver_status == "Não" or ver_status == "Nao":
            print("...")
            break
        else:
            print("Não entendi...")