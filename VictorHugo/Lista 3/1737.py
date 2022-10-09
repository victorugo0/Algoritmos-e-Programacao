# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

qtd = int(input())
soma_num = 0

if qtd <= 0:
    print("Informe uma quantidade > 0!")
else:
    while qtd > 0:
        num = float(input())
        qtd = qtd - 1
        soma_num = soma_num + num
    print("Soma dos números informados: %.2f" % soma_num)