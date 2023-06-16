

import datetime
data_atual = datetime.date.today()

Calculo = -1

print("\n╔════════════════════════════════════════╗")
Dia = int(input("   Digite o DIA do seu Nascimento: "))
Mes = int(input("   Digite o MES do seu Nascimento: "))
Ano = int(input("   Digite o ANO do seu Nascimento: "))
print(  "╚════════════════════════════════════════╝")
SysDia = data_atual.day
SysMes = data_atual.month
SysAno = data_atual.year

print("\n══════════════════════════════════════════")
if SysMes >= Mes:
    if SysDia >= Dia:
        Calculo = SysAno - Ano               
        print("Voce tem {} anos!" .format(Calculo))
else:
    Calculo = SysAno - Ano -1
    print("Voce tem {} anos!" .format(Calculo))
print(  "══════════════════════════════════════════")



    



