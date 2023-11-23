salario = float(input('Digite seu salário: '))
opt = input('Deseja receber VT? (S ou N): ').upper()

if salario <= 1320 :
    inss = salario*0.075
    if opt == 'S':
        vt = salario*0.06
    else :
        vt = 0
    print(f'Sua alíquota é de 7,5%\n Desconto INSS: R${round(inss,2)}\n '
          f'Desconto VT: R$ {vt}\n Salário: R${round((salario - inss - vt),2)}')
elif 1320 < salario <= 2571.29 :
    inss = (1320*0.075) + ((salario - 1320)*0.09)
    if opt == 'S':
        vt = salario * 0.06
    else:
        vt = 0
    print(f'Sua alíquota é de 9%\n Desconto INSS: R${round(inss, 2)}\n '
          f'Desconto VT: R$ {vt}\n Salário: R${round((salario - inss - vt),2)}')
elif 2571.29 < salario <= 3856.94 :
    inss = (1320*0.075) + ((2571.29 - 1320)*0.09) + ((salario - 2571.29)*.012)
    if opt == 'S':
        vt = salario * 0.06
    else:
        vt = 0
    print(f'Sua alíquota é de 12%\n Desconto INSS: R${round(inss, 2)}\n '
          f'Desconto VT: R$ {vt}\n Salário: R${round((salario - inss - vt),2)}')
elif 3856.95 < salario <= 7507.49 :
    inss = (1320*0.075) + ((2571.29 - 1320)*0.09) + ((3856.94 - 2571.29)*.012) + ((salario - 3856.94)*.14)
    if opt == 'S':
        vt = salario * 0.06
    else:
        vt = 0
    print(f'Sua alíquota é de 14%\n Desconto INSS: R${round(inss, 2)}\n '
          f'Desconto VT: R$ {vt}\n Salário: R${round((salario - inss - vt),2)}')
else :
    inss = (1320 * 0.075) + ((2571.29 - 1320) * 0.09) + ((3856.94 - 2571.29) * .012) + ((7507.49 - 3856.94)*.14)
    if opt == 'S':
        vt = salario*0.06
    else :
        vt = 0
    print(f'Sua alíquota é de 14%\n Desconto INSS: R${round(inss, 2)}\n '
          f'Desconto VT: R$ {vt}\n Salário: R${round((salario - inss - vt), 2)}')

