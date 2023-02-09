#!/usr/bin/env python
# coding: utf-8

# Importando dados
import pandas as pd 
dados= pd.read_csv("C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/aluguel.csv", sep = ';')
dados.head(5)

# Selecionando bairros
bairros = ['Copacabana','Ipanema','Barra da Tijuca','Leblon','Botafogo','Flamengo','Tijuca']

selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]

dados['Bairro'].drop_duplicates()

# Agrupando dados por Bairro
grupo_bairro = dados.groupby('Bairro')

for bairros, info in grupo_bairro:
    print(bairros)

# Valor médio do Aluguel por bairro
for bairros, info in grupo_bairro:
    print('{} ->{}'.format(bairros,dados['Valor'].mean()))


grupo_bairro['Valor','Condominio'].mean().round(2)


# # Estastíticas Descritivas

grupo_bairro['Valor'].describe().round(2)


grupo_bairro['Valor'].aggregate(['min', 'max','sum'])


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20, 10))


# ### Teremos um gráfico em barra, em que podemos identificar a variação atípica no bairro "Botafogo". 

fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')
fig.set_label('valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})


# # Frequências de Quartos


classes = [0, 2, 4, 6, 100]


quartos = pd.cut(dados['Quartos'],classes)


pd.value_counts(quartos)


labels = ['0 e 2 quartos',
          '3 e 4 quartos',
          '5 e 6 quartos',
          '7 quartos ou mais']

quartos = pd.cut(dados['Quartos'], classes, labels = labels)
freq_quartos = pd.value_counts(quartos)


tabela = pd.DataFrame(freq_quartos)


tabela.sort_values(by = 'Quartos', ascending = False)
tabela.columns.name = 'Faixa de Quartos'
tabela.sort_index(inplace=True)
tabela

