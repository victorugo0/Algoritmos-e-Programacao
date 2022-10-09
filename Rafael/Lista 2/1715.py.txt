# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715






ccf = int(input(''))

valor = float(input())



if ccf == 1:
    print(f'Valor total a ser pago: R$%.2f' %(valor * 1.0))
    
elif ccf == 2:
    print(f'Valor total a ser pago: R$%.2f' %(valor * 0.87))
    
elif ccf == 3: 
    print(f'Valor total a ser pago: R$%.2f' %(valor * 0.93))

else:
    print("OPÇÃO INVÁLIDA!")