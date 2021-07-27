#LENDO ARQUIVO
'''handler = open('storyER.txt', 'r')
    print(handler.read())'''

#The main object

'''sanityLife = 50
class Player:


    def __init__(self, name, age):
        self.name = name
        self.age = age


priest = Player("Nicodemos", 35 )'''


#Lendo história
handler = open('storyER.txt', 'r')
print(handler.read())

#Começando o game em si
def beginningGame():
    print("Start")
    print("Wake up")
    print("Espace")
    import asciiStrg as pics

#Todos os eventos do jogo
def eventListeners():
    #EVENTS


#Os itens/objetos do jogo
def allItems():
    #itens









#Laço para começar ou não o jogo
while True:
    try:
        WantToStt = str(input("Want to start?('Yes' for start/ 'No' for exit)"))
        WantToStt = WantToStt.capitalize()
        if WantToStt == "Yes" or WantToStt == "Sim" or WantToStt == "Y" or WantToStt == "S" :
            beginningGame()
            break
        elif WantToStt == "No" or WantToStt == "Nao" or WantToStt == "N":
            print("GOODBYE")
            break
        else:
            print("Understand, type again")
    except:
        print("Undefined")
        break