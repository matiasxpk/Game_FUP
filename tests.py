def verStatus(dimSanidade, aumExp):
    sanidadeAtual = dimSanidade
    expAtual = aumExp
    while True:
        pergunta = input("Quer ver seus status? ").capitalize()
        if pergunta == "Sim":
            print(f".: -=-Sua sanidade atual é de: {sanidadeAtual}\n"
                  f"Sua porcetagem de exploração é de: {expAtual}-=- :.")
            break
        if pergunta == "Não" or pergunta == "Nao":
            print("...")
            break
        else:
            print("Não entendi...")
    if sanidadeAtual <= 0:
        print("GOODBYE")
        return