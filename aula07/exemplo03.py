while True:
    numero = int(input("\nDigite um número: "))
    
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f" Dobro: {dobro}")
    print(f" Triplo: {triplo}")
    print(f" Quadrado: {quadrado}")

    resposta = input("\nDeseja continuar [S/N] ? ").upper()[0]
    
    if resposta == "N":
        break