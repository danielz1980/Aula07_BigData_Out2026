resposta = 'S'
META = 5000
vendedor = 0
bonus = 0
total_vendas = 0
total_bonus = 0

while resposta == 'S':
    vendedor = vendedor + 1
    valor_venda = float(input("\nInforme o valor de vendas do vendedor: R$ "))
    percent_meta = (valor_venda / META) * 100
    
    if percent_meta < 70:
        print(f"O vendedor {vendedor} não atingiu a meta de R$ {META}")
        print(f"O vendedor {vendedor} não tem direito a bônus")
    elif 70 <= percent_meta < 100:
        bonus = 200
        print(f"Percentual de atingimento da meta do vendedor {vendedor}: {percent_meta} %")
        print(f"Bônus do vendedor {vendedor}: R$ {bonus}")
    else:
        bonus = 500
        print(f"Percentual de atingimento da meta do vendedor {vendedor}: {percent_meta} %")
        print(f"Bônus do vendedor {vendedor}: R$ {bonus}")

    total_vendas = total_vendas + valor_venda
    total_bonus = total_bonus + bonus
    
    resposta = input("\nDeseja continuar? (S/N): ").upper()[0]

print(f'\nValor total de venda de todos os vendedores: R$ {total_vendas:.2f}')

print(f'\nValor total de bônus de todos os vendedores: R$ {total_bonus:.2f}')

print("\nPrograma encerrado")