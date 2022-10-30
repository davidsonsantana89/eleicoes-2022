#!/usr/bin/env python
# coding: utf-8

# In[58]:


#importar as bibliotecas necessárias
import requests
import pandas as pd

# endereço de onde os dados serão obtidos
URL = 'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'

# atribuir os dados obtidos na variável resultado
resultado = requests.get(URL).json()

#criar um dicionário para armazenar os nomes dos candidatos,
#total de votos apurados e a porcentagem destes, respectivamente
dic_cand = {'candidato':[],
           'votos_apurados':[],
           '%_votos_apurados':[]}

#iterar sobre os dados obtidos e armazená-los no dicionário criado antes
for i in range(2):
    dic_cand['candidato'].append(resultado['cand'][i]['nm'])
    dic_cand['votos_apurados'].append(resultado['cand'][i]['vap'])
    dic_cand['%_votos_apurados'].append(resultado['cand'][i]['pvap'])

#criar um dataframe a partir do dicionário criado antes.
df = pd.DataFrame(dic_cand)

# exibir na tela os resultados
display(df[['candidato', '%_votos_apurados']])


# In[ ]:




