resposta = 'S'
META = 2000
soma = 0
vendedor = 1

while resposta == 'S':
    valor_venda = float(input("\nInforme o valor de vendas do vendedor: R$ "))
    soma = valor_venda + soma
    if valor_venda < META:
        print(f"O vendedor {vendedor} não atingiu a meta de R$ {META}")
    else:
        percent_meta = (valor_venda / META) * 100
        print(f"Percentual de atingimento da meta do vendedor {vendedor}: {percent_meta} %")
    resposta = input("\nDeseja continuar? (S/N): ").upper()[0]

print(f'\nSomatório de venda de todos os vendedores: R$ {soma:.2f}')

print("\nPrograma encerrado")