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

# a) imprimir o nome (convertido para maiúsculas) de todos os concorrentes que se inscrevem como 'Individuais' e são de 'Valongo'.

# In[6]:


dataSplited=trataJson('inscritos-form.json')
showMeDist(dataSplited)


# In[19]:


for linha in dataSplited:
    morada =re.search(r'(?i:Valongo)',linha[2])
    if(morada):
        individual = re.search(r'(?i:Individual)',linha[6])
    
        if(individual): 
            name, dataNasc, moradaS, email,prova,escalao,equipa= getdataLine(linha)
            print('Nome de Inscrito: ',name[1].upper(),'\n' )
            f = open('PLTP01_exA.txt', "a")
            f.write('''Resposta:
            ''')
            f.write('''Nome de Inscrito: 
            ''')
            f.write(name[1].upper())
            f.write('\n')
            f.close()
   


# b) imprimir o nome completo, o telemóvel e a prova em que está inscrito cada concorrente cujo nome
# seja 'Paulo' ou 'Ricardo', desde que usem o GMail.
# 

# In[29]:


dataSplited=trataJson('inscritos-form.json')
showMeDist(dataSplited)


# In[30]:



for linha in dataSplited:
    paulo =re.search(r'(?i:Paulo)',linha[0]) 
    ricardo =re.search(r'(?i:Ricardo)',linha[0])
    if((paulo or ricardo)):
        gmail = re.search(r'(?i:@gmail)',linha[3])
    
        if( gmail): 
            f = open('PLTP01_exB.txt', "a")
            name, dataNasc, morada, email,prova,escalao,equipa= getdataLine(linha)
            resp='Dados de Utilizador:'+'\n'+ 'Nome: '+name[1].upper()+'\n'+'Email: '+email[1]+'\n'+'Prova: '+prova[1]+'\n'+'\n'
            print(resp)
            f.write(resp)
            f.close()
   


#  c) imprimir toda a informação dos atletas da equipe "TURBULENTOS".

# In[13]:


dataSplited=trataJson('inscritos-form.json')
showMeDist(dataSplited)


# In[37]:


for linha in dataSplited:
    
    turb = re.search(r'^(?i:TURBULENTOS$)',linha[6]) ## turbulentos vs os turbolentos <- ver isto
    if(turb ): 
        f = open('PLTP01_exC.txt', "a")
        name, dataNasc, morada, email,prova,escalao,equipa= getdataLine(linha)
        resp='Dados de Utilizador:'+'\n'+ 'Nome: '+name[1].upper()+'\n'+'Data de Nascimento: '+dataNasc[1]+'\n'+'Morada: '+morada[1]+'\n'+'Email: '+email[1]+'\n'+'Prova: '+prova[1]+'\n'+'Escalão: '+escalao[1]+'\n'+'Prova: '+equipa[1]+'\n'+'\n'
        print(resp)
        f.write(resp)
        f.close()


# d) imprimir a lista dos escalões por ordem alfabética e para cada um indicar quantos atletas estão inscritos nesse escalão.

# In[20]:


dataSplited=trataJson('inscritos-form.json')
showMeDist(dataSplited)


# In[42]:


d = dict()
for linha in dataSplited:
    if linha[5] not in d:
        d[linha[5]] = 1
    else:
        d[linha[5]]+=1

for x in sorted(d):
    f = open('PLTP01_exD.txt', "a")
    escalao = x
    n=d[x]
    resp='---Dados de escalão---'+'\n'+ 'Nome de escalão: '+'\''+escalao+'\''+'\n'+'Numero de Inscritos: '+str(n)+'\n'+'\n'
    print(resp)
    f.write(resp)
    f.close()    


# In[14]:


#primeiro ciclo vai buscar todos os escalões e ordena 
# 2º ciclo vai a lista e pega nos nomes dos do dado escalão
# - escalão : 
# tendo a estrutura imprime


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

# In[15]:


# 1 º equipas + numero de atletas
# ordenar lista por ordem decrescente de n de atletas
# Link para outra pagina html
    # ATLETAS DE 1 EQUIPA (nome) com informação de provas em que está inscrito


# In[23]:


dataSplited=trataJson('inscritos-form.json')
showMeDist(dataSplited)


# In[ ]:





# In[24]:


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


# In[30]:


lfinal=[]
for i in range(len(lteam)):
    lfinal.append((lteam[i], lnome[i], len(lnome[i])))
lfinal = sorted(lfinal, key=lambda tup: tup[2],reverse=True)

lfinal


# In[32]:


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


# In[33]:


htmljogadorMake(lfinal[1][0], lfinal[1][1][1])


# In[34]:


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


# In[35]:


html1Make(lfinal)


# In[ ]:





# In[ ]:





# In[ ]:




