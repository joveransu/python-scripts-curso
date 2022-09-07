#Avançando
for c in range(1,10):
    print(c)
print('-=' * 20)

#Com comandos dentro
for c in range(0,3):
    print('Ansu ',end='')
    print('Teste')
print('-=' * 20)

#Com condicionais
for c in range(0,3):
    if c == 2:
        print(c)
    print('Ansu ',end='')
    print('BOSS')
print('-=' * 20)

#Voltando
for c in range(7,0,-1):
    print(c)
print('-=' * 20)

#Pulando
for c in range(0,7,2):
    print(c)
print('-=' * 20)

#Digitando
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
inc = int(input('Digite o incremento: '))
for c in range(i, f+1, inc):
    print(c)

#Brincando
s = 0
for c in range(0,5):
    n = int(input('Digite um numero: '))
    s += n
print(s)