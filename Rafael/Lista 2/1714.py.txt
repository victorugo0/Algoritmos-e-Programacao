# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714







precprod = float(input())

menor = precprod * 1.45

maior = precprod * 1.30

if precprod < 20 :
    print("\nValor de venda: R$%.2f" %(menor))
else:
    print("\nValor de venda: R$%.2f" %(maior))