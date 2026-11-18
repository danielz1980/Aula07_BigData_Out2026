# contador = 1
# while contador <= 10:
#     print(contador)
#     # contador = contador + 1
#     contador += 1  # equivalente a linha acima

contador = 1
soma = 0

while contador <= 5:
    n = float(input(f"Digite um valor para a posição {contador}: "))
    soma = soma + n
    print(f"Valor digitado para a posição {contador}: {n}")
    contador += 1
    print()

print(f"Somatório: {soma}")