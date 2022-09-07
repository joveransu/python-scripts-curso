#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: '))
frase = frase.replace(' ', '')
invertido = frase[::-1]
pale = True
for c in range(0, len(frase)):
    if frase[c].upper() != invertido[c].upper():
        pale = False
if pale:
    print('Frase é palindromo')
else:
    print('Frase NÃO é palindromo')

#metodo dois

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
invertido = frase[::-1]
print(frase, invertido)
if frase == invertido:
    print('Frase é palindromo')
else: 
    print('Frase NÃO é palindromo')