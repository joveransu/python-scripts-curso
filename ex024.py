#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.

city = input('Diga uma cidade: ').strip()
print(city[:6].upper() == 'SANTO') #Não mostrou o meio de comparar, porém usou o mesmo.
city = city.split()
print(bool(city[0].upper().find('SANTO')+1))

