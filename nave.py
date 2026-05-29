##Definir as variáveis
combustivel = 110
tripulantes = []

## Definir funções

def viajar():
    ##aqui vamos gastar combustível
    global combustivel ##Avisa a função que a variável externa será modificada
    if(combustivel>=30):
        combustivel = combustivel - 30
        print("A nave viajou! 🚀")
    else:
        print("Você está sem combustível suficiente. Abasteça! 🆘")

def abastecer():
    global combustivel
    combustivel = 110
    print("Tanque cheio! ⛽")

def status_nave():
    #Mostre a quantidade de combustível e os tripulantes
    print("\n------ STATUS DA NAVE -----")
    print(f"Temos {combustivel} de combustível.")
    print(f"Os tripulantes são: {tripulantes}.")
    print("----------------------------------\n")

def registrarTripulante():
    novoTripulante= input("Qual o nome do novo tripulante?: ")
    tripulantes.append(novoTripulante)
    print("Tripulante inserido com sucesso! 🚀")

## Criar um menu

while True: ##esse loop roda para sempre!
    print("\nBem vindo ao menu interativo da nave. Por favor selecione uma opção:")
    print("\n1- Mostrar status da nave | 2 - Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Sair")
    opcao = input("Escolha: ")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()
    elif (opcao == "3"):
        abastecer()
    elif (opcao == "4"):
        registrarTripulante()
    elif (opcao == "5"):
        print("Viagem encerrada!")
        break











# status_nave()
# registrarTripulante()
# registrarTripulante()
# registrarTripulante()
# status_nave()
# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()