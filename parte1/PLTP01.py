#!/usr/bin/env python
# coding: utf-8

# In[10]:


import re
import json


# In[11]:



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


# In[12]:


## Teste de Leitura
# read file
with open('inscritos-form.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)
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

# In[63]:



## a)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)
obj = json.loads(data)

data = obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[56]:


for i in range(len(content)):
    linha = content[i]
    
    #print(str(linha))
    teste = re.search(r'(?i:Valongo)',linha['morada'])
    if(teste):
        individual = re.search(r'(?i:Individual)',linha['equipa'])
    
        if(individual): 
            print('---------Dados de Inscrito---------')
            print(linha['nome'].upper())
            print()
        
   


# b) imprimir o nome completo, o telemóvel e a prova em que está inscrito cada concorrente cujo nome
# seja 'Paulo' ou 'Ricardo', desde que usem o GMail.
# 

# In[100]:


## b)

# read file
with open('inscritos-form.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)
obj = json.loads(data)

data = obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[101]:


for i in range(len(content)):
    linha = content[i]
    #print(str(linha))
    paulo = re.search(r'(?i:Paulo)',linha['nome']) ## aqui posso especificar que deve estar dentro do nome
    ricardo = re.search(r'(?i:Ricardo)',linha['nome'])
    if((paulo or ricardo)):
        gmail = re.search(r'(?i:@gmail)',linha['email'])
    
        if( gmail): 
            print('---------Dados de Utilizador---------')
            print(linha['nome'].upper())
            print(linha['email'])
            print(linha['prova'])
            print()
   


#  c) imprimir toda a informação dos atletas da equipe "TURBULENTOS".

# In[107]:



## c)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)
obj = json.loads(data)

data = obj.pop('inscritos')

content = data
#open('inscritos-form.json', encoding="utf-8")


# In[109]:


for i in range(len(content)):
    linha = content[i]
    
    turb = re.search(r'(TURBULENTOS)',linha['equipa']) ## turbulentos vs os turbolentos <- ver isto
    
    
    if(turb ): 
        print('---------Dados de Utilizador---------')
        print(linha['nome'])
        print(linha['dataNasc'])
        print(linha['morada'])
        print(linha['email'])
        print(linha['prova'])
        print(linha['escalao'])
        print(linha['equipa'])
        print()


# d) imprimir a lista dos escalões por ordem alfabética e para cada um indicar quantos atletas estão inscritos nesse escalão.

# In[104]:



## d)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)
obj = json.loads(data)

data = obj.pop('inscritos')

content = data#open('inscritos-form.json', encoding="utf-8")


# In[ ]:





# In[105]:


#primeiro ciclo vai buscar todos os escalões e ordena 
# 2º ciclo vai a lista e pega nos nomes dos do dado escalão
# - escalão : 
# tendo a estrutura imprime
d = dict()
for a in content:
    if a['escalao'] not in d:
        d[a['escalao']] = 1
    else:
        d[a['escalao']]+=1

print(d)


# e) gerar uma página HTML com a lista das equipes inscritas em qualquer prova, indicando o seu nome e o número dos atletas que a constituem e que se inscreveram pelo menos uma vez numa prova; 
# 
# essa lista deve estar ordenada por ordem decrescente do número de atletas; 
# 
# além disso, cada equipe deve ter um link para outra página HTML com a informação que achar interessante sobre cada atleta indicando as provas em que cada um participou.

# In[ ]:


# 1 º equipas + numero de atletas
# ordenar lista por ordem decrescente de n de atletas
# Link para outra pagina html
    # ATLETAS DE 1 EQUIPA (nome) com informação de provas em que está inscrito


# In[126]:



## e)
# read file
with open('inscritos-form.json', 'r') as myfile:
    data = myfile.read()
# parse file
obj = json.loads(data)
content = obj.pop('inscritos')


# In[123]:


d = dict()
for a in content:
    if a['equipa'] not in d:
        d[a['equipa']] = 1
    else:
        d[a['equipa']]+=1
#d


# In[122]:


for w in sorted(d, key=d.get, reverse=True):
    print(w, d[w])


# In[ ]:




