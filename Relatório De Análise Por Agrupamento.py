#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
dados= pd.read_csv("C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/aluguel.csv", sep = ';')
dados.head(5)


# In[4]:


bairros = ['Copacabana','Ipanema','Barra da Tijuca','Leblon','Botafogo','Flamengo','Tijuca']

selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]
dados['Bairro'].drop_duplicates()


# In[5]:


grupo_bairro = dados.groupby('Bairro')

for bairros, info in grupo_bairro:
    print(bairros)


# In[ ]:





# In[8]:


for bairros, info in grupo_bairro:
    print('{} ->{}'.format(bairros,dados['Valor'].mean()))


# In[ ]:





# In[9]:


grupo_bairro['Valor','Condominio'].mean().round(2)


# # Estastíticas Descritivas

# In[10]:


grupo_bairro['Valor'].describe().round(2)


# In[11]:


grupo_bairro['Valor'].aggregate(['min', 'max','sum'])


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (20, 10))


# ### Teremos um gráfico em barra, em que podemos identificar a variação atípica no bairro "Botafogo". 

# In[13]:


fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')
fig.set_label('valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})


# # Frequências de Quartos

# In[14]:


classes = [0, 2, 4, 6, 100]


# In[15]:



quartos = pd.cut(dados['Quartos'],classes)


# In[16]:


pd.value_counts(quartos)


# In[17]:


labels = ['0 e 2 quartos',
          '3 e 4 quartos',
          '5 e 6 quartos',
          '7 quartos ou mais']


# In[18]:


quartos = pd.cut(dados['Quartos'], classes, labels = labels)
freq_quartos = pd.value_counts(quartos)


# In[19]:


tabela = pd.DataFrame(freq_quartos)


# In[20]:


tabela.sort_values(by = 'Quartos', ascending = False)
tabela.columns.name = 'Faixa de Quartos'
tabela.sort_index(inplace=True)
tabela

