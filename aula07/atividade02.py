contador = 1
soma = 0

while True:

    despesa = float(input(f"\nDigite um valor para a despesa {contador}: R$ "))
    soma = soma + despesa
    contador += 1
    
    resposta = input("\nDeseja continuar [S/N] ? ").upper()[0]
    if resposta == "N":
        break

print(f"\nQuantidade de despesas: {contador}")
print(f"\nSomatório das despesas: {soma}")

print("\nPrograma encerrado")