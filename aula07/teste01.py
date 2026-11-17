somatorio_vendas = 0

for i in range(5):
    print(f"\n{i+1}ª Venda")
    valor_venda = float(input("Digite o valor da venda: "))
    if valor_venda < 200:
        print("Valor da venda sem direito a desconto.")
        print(f"Valor da venda: R$ {valor_venda:.2f}")
        somatorio_vendas = somatorio_vendas + valor_venda
    else:
        print("Valor da venda com direito a 10% de desconto.")
        desconto = valor_venda * 0.10
        valor_venda = valor_venda * 0.90
        print(f"Valor da venda: R$ {valor_venda:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        somatorio_vendas = somatorio_vendas + valor_venda

print(f"\nSomatório das vendas: R$ {somatorio_vendas:.2f}")