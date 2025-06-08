# Importação das bibliotecas Matplotlib, Pandas, Numpy e Matplot3d para organizar e visualizar os dados gerados pelo script, além da biblioteca Decimal para realizar os calculos com exatidão de casas decimais
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits import mplot3d
from decimal import Decimal

# variáveis de cor para estilização#
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
REVERSE = "\033[m"

lista_eixo_x = []
lista_eixo_y = []
lista_eixo_z = []
#Input de variaveis utilizadas para o calculo das variaveis do processo, e tratamento de erros#
while True:
    try:
        massa_entrada_gasosa_fundo = Decimal(input('Insira a vazão de efluente a ser tratado em kg/h: '))
        break

    except Exception:
        print("Valor inválido, por favor insira apenas números inteiros ou com ponto flutuante")
        
while True:
    try:
        fração_acido_entrada_fundo = Decimal(input('Insira a fração de ácido no efluente: '))
        break
    except Exception:
        print("Valor inválido, por favor insira apenas números inteiros ou com ponto flutuante")
        
while True:
    try:
        fração_acido_saida_topo = Decimal(input('Insira a fração de acido no efluente tratado: '))
        break
    except Exception:
        print("Valor inválido, por favor insira apenas números inteiros ou com ponto flutuante")

while True:
    try:
        massa_saida_aquosa_fundo = Decimal(input('Insira a vazão de efluente aquoso em kg/h: '))
        break
    except Exception:
        print("Valor inválido, por favor insira apenas números inteiros ou com ponto flutuante")

while True:
    try:
        quantidade_de_tempo = int(input('Insira por quanto tempo quer projetar o processo? '))
        break
    except Exception:
        print("Valor inválido, por favor insira um número inteiro.")
        
#Loop While utilizado para repetir os inputs até que uma opção correta seja inserida
while True:
    unidade_de_tempo = str(input(f'\nInforme a medida utilizada'
                             f'\n{GREEN}[h]{REVERSE} para horas'
                             f'\n{BLUE}[d]{REVERSE} para dias'
                             f'\n{CYAN}[m]{REVERSE} para meses'
                             f'\n{RED}[a]{REVERSE} para anos: ').lower().split(" "))

    if unidade_de_tempo not in "hdma":
        print( f'{RED}Valor inválido!!!{REVERSE}')

    else:
        while True:
            conversão = str(input(f'Manter a medida{CYAN}[1]{REVERSE}'
                      f'\nConverter a medida {GREEN}[2]{REVERSE}: ').split(" "))

            if conversão not in "12":
                print( f'{RED}Valor inválido!!!{REVERSE}')
            else:
                break
        break

while True:

    if conversão == "1":
        unidade_de_tempo = unidade_de_tempo
        break

    elif conversão == "2" and unidade_de_tempo == "h":
        quantidade_de_tempo = 60 * quantidade_de_tempo
        unidade_de_tempo = 'min'
        break

    elif conversão == "2" and unidade_de_tempo == 'd':
        unidade_de_tempo = str(input(f'Converter para horas{RED}(h){REVERSE}'
                                 f'\nConverter para minutos{CYAN}(min): ').lower().split(" "))

        if unidade_de_tempo == "h":
            quantidade_de_tempo = quantidade_de_tempo * 24
            break

        elif unidade_de_tempo == "min":
            quantidade_de_tempo = quantidade_de_tempo * 1440
            break

        else:
            print( f'{RED}Valor inválido!!!{REVERSE}')

    elif conversão == "2" and unidade_de_tempo == 'm':
        unidade_de_tempo = str(input(f'Converter para dias{RED}[d]{REVERSE}'
                                 f'\nConverter para horas{CYAN}[h]').lower().split(" "))
        if unidade_de_tempo == 'd':
            quantidade_de_tempo *= 30
            break

        elif unidade_de_tempo == 'h':
            quantidade_de_tempo *= 24 * 30
            break

        else:
            print( f'{RED}Valor inválido!!!{REVERSE}')

    else:
        unidade_de_tempo = str(input(f'Converter para meses {GREEN}[m]{REVERSE}'
                                 f'\nConverter para dias {BLUE}[d]').lower().split(" "))
        if unidade_de_tempo == "m":
            quantidade_de_tempo *= 12
            break

        elif unidade_de_tempo == "d":
            quantidade_de_tempo *= 12 * 30
            break

        else:
            print(f'{RED}Valor inválido!!!{REVERSE}')

if unidade_de_tempo == "h":
    massa_entrada_gasosa_fundo = massa_entrada_gasosa_fundo
    massa_saida_aquosa_fundo = massa_saida_aquosa_fundo

elif unidade_de_tempo == "min":
    massa_entrada_gasosa_fundo /= 60
    massa_saida_aquosa_fundo /= 60

elif unidade_de_tempo == "d":
    massa_entrada_gasosa_fundo *= 24
    massa_saida_aquosa_fundo *= 24

elif unidade_de_tempo == "m":
    massa_entrada_gasosa_fundo *= 24 * 30
    massa_saida_aquosa_fundo *= 24 * 30

else:
    massa_entrada_gasosa_fundo *= 24 * 30 * 12
    massa_saida_aquosa_fundo *= 24 * 30 * 12
#calculo utilizado para obter as variaveis desejadas do processo
fração_ar_entrada_fundo = 1 - fração_acido_entrada_fundo
fração_ar_saida_topo = 1 - fração_acido_saida_topo
massa_de_acido_entrada_fundo = fração_acido_entrada_fundo * massa_entrada_gasosa_fundo
massa_de_ar = fração_ar_entrada_fundo * massa_entrada_gasosa_fundo
massa_de_acido_saida_topo = (massa_de_ar * fração_acido_saida_topo) / (fração_ar_saida_topo)
massa_de_acido_saida_fundo = massa_de_acido_entrada_fundo - massa_de_acido_saida_topo
fração_de_acido_saida_fundo = (massa_de_acido_saida_fundo / massa_saida_aquosa_fundo)
fração_de_agua_saida_fundo = 1 - fração_de_acido_saida_fundo
massa_de_agua = fração_de_agua_saida_fundo * massa_saida_aquosa_fundo
massa_de_saida_topo = massa_de_acido_saida_topo + massa_de_ar
#Sessões de código utilizadas para escolher cada eixo do gráfico
while True:
    eixo_x = str(input(f"\n{REVERSE}Qual o eixo x do gráfico?"
                   f"\n{RED}[1]{REVERSE} Vazão de entrada do efluente gasoso"
                   f"\n{GREEN}[2]{REVERSE} Vazão de entrada de água pura"
                   f"\n{CYAN}[3]{REVERSE} Vazão de saida de gás tratado"
                   f"\n{BLUE}[4]{REVERSE} Vazão de saida de efluente aquoso: ").split(" "))

    if eixo_x not in "1234":
        print(f'{RED}Valor inválido!!!{REVERSE}')
    else:
        break

if eixo_x == 1:
    massa_x = massa_entrada_gasosa_fundo
    nome_x = 'efluente gasoso'

elif eixo_x == 2:
    massa_x = massa_de_agua
    nome_x = 'água pura'

elif eixo_x == 3:
    massa_x = massa_de_saida_topo
    nome_x = 'gás tratado'

elif eixo_x == 4:
    massa_x = massa_saida_aquosa_fundo
    nome_x = 'efluente aquoso'

while True:
    eixo_y = str(input("\nQual o eixo y do gráfico?"
                   f"\n{RED}[1]{REVERSE} Vazão de entrada do efluente gasoso"
                   f"\n{GREEN}[2]{REVERSE} Vazão de entrada de água pura"
                   f"\n{CYAN}[3]{REVERSE} Vazão de saida de gás tratado"
                   f"\n{BLUE}[4]{REVERSE} Vazão de saida de efluente aquoso: ").split(" "))

    if eixo_y not in '1234':
        print(f'{RED}Valor inválido!!!{REVERSE}')
    else:
        break

