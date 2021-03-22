#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import json


# In[13]:



## Funcções de Busca

    
def buscarecebendo2(ER,fraseFonte):
    y = re.search(ER, fraseFonte) #  search retorna a ocorrencias
    if(y): 
      print("Em \'", y.string, "\' foi encontrado: ", y.group())    # 
    else:
      return 0

def buscarecebendo(ER,fraseFonte):
    y = re.search(ER, fraseFonte) #  search retorna a ocorrencias
    if(y): 
      print( y.group())    # 
    else:
      return 0
      print("Não encontrado")

def buscarecebendoCaps(ER,fraseFonte):
    y = re.search(ER, fraseFonte) #  search retorna a ocorrencias
    if(y): 
      print( y.group().upper())    # 
    else:
      return 0
      print("Não encontrado")    


# In[14]:


## Teste de Leitura
# read file
with open('inscritos-form.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj=json.loads(data)
obj 


# # Processador de Inscritos numa atividade Desportiva

# Neste exercício pretende-se trabalhar com um arquivo desportivo criado por um Organizador de Provas de Orientação realizadas em diferentes locais e para diferentes graus de dificuldade adaptadas a diferentes classes de participantes.

# Construa, então, um ou vários programas Python para processar o ficheiro de texto 'inscritos.json' anexo1 conforme solicitado nas alíneas seguintes:
# 
# 
#     a) imprimir o nome (convertido para maiúsculas) de todos os concorrentes que se inscrevem como 'Individuais' e são de 'Valongo'.
#     b) imprimir o nome completo, o telemóvel e a prova em que está inscrito cada concorrente cujo nome seja 'Paulo' ou 'Ricardo', desde que seja da Vodafone.
#     c) imprimir toda a informação dos atletas da equipe "TURBULENTOS".
#     d) imprimir a lista dos escalões por ordem alfabética e para cada um indicar quantos atletas estão inscritos nesse escalão.
#     e) gerar uma página HTML com a lista das equipes inscritas em qualquer prova, indicando o seu nome e o número dos atletas que a constituem e que se inscreveram pelo menos uma vez numa prova; essa lista deve estar ordenada por ordem decrescente do número de atletas; além disso, cada equipe deve ter um link para outra página HTML com a informação que achar interessante sobre cada atleta indicando as provas em que cada um participou.

# a) imprimir o nome (convertido para maiúsculas) de todos os concorrentes que se inscrevem como 'Individuais' e são de 'Valongo'.

# In[10]:



## a)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj=json.loads(data)
obj = json.loads(data)

data=obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[23]:


for i in range(len(content)):
    linha=content[i]
    #print(str(linha))
    teste =re.search(r'(?i:Valongo)',str(linha))
    individual=re.search(r'(?i:Individual)',str(linha))
    if(teste and individual): 
        print('---------Dados de Inscrito---------')
        buscarecebendoCaps(r'\'nome\': \'([^\']*)\'',str(linha))
        print()
        
   


# b) imprimir o nome completo, o telemóvel e a prova em que está inscrito cada concorrente cujo nome
# seja 'Paulo' ou 'Ricardo', desde que usem o GMail.
# 

# In[16]:


## b)

# read file
with open('inscritos-form.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj=json.loads(data)
obj = json.loads(data)

data=obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[19]:


for i in range(len(content)):
    linha=content[i]
    #print(str(linha))
    paulo =re.search(r'(?i:Paulo)',str(linha)) ## aqui posso especificar que deve estar dentro do nome
    ricardo=re.search(r'(?i:Ricardo)',str(linha))
    gmail=re.search(r'(?i:@gmail)',str(linha))
    
    if((paulo or ricardo)and gmail): 
        print('---------Dados de Utilizador---------')
        buscarecebendoCaps(r'\'nome\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'email\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'prova\': \'([^\']*)\'',str(linha))
        print()
   


#  c) imprimir toda a informação dos atletas da equipe "TURBULENTOS".

# In[ ]:



## c)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj=json.loads(data)
obj = json.loads(data)

data=obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[22]:


for i in range(len(content)):
    linha=content[i]
    #print(str(linha))
    turb =re.search(r'(TURBULENTOS)',str(linha)) ## turbulentos vs os turbolentos <- ver isto
    
    
    if(turb ): 
        print('---------Dados de Utilizador---------')
        buscarecebendoCaps(r'\'nome\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'dataNasc\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'morada\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'email\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'prova\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'escalao\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'equipa\': \'([^\']*)\'',str(linha))
        print()


# d) imprimir a lista dos escalões por ordem alfabética e para cada um indicar quantos atletas estão inscritos nesse escalão.

# In[24]:



## d)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj=json.loads(data)
obj = json.loads(data)

data=obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[26]:


#primeiro ciclo vai buscar todos os escalões e ordena 
# 2º ciclo vai a lista e pega nos nomes dos do dado escalão
# - escalão : 
# tendo a estrutura imprime

for i in range(len(content)):
    linha=content[i]
    #print(str(linha))
    escalao =re.search(r'escalao',str(linha)) 
   
    if(turb ): 
        print('---------Dados de Utilizador---------')
        buscarecebendoCaps(r'\'nome\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'dataNasc\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'morada\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'email\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'prova\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'escalao\': \'([^\']*)\'',str(linha))
        buscarecebendo(r'\'equipa\': \'([^\']*)\'',str(linha))
        print()


# e) gerar uma página HTML com a lista das equipes inscritas em qualquer prova, indicando o seu nome e o número dos atletas que a constituem e que se inscreveram pelo menos uma vez numa prova; essa lista deve estar ordenada por ordem decrescente do número de atletas; além disso, cada equipe deve ter um link para outra página HTML com a informação que achar interessante sobre cada atleta indicando as provas em que cada um participou.

# In[ ]:




