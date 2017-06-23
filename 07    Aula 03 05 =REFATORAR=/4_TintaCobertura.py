area=int(input("Informe a área em m² a ser pintada: "))
ltinta = area // 18
if area % 18 !=0 :
    ltinta=ltinta+1
print("Serão Necessárias %d latas de tinta \n e o valor total será de R$: %d "%(ltinta,ltinta*80))