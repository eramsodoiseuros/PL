#!/usr/bin/env python
# coding: utf-8

# In[17]:


import re


# In[18]:


## Teste de Leitura
#with open('inscritos-form.json', 'r') as myfile:
   #data = myfile.read()
#print(data)
#myfile.close()


# In[19]:


def trataJson(jfile):
    with open(jfile, 'r') as myfile:
        data = myfile.read()
    content = data
    fatl=re.sub(r'\n',' ',data)      
    fatl=re.sub(r'[^i]*inscritos\"\:\[','',fatl)
    dataA=re.split(r'},{', fatl)
    for i in range(len(dataA)):
        dataA[i]=re.split(r'\"\,\s*\"', dataA[i])
        for j in range(len(dataA[i])):
            cena=re.split(r'\"\:\"', dataA[i][j])
            if(len(cena)>1):
                dataA[i][j]= cena[1]
            else:
                dataA[i][j]= "NaN"   
        dataA[i][6]=re.sub(r'\"','',dataA[i][6])
    myfile.close()
    return dataA


# In[20]:


def getdataLine(linha):
    name = re.search(r'([^"]*)',linha[0])
    dataNasc = re.search(r'([^"]*)',linha[1])
    morada = re.search(r'([^"]*)',linha[2])
    email = re.search(r'([^"]*)',linha[3])
    prova = re.search(r'([^"]*)',linha[4])
    escalao = re.search(r'([^"]*)',linha[5])
    equipa = re.search(r'([^"]*)',linha[6])
    
    return name, dataNasc, morada, email,prova,escalao,equipa
    


# In[21]:


def showMeDist(dataSplited):
    print(0,"- nome -",dataSplited[1][0])
    print(1,"- dataNasc -",dataSplited[1][1])
    print(2,"- morada -",dataSplited[1][2])
    print(3,"- email -",dataSplited[1][3])
    print(4,"- prova -",dataSplited[1][4])
    print(5,"- escalao -",dataSplited[1][5])
    print(6,"- equipa -",dataSplited[1][6])
    


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

# d) imprimir a lista dos escalões por ordem alfabética e para cada um indicar quantos atletas estão inscritos nesse escalão.

# In[22]:


dataSplited=trataJson('inscritos-form.json')
# showMeDist(dataSplited)


# In[23]:


d = dict()
for linha in dataSplited:
    if linha[5] not in d:
        d[linha[5]] = 1
    else:
        d[linha[5]]+=1

for x in sorted(d):
    print(x, d[x])


# In[ ]:





# In[ ]:




