# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = (input(""))
horas_extras = float(input())

salario_min = 1192.40
valor_hora_extra = 10.00

salario_hora_extra = horas_extras * valor_hora_extra
salario_bruto = 3 * salario_min + salario_hora_extra
if salario_bruto > 2000.00:
    inss = salario_bruto * 0.12
else:
    inss = salario_bruto * 0.05

if salario_bruto > 2500.00:
    imposto_renda = salario_bruto * 0.20
else:
    imposto_renda = salario_bruto

salario_liquido = salario_bruto - (inss + imposto_renda)

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" % salario_bruto)
print("Salário Líquido: R$%.2f" % salario_liquido)