if eixo_y == "1":
    massa_y = massa_entrada_gasosa_fundo
    nome_y = 'efluente gasoso'

elif eixo_y == "2":
    massa_y = massa_de_agua
    nome_y = 'água pura'

elif eixo_y == "3":
    massa_y = massa_de_saida_topo
    nome_y = 'gás tratado'

else:
    massa_y = massa_saida_aquosa_fundo
    nome_y = 'efluente aquoso'

while True:
    eixo_z = str(input("\nQual o eixo z do gráfico?"
                       f"\n{RED}[1]{REVERSE} Vazão de entrada do efluente gasoso"
                       f"\n{GREEN}[2]{REVERSE} Vazão de entrada de água pura"
                       f"\n{CYAN}[3]{REVERSE} Vazão de saida de gás tratado"
                       f"\n{BLUE}[4]{REVERSE} Vazão de saida de efluente aquoso: ").split(" "))

    if eixo_y not in '1234':
        print(f'{RED}Valor inválido!!!{REVERSE}')
    else:
        break

if eixo_z == "1":
    massa_z = massa_entrada_gasosa_fundo
    nome_z = 'efluente gasoso'

elif eixo_z == "2":
    massa_z = massa_de_agua
    nome_z = 'água pura'

elif eixo_z == "3":
    massa_z = massa_de_saida_topo
    nome_z = 'gás tratado'

else:
    massa_z = massa_saida_aquosa_fundo
    nome_z = 'efluente aquoso'

tempo = []
count = 0
#Aqui é onde os valores são anexados em sua respectiva lista do gráfico...
# ...e convertidas em notação cientifica se os valores forem maiores que 1000
while True:
    count += 1
    tempo.append(count)

    massa_x_convertida = count * massa_x
    massa_y_convertida = count * massa_y
    massa_z_convertida = count * massa_z

    lista_eixo_x.append(massa_x_convertida)
    lista_eixo_y.append(massa_y_convertida)
    lista_eixo_z.append(massa_z_convertida)

    if count == quantidade_de_tempo:
        break
#dicionario utilizado para criar um dataframe com o Pandas
print( "\n " )
#dataframe salvo em arquivo.csv com informação da quantidade e unidade de tempo#
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(lista_eixo_x, lista_eixo_y, lista_eixo_z, 'red')
ax.set_xlabel(f'Vazão de {nome_x} em kg', fontsize=12)
ax.set_ylabel(f'Vazão de {nome_y} em kg', fontsize=12)
ax.set_zlabel(f'Vazão de {nome_z} em kg', fontsize=12)
ax.scatter3D(lista_eixo_x, lista_eixo_y, lista_eixo_z, c=(lista_eixo_z), cmap='cividis')
plt.show()
# etapa necessária pra transformar os decimais em notação cientifíca para melhor visualização na tabela...#
lista_eixo_x = [np.format_float_scientific(massax, precision=3, exp_digits=1) for massax in lista_eixo_x]
lista_eixo_y = [np.format_float_scientific(massay, precision=3, exp_digits=1) for massay in lista_eixo_y]
lista_eixo_z = [np.format_float_scientific(massaz, precision=3, exp_digits=1) for massaz in lista_eixo_z]
#Plotagem do gráfico 3d#
tabela = {f'Vazão de {nome_x} kg': lista_eixo_x,
          f'Vazão de {nome_y} kg': lista_eixo_y,
          f'Vazão de {nome_z} kg': lista_eixo_z,
          f'Tempo em {unidade_de_tempo}': tempo}
pd.set_option('display.max_rows', 22000)
pd.set_option('display.max_columns', 4)
pd.set_option('display.expand_frame_repr', False)
tabela_de_vazoes = pd.DataFrame(tabela)
print(tabela_de_vazoes)
tabela_de_vazoes.to_csv(f'{massa_de_acido_entrada_fundo}{massa_de_agua}.csv')

