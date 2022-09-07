from cadastro.numeros import leiaInt
from cadastro.cores import get_color
from cadastro.textos import CenterLine
from cadastro.arquivos import *
from time import sleep


resetar = get_color()
amarelo = get_color("Amarelo")
azul = get_color("Azul")
vermelho = get_color("Vermelho")
verde = get_color('Verde')

main_menu = f"""
{CenterLine('MENU PRINCIPAL', 32, True)}
{amarelo}1{resetar} - {azul}Ver pessoas cadastradas.{resetar}
{amarelo}2{resetar} - {azul}Cadastrar novas pessoas.{resetar}
{amarelo}3{resetar} - {azul}Sair do sistema.{resetar}
{'=' * 32}
"""

arquivo = 'ansu.txt'
if existFile(arquivo):
    print(f'{verde}Arquivo {amarelo}"{arquivo}"{verde} foi encontrado.{resetar}')
else:
    print(f'{vermelho}Arquivo não foi encontrado, criando...{resetar}')
    createFile(arquivo)

sleep(1.5)

while True:
    print(main_menu)
    opcao = leiaInt(f'{amarelo}Sua opção: {resetar}')
    if opcao == 1:
        print(CenterLine('PESSOAS CADASTRADAS', 32, True))
        sleep(0.6)
        readFile(arquivo)
    elif opcao == 2:
        print(CenterLine('NOVO CADASTRO', 32, True))
        sleep(0.6)
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        insertPeople(arquivo, nome, idade)
    elif opcao == 3:
        print(CenterLine('Saindo do Sistema... Até Logo', 32, True))
        sleep(0.6)
        break
    else:
        print(f'{vermelho}ERRO: Digite uma opção válida.{resetar}')
    sleep(1)