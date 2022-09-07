def existFile(file):
    try:
        arquivo = open(file, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(file):
    try:
        arquivo = open(file, 'wt+')
        arquivo.close()
    except:
        print(f'\033[31mHouve um erro na criação de {file}.\033[m')
    else:
        print(f'\033[32mArquivo {file} foi criado com sucesso.\033[m')
        return arquivo


def readFile(file):
    try:
        arquivo = open(file, 'rt')
    except FileNotFoundError:
        print(f'\033[31mFalha ao ler o arquivo {file}.\033[m')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<15} {dado[1]:>5} anos')
    finally:
        arquivo.close()


def insertPeople(file, name='Desconhecido', years=0):
    try:
        arquivo = open(file, 'at')
    except:
        print(f'\033[31mHouve um erro na inserção no arquivo {file}.\033[m')
    else:
        try:
            arquivo.write(f'{name};{years}\n')
            print(f'\033[32mNovo registro de {name} adicionado.\033[m')
        except:
            print(f'\033[31mHouve um erro na inscrição de dados no {file}.\033[m')
    finally:
        arquivo.close()