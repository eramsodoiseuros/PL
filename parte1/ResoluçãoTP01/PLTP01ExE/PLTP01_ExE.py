#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import os


# In[2]:


## Teste de Leitura
#with open('inscritos-form.json', 'r') as myfile:
   #data = myfile.read()
#print(data)
#myfile.close()


# problema do backslash na cria~ão de ir


# In[3]:


def trataJson(jfile):
    with open(jfile, 'r') as myfile:
        data = myfile.read()
    content = data
    fatl=re.sub(r'\n',' ',data)      
    fatl=re.sub(r'[^i]*inscritos\"\:\[','',fatl)
    fatl=re.sub(r'}    ] }','',fatl)       
    dataA=re.split(r'},{', fatl)
    for i in range(len(dataA)):
        dataA[i]=re.split(r'\"\,\s*\"', dataA[i])
        for j in range(len(dataA[i])):
            cena=re.split(r'\"\:\"', dataA[i][j])
            if(len(cena)>1):
                dataA[i][j]= cena[1]
            else:
                dataA[i][j]= "NaN"     
        dataA[i][6]=re.sub(r'\"','',dataA[i][6])     # problema do ultimo jogador ter " no fim da equipa
        dataA[i][6]=re.sub(r'\/','',dataA[i][6])    # problema do backslash na cria~ão de ir
        dataA[i][6]=re.sub(r'\s+$','',dataA[i][6])
    myfile.close()
    return dataA


# In[4]:


def getdataLine(linha):
    name = re.search(r'([^"]*)',linha[0])
    dataNasc = re.search(r'([^"]*)',linha[1])
    morada = re.search(r'([^"]*)',linha[2])
    email = re.search(r'([^"]*)',linha[3])
    prova = re.search(r'([^"]*)',linha[4])
    escalao = re.search(r'([^"]*)',linha[5])
    equipa = re.search(r'([^"]*)',linha[6])
    
    return name, dataNasc, morada, email,prova,escalao,equipa
    


# In[5]:


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

# e) gerar uma página HTML com a lista das equipes inscritas em qualquer prova, indicando o seu nome e o número dos atletas que a constituem e que se inscreveram pelo menos uma vez numa prova; 
# 
# essa lista deve estar ordenada por ordem decrescente do número de atletas; 
# 
# além disso, cada equipe deve ter um link para outra página HTML com a informação que achar interessante sobre cada atleta indicando as provas em que cada um participou.

# <html>
#     <head>
#         <h1>Pagina de apresentação de equipas<h1>
#     </head>
#     <body>
#         <equipa> <h2>Team 1</h2>
#             <jogador> 
#                 <nome> player 1</nome>
#                 <cena> cena 1</cena>
#             </jogador> 
#         </equipa>  
#     </body>
# </html>

# In[6]:


# 1 º equipas + numero de atletas
# ordenar lista por ordem decrescente de n de atletas
# Link para outra pagina html
    # ATLETAS DE 1 EQUIPA (nome) com informação de provas em que está inscrito


# In[7]:


dataSplited=trataJson('inscritos-form.json')
showMeDist(dataSplited)


# In[ ]:





# In[8]:


lteam=[]
lnome=[]
# lteam - nomes equipas
# lnome - [
            #[
                #(nome,informações)
            #]
        #]
        #[[equipa1],[equipa2]]
for linha in dataSplited:
    name, dataNasc, morada, email,prova,escalao,equipa= getdataLine(linha)
    if equipa[1].upper() not in lteam:
        
        lteam.append(equipa[1].upper())
        lnome.append([(name[1],[dataNasc[1], morada[1], email[1],prova[1],escalao[1],equipa[1]])])
    else:
        lnome[lteam.index(equipa[1].upper())].append((name[1],[dataNasc[1], morada[1], email[1],prova[1],escalao[1],equipa[1]]))
#print(lteam)
#print(lnome)


# In[9]:


lfinal=[]
for i in range(len(lteam)):
    lfinal.append((lteam[i], lnome[i], len(lnome[i])))
lfinal = sorted(lfinal, key=lambda tup: tup[2],reverse=True)

lfinal


# In[10]:


def htmljogadorMake(equipa, tuplogamer):
    equipa=equipa.replace(" ", "")
    grant=True;
    pastadeequipa = 'PastaHtml'+'/'+equipa
    if not os.path.exists(pastadeequipa):
        os.mkdir(pastadeequipa)
    nomeHtml= pastadeequipa+'/'+ tuplogamer[0].replace(" ", "") +'.html'
    print(nomeHtml)
    if not os.path.exists(nomeHtml):
        f = open(nomeHtml, "w")

        f.write('''<html>
            <head><title>Informação de Jogador</title></head>
            <body>''')
        f.write('<Jogador> <h2>'+ tuplogamer[0] +'</h2><br>')
        f.write('<dataNasc>'+ 'Data de Nascimento: '+ tuplogamer[1][0]+';'+'</dataNasc><br>')
        f.write('<morada>'+ 'Morada: '+ tuplogamer[1][1]+';'+'</morada><br>')
        f.write('<email>'+ 'Email: '+ tuplogamer[1][2]+';'+'</email><br>')
        f.write('<provas>'+ 'Provas: '+ tuplogamer[1][3]+';'+'</provas><br>')
        f.write('<escalao>'+ 'Escalão: '+ tuplogamer[1][4]+';'+'</escalao><br>')
        f.write('<equipa>'+ 'Equipa: '+ tuplogamer[1][5]+';'+'</equipa><br>')
        f.write('</Jogador>')
        f.write('</body> </html>')
        f.close()
    else: 
        grant=False;
        f = open(nomeHtml, "r")
        cont=f.read()
        cont=re.sub(r'<provas>Provas:','<provas>Provas:'+tuplogamer[1][3]+'; ',cont)
        f.close()
        f = open(nomeHtml, "w")
        f.write(cont)
        f.close()
        
    
    return equipa+'/'+ tuplogamer[0].replace(" ", "") +'.html',grant


# In[11]:


htmljogadorMake(lfinal[1][0], lfinal[1][1][1])


# In[12]:


def html1Make(lfinal):
    nomeHtml= 'PastaHtml'+'/'+'testePL.html'
    print(nomeHtml)
    if not os.path.exists('PastaHtml'):
        os.mkdir('PastaHtml')
    f = open(nomeHtml, "w")
    f.write('''<html>
    <head><title>Lista de Todas as equipas</title></head>
    <body>''')
    for i in lfinal:
        f.write('<equipa> <h2>'+i[0] +'</h2><br>')
        for j in range(len(i[1])):
            link, grant = htmljogadorMake(i[0], i[1][j])
            if grant:
                f.write('<jogador>'+i[1][j][0]+'</jogador><br>')
                f.write('<a href='+link+'>link</a><br>')
        
        f.write('</equipa>')
    f.write('</body> </html>')
    f.close()
    return


# In[13]:


html1Make(lfinal)


# In[ ]:





# In[ ]:





# In[ ]:




