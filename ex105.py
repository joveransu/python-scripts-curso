#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)

def notas(*notas, sit=False):
    """
        -> Retorna um dicionario com o:
        #– Quantidade de notas
        #– A maior nota
        #– A menor nota
        #– A média da turma
        #– A situação (opcional)
    """
    alunos = dict()
    alunos['totnota'] = len(notas)
    alunos['maiornota'] = max(notas)
    alunos['menornota'] = min(notas)
    alunos['medias'] = sum(notas)/len(notas)
    if sit:
        if alunos['medias'] < 5:
            alunos['situacao'] = 'RUIM'
        elif alunos['medias'] < 7:
            alunos['situacao'] = 'RAZOAVEL'
        else:
            alunos['situacao'] = 'BOA'
    return alunos

print(notas(5.5, 9.5, 10, 6.5, sit=True))