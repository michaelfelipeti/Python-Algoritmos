'''
4)sistema deve perguntar quantos cigarros a pessoa fuma por dia  e por quantos anos ela já fuma.
  Sabendo que cada cigarro se perde 10min de vida sistema deve calcular quantos dias de vida o fumente perderá
'''
fum_dia = int(input("Informe quantos cigarros fuma por dia: "))
anos_fum = int(input("A quantos anos já fuma?: "))
tot_fum = fum_dia * (anos_fum * 365)
dias_perdidos = tot_fum / 144
if tot_fum % 144 == 0:
    print("Você tem menos %.0d dias de Vida"%dias_perdidos)
elif tot_fum % 144 != 0:
    horas_perdidas = (tot_fum % 144) / 6
    print("Você tem menos %0.d dias e %0.d hora(s) de Vida"%(dias_perdidos,horas_perdidas))