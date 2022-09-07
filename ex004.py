# var1 = input('Digite algo: ')
#print('É numerico? {}\nÉ decimal? {}\nÉ string? {}\nTipo: {}\nVariavel = {}\nÉ alfanumerico? {}\nEstá em maiuscula? {}\nEstá em minuscula? {}'
#.format(var1.isnumeric(), var1.isdecimal(), var1.isalpha(), type(var1), var1, var1.isalnum(), var1.isupper(), var1.islower()))

nome = input('Qual seu nome?: ')
print('Prazer em te conhecer {}!'.format(nome), end=' continuar linha ') #para continuar a linha
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
