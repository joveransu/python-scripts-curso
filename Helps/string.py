#Fatiamento
frase = 'Curso em Video Python'
print(frase[9]) #Seleciona o caractere 9 = 'V'
print(frase[9:14]) #Seleciona toda parte da string do 9 ao 14, porém não inclui o 14 = 'Video'
print(frase[9:21:2]) #Seleciona a parte do 9 ao 21, porém mostrará numeros de 2 em 2 = 'VdoPto'
print(frase[:5]) #Seleciona o inicio da frase até o numero 5 = 'Curso' (representa 'frase[0:5]')
print(frase[15:]) #Seleciona do caractere 15 até o ultimo = 'Python' (representa 'frase[15:21]')
print(frase[9::3]) #Seleciona a frase do caractere 9 até o final pulando de 3 em 3 = 'VePh'

#Analise
print('=' * 15)
print(len(frase)) #Comprimento = 21
print(frase.count('o')) #Conta quantas caracteres 'o' tem na frase. = 3
print(frase.count('o',0,13)) #Conta quantas caracteres 'o' tem na frase fatiando ela. = 1
print(frase.find('deo')) #Mostra a caractere que começou o 'deo', caso contrário o valor será -1 = 11
print('Curso' in frase) #Retornar um valor bool se encontrar a palavra na frase
print(frase.replace('Python', 'Android')) #Troca as caracteres/Palavras = 'Curso em Video Android'
print(frase.upper()) #Deixa tudo maiusculo = 'CURSO EM VIDEO PYTHON'
print(frase.lower()) #Deixa tudo minusculo = 'curso em video python'
print(frase.capitalize()) #Deixa so a primeira letra maiuscula = 'Curso em video python'
print(frase.title()) #Deixa todas palavras com a primeira caractere maiuscula = 'Curso Em Video Python'
frase2 = '   Espaços no começo e fim   '
print(frase2.strip()) #Remove todos espaços no começo e fim da string = 'Espaços no começo e fim'
print(frase2.rstrip()) #Remove todos espaços no fim da string = '   Espaços no começo e fim'
print(frase2.lstrip()) #Remove todos espaços no começo da string = 'Espaços no começo e fim   '

#Divisão
print('=' * 15)
print(frase.split()) #Retorna uma lista(tabela) com todas palavras da string = '['Curso', 'em', 'Video', 'Python']'

#Junção
print('=' * 15)
print('-'.join(frase)) #Mostra todos caracteres separados com o simbolo colocado = 'C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n'
frase2 = frase.split() #Preparando uma varialvel para usar abaixo
print('-'.join(frase2)) #Junta todas as palavras de frase2 e coloca um - entre elas = 'Curso-em-Video-Python'

#Melhorias
print("""Isso aqui server para mostrar
na tela um texto longo, e quebrado 
por várias linhas, ele engloba tudo.""")#Print melhorada

print(frase.upper().count('O'))#Funções que podem ser usadas juntas com outras

print(frase.lower().find('v'))

frase2 = frase.replace('Python', 'Games') #Curso em Video Games
print(frase2)

frase2 = frase.split() #['Curso', 'em', 'Video', 'Python']
print(frase2[2][3]) # e

print('{:=^40}'.format('Ansu')) #Escrever '=' e 'Ansu' no espaço de 40 caracteres e ^ diz que a palavra 'Ansu' ficará no meio