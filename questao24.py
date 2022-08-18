from datetime import datetime

#data de partida
d1 = datetime.strptime('2002-01-14', '%Y-%m-%d')

#data de chegada
d2 = datetime.strptime('2022-08-17', '%Y-%m-%d')


#quantidade de dias
dias_totais = abs((d2 - d1).days)
print (dias_totais) 
