
  # Resolvendo Problemas de Engenharia de Processos com Python

É um script escrito em Python, que resolve o problema abaixo e permite que sejam gerados tabelas e gráficos que exibem as vazões de cada susbtancia consumida e gerada ao longo do tempo, definido pelo usuário.

Uma indústria precisa tratar seu efluente gasoso que está contaminado com ácido sulfúrico. Para tratar 500 kg/h de um efluente que possui 30% em massa do ácido em ar atmosférico, a indústria dispõe de uma coluna de lavagem de gases. O efluente gasoso deve sair da coluna como uma concentração de no máximo 1% de ácido. Para tanto se usa uma corrente em contracorrente de água pura. 2000kg/h segue para uma ETE, antes do descarte final. Calcule, para estas condições, a vazão de água pura, a vazão do efluente gasoso e a fração em massa de ácido no rejeito líquido.(Problema apresentado pelo professor Andrey Oliveira de Souza


## 🚀 Começando

### 📋 Pré-requisitos


```
- Python3
- Pip(Se rodar o cógigo em um ambiente venv no Python)
- Bibliotecas do repositório de pacotes do Python: MatPlotlib, Pandas, NumPy, decimal, tkinter, pathlib
- Terminal de comandos ou IDE(Pycharm, VsCode entre outros)
```

### 🔧 Instalação


Abra o terminal do seu Sistema Operacional com git instalado e clone o repositório do projeto:

```
    git clone https://github.com/Kagimon/ProcessoUnitarioLavagemResiduoAcido
```

 Instale todas as bibliotecas necessárias 
 
- Matplotlib - [https://www.w3schools.com/python/matplotlib_getting_started.asp](https://www.w3schools.com/python/matplotlib_getting_started.asp)
- Pandas - [https://www.w3schools.com/python/pandas/pandas_getting_started.asp](https://www.w3schools.com/python/pandas/pandas_getting_started.asp)
- Tkinter bult-in com o Python, mas pode estar ausente em alguns sistemas
-pip install tkinter-
        
### 🔩 Resultados do  código
Resolução do problema acima junto de um gráfico e tabela que representam 12 horas do processo(código executado no bash do linux mint)

![execução do código](https://github.com/Kagimon/ProcessoUnitarioLavagemResiduoAcido/blob/main/execucaodocodigo.png)


**DIRETORIOS CRIADOS PELO SCRIPT**
- O código cria diretórios nomeados pelas frações de ácido na entrada e na saída de efluente gasoso, e salva os DataFrames exportados como arquivos .csv nomeados com as vazões de entrada de efluente gasoso e saída de efluente aquoso e a quantidade de tempo do processo.

![https://github.com/Kagimon/ProcessoUnitarioLavagemResiduoAcido/blob/main/diretorio.png](https://github.com/Kagimon/ProcessoUnitarioLavagemResiduoAcido/blob/main/diretorio.png)

**Gráfico que representa o processo**
![https://github.com/Kagimon/ProcessoUnitarioLavagemResiduoAcido/blob/main/diretorio.png](https://github.com/Kagimon/ProcessoUnitarioLavagemResiduoAcido/blob/main/gr%C3%A1fico500.png)

## ✒️ Autores

* **Karlos Eduardo Ramos Albuquerque** - *desenvolvedor do projeto* - (https://github.com/Kagimon)

