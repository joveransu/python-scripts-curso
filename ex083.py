#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = input('Digite uma expressão: ').strip()

continuar = False
if expression.count('(') == expression.count(')'):
    if expression.find('(') < expression.find(')'):
        for i, v in enumerate(expression):
            check = i
            if v == '(':
                while check < len(expression):
                    if expression[check] == ')':
                        continuar = True
                        break
                    check += 1 

        if continuar:
            print(f' A expressão {expression} é válida.')   
        else:
            print(f' A expressão {expression} não é válida.')          
    else:
        print(f' A expressão {expression} não é válida.')
else:
    print(f' A expressão {expression} não é válida.')

#Professor

expression = input('Digite uma expressão: ').strip()
pilha = []
for simb in expression:
    if simb == '(':
        pilha.append
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f' A expressão {expression} é válida.')   
else:
    print(f' A expressão {expression} não é válida.')  