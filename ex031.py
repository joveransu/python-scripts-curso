#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando 0.50 por Km para viagens ate 200Km e 0.45 por viagens mais longas

dis = int(input('Qual a distância da viagem? '))
if dis <= 200:
    print('O preço será R$ {:.2f}'.format(dis*0.50))
else:
    print('O preço será R$ {:.2f}'.format(dis*0.45))

# preco = dis * 0.50 if dis <= 200 else preco = dis * 0.45
# print('O preço será R$ {:.2f}'.format(preco))
