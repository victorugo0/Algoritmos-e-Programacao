# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713




valorhora = float(input())

numhoras = float(input())

salariobruto = valorhora * numhoras

imposto = salariobruto * 0.11

inss = salariobruto * 0.08

sindicato = salariobruto * 0.05

liquido = (salariobruto - imposto) - inss - sindicato

print("\nSalário bruto: R$%.2f" %(salariobruto))

print("\nImposto: R$%.2f" %(imposto))

print("\nINSS: R$%.2f" %(inss))

print("\nSindicato: R$%.2f" %(sindicato))

print("\nLíquido: R$%.2f" %(liquido))