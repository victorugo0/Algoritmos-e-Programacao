# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716






plano = str(input())

salario = float(input())

if plano == "A" :
    print("Novo salário: R$%.2f" %(salario * 1.10))

elif plano == "B" :
     print("Novo salário: R$%.2f" %(salario * 1.15))
     
elif plano == "C" :
     print("Novo salário: R$%.2f" %(salario * 1.20))
