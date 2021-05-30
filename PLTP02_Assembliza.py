from PLTP02_lex import tokens
import ply.yacc as yacc
import sys
import os

def assembliza(tupleX,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer):
    
    if (tupleX[0] == 'CodigoRec') :# ('Codigorec' ,BlocodeCodigo, Codigo )
        
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
    if (tupleX[0] == 'Declaracao') :#('Declaracao', 'INT', 'x')
        
    
        if(tupleX[2] in dict_var): print('variavel tentou escrever por cima de outra')
            
        else:
            cabeca=cabeca + 'pushi 0\n'
            
            dict_var[tupleX[2]] = sp
            sp+=1

    if (tupleX[0] == 'Declaracao_e_Atribuicao') :#('Declaracao_e_Atribuicao',dec , atribuicao)
    
        cabeca=cabeca + 'pushi '+ str(tupleX[2][2][1][1]) +'\n'
        
        dict_var[tupleX[1][2]] = sp
        sp+=1

    if (tupleX[0] == 'Declaracao_STDIN') :#('Declaracao_STDIN', 'INT', ('STDIN', 'n'))
        
        aux = 'read\natoi\nstoreg ' + str(sp) + '\n'
        
        cabeca = cabeca + 'pushi 0\n' 
        corpo = corpo + aux

        dict_var[tupleX[2][1]] = sp
        sp+=1

    if (tupleX[0] == 'Atribuicao') :#('Atribuicao', 'c', ('Var', ('NUM', '0')))
    
        
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        corpo=corpo+'storeg '+ str(dict_var.get(tupleX[1])) + '\n\n'
        sp-=1

    if (tupleX[0] == 'Operacao') :#('Operacao', '-', ('Var', ('ID', 'n')), ('NUM', '1')))
    
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        if(tupleX[1]=='-'):
                corpo=corpo+'sub\n'
                sp-=1

        if(tupleX[1]=='+'):
                corpo=corpo+'add\n'
                sp-=1

        if(tupleX[1]=='/'):
                corpo=corpo+'div\n'
                sp-=1

        if(tupleX[1]=='*'):
                corpo=corpo+'mul\n'
                sp-=1

        if(tupleX[1]=='%'):
                corpo=corpo+'mod\n'
                sp-=1

    if (tupleX[0] == 'STDIN') :#('STDIN', 'n')
            corpo=corpo+'read\n'+'atoi\n'
            sp+=1
            corpo=corpo+ 'storeg ' +str(dict_var.get(tupleX[1])) + '\n\n'
            sp-=1

    if (tupleX[0] == 'OperacaoLogica'):

        if(tupleX[1]=='&&'):
            
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
            
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
            
            
            if(tupleX[2][0] != 'OperacaoLogica' or tupleX[3][0] != 'OperacaoLogica'): corpo=corpo+'mul\n'

    if (tupleX[0] == 'OperacaoCondicional') :#('OperacaoCondicional', '>', ('ID', 'n'), ('NUM', '0'))
        aux=""
        
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        if(tupleX[1]=='>'):
            aux=aux+'sup' + '\n'
            sp-=1
            
        if(tupleX[1]=='<'):
            aux=aux+'inf' + '\n'
            sp-=1
    
        if(tupleX[1]=='=='):
            aux=aux+'equal' + '\n'
            sp-=1
        if(tupleX[1]=='!='):
            aux=aux+'equal' + '\n'+'NOT' + '\n'
            sp-=1
        if(tupleX[1]=='>='):
            aux=aux+'supeq'  + '\n'
            sp-=1
    
        corpo=corpo+aux

    if (tupleX[0] == 'IF') :#('IF', ('OperacaoLogica', '&&', ('OperacaoLogica', '&&', ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'y')), ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'w'))), ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'z'))), ('STDOUT', ('ID', 'a')))
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        
        extraID=extrapointer

        corpo=corpo+aux
        aux=""
        
        #---------------
        #condição do if
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        aux+='jz ENDSimpleIF'+str(cicleID)+'\n\n'
        
        corpo=corpo+aux
        aux=""

        extrapointer=extraID
        delayaux=delay

        #Do de IF
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        delay=delayaux
        
        aux=aux+'\n\tENDSimpleIF'+str(cicleID)+':       \n'
        
        corpo=corpo+aux
        aux=""
        
        extrapointer=extraID

    if (tupleX[0] == 'IFELSE') :
    
        aux=""
        
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
        #---------------
        #condição do if
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        corpo=corpo+'jz ELSE'+str(cicleID)+'\n\n'
        aux=""   
        
        #---------------
        #tarefas do IfELSE
        
        extrapointer=extraID
        
        delayaux=delay
        
        #---------------
        #tarefas do IfELSE --- DO
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        extrapointer=extraID
        corpo=corpo+'jump ENDIFELSE'+str(cicleID)+'\n'
        aux=""   
        
        #---------------
        #tarefas do IfELSE --- ELSE
        #Else de IFElse
        corpo=corpo+'\n\tELSE'+str(cicleID)+':\n\n'
        aux=""   
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        extrapointer=extraID
        
        delay=delayaux
        
        aux=aux+'\nENDIFELSE'+str(cicleID)+':     \n\n'
        corpo=corpo+aux
        aux=""
        
    if (tupleX[0] == 'ID') :#('ID', 'x')
        aux='pushg '+str(dict_var.get(tupleX[1]))+'\n'
        sp+=1
        corpo=corpo+aux
        
    if (tupleX[0] == 'STDOUTPAL') :
        corpo=corpo+'pushs '+tupleX[1]+'\n' +'writes\npushs "\\n"\nwrites\n'
        sp+=1

    if (tupleX[0] == 'STDOUT') :#('STDOUT', ('ID', 'x')) 
        
        if(tupleX[1][0]=='ID'):
            
                corpo=corpo+'pushg '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\npushs "\\n"\nwrites\n'

        if(tupleX[1][0]=='NUM'):
            corpo=corpo+'pushi '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\npushs "\\n"\nwrites\n' 
        
        if(tupleX[1][0]=='TRUE'):
            corpo=corpo+'pushs "TRUE" '+'\n' + 'writes\npushs "\\n"\nwrites\n'
            
        if(tupleX[1][0]=='FALSE'):
            corpo = corpo + 'pushs "FALSE" '+'\n' + 'writes\npushs "\\n"\nwrites\n'
 
    if (tupleX[0] == 'COMMENT') :#('COMMENT', '*/ atenção aqui estou ainda a pensar como garantir que o numero é INT /*')
        size = len(tupleX[1])
        aux = tupleX[1][2:size-2]
        corpo = corpo + '\n\t//' + aux + '\n\n'

    if (tupleX[0] == 'Var') : #('Var', ('ID', 'x'))
    
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

    if (tupleX[0] == 'WHILE') :#('WHILE', ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'x')), 'DO', ('Declaracao', 'INT', 'y'))
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer

        aux=aux+'\n\tWhile'+str(cicleID)+':            \n\n'
        corpo=corpo+aux
        aux=""
        
        extrapointer=extraID
        #Condição de While
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        extrapointer=extraID
        aux=aux+'jz EndOfWhile'+str(cicleID)+'\n\n'
        corpo=corpo+aux
        aux=""

        delayaux=delay
        
        extrapointer=extraID

        #Do de While
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        aux=aux+'jump While'+str(cicleID)+'\n'
        corpo=corpo+aux
        aux=""
        delay = delayaux
        
        aux=aux+'\n\tEndOfWhile'+str(cicleID)+':         \n\n'
        corpo=corpo+aux
        aux=""

    if (tupleX[0] == 'NUM') :#('NUM', '1')
        aux='pushi '+str(tupleX[1])+'\n'
        sp+=1#
        corpo=corpo+aux
        
        
    if (tupleX[0] == 'ARRAYNUM') :#ARRAYNUM NUM ID ';' "  DONE
        cabeca=cabeca + 'pushn '+ tupleX[1]+'\n'
        
        dict_var[tupleX[2]] = sp
        sp+=1
    
    if (tupleX[0] == 'ARRAYID') :#ARRAYID ID ID ';' "
        cicleID = contador_de_Ciclos
        variavel_tamanho=tupleX[1]
        variavel_array=tupleX[2]
        
        dict_var[variavel_array] = sp
        sp+=1
        #('FOR', 'j', ('OperacaoCondicional', '<', ('ID', 'j'), ('ID', 'tamanho')), ('Atribuicao', 'j', ('Operacao', '+', ('Var', ('ID', 'j')), ('NUM', '1'))), ('Atribuicao', 'i', ('Var', ('NUM', '0')))))
        
        tuplexAux= ('FOR_ARRAY_IN', 'indicedefor'+str(cicleID), variavel_tamanho, variavel_array)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza_ARRAY(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        #ciclo For Para Criar Array

        sp+=1

    if (tupleX[0] == 'FOR') :#('FOR', (ID ,  A ), (Condição) ,OperacaoAtribuição , BlocodeCodigo )
        aux="" 
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
        # assembliza-declaração do indice
        tuplexAux= ('Declaracao','INT',tupleX[1])
        fp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        #('Atribuicao', 'c', ('Var', ('NUM', '0')))
        #tuplexAux= ('Atribuicao',tupleX[1],('Var', ('NUM', '0')))
        #sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        #Criação Labelfor_
        aux=aux+'\n\tFor'+str(cicleID)+':\n\n'
        corpo=corpo+aux
        aux=""
        
        #assembliza-codigo da condição 
        tuplexAux= tupleX[2]
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        #+ jz para fim
        aux=aux+'jz EndOfFor'+str(cicleID)+'\n\n'
        corpo=corpo+aux
        aux=""
        #assembliza-BlocoCodigo
        tuplexAux= tupleX[4]
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        #assembliza-Operacao
        tuplexAux= tupleX[3]
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        #jump Labelfor_
        aux=aux+'jump For'+str(cicleID)+'\n'
        corpo=corpo+aux
        aux=""
        aux=aux+'\n\tEndOfFor'+str(cicleID)+':\n'
        corpo=corpo+aux
        aux=""

    if (tupleX[0] == 'STRUCTARRAY_STDIN') :#('STRUCTARRAY_STDIN', p[2],p[3] )
        cicleID = contador_de_Ciclos
        variavel_nome=tupleX[1]
        variavel_indice=tupleX[2]

        #('FOR', 'j', ('OperacaoCondicional', '<', ('ID', 'j'), ('ID', 'tamanho')), ('Atribuicao', 'j', ('Operacao', '+', ('Var', ('ID', 'j')), ('NUM', '1'))), ('Atribuicao', 'i', ('Var', ('NUM', '0')))))
        
        tuplexAux= ('FOR_ARRAY_STDIN',  variavel_indice, variavel_nome)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza_ARRAY(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        #ciclo For Para Criar Array

        sp+=1
    if (tupleX[0] == 'STRUCTARRAY_STDOUT') :#ARRAYID ID ID ';' "
        
        cicleID = contador_de_Ciclos
        variavel_array=tupleX[1]
        variavel_indice=tupleX[2]
        
        #('FOR', 'j', ('OperacaoCondicional', '<', ('ID', 'j'), ('ID', 'tamanho')), ('Atribuicao', 'j', ('Operacao', '+', ('Var', ('ID', 'j')), ('NUM', '1'))), ('Atribuicao', 'i', ('Var', ('NUM', '0')))))
        
        tuplexAux= ('FOR_ARRAY_STDOUT',  variavel_indice, variavel_array)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza_ARRAY(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)

        #ciclo For Para Criar Array

        sp+=1
        
    
    if (tupleX[0] == 'RETURNID') :#('RETURN', "x")
        aux=""
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
        aux=aux+'pushg '+str(dict_var.get(tupleX[1]))+'\nstorel -1\n\n'
        corpo=corpo+aux
        aux=""
    if (tupleX[0] == 'RETURN') :#('RETURN', "1")
        aux=""
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
        aux=aux+'pushi '+str(tupleX[1])+'\nstorel -1\n\n'
        corpo=corpo+aux
        aux=""
        
    if (tupleX[0] == 'CALLEMPTY') :#('CALLEMPTY', "_nome_")
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
        aux=aux+'pusha '+str(tupleX[1])+'\ncall\nnop\npushs "a funcao devolveu:\\n"\nwrites\nwritei\npushs "debug :FIM\\n"\nwrites\n'
        
        corpo=corpo+aux
        aux=""
        
    if (tupleX[0] == 'CALLEMPTYID') :#('CALLEMPTY',ID, "_nome_")
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer

        cabeca = cabeca + 'pushi 0\n'
        
        dict_var[tupleX[1]] = sp

        aux = aux + 'pushi 0\npusha '+str(tupleX[2])+'\ncall\nnop\n'
        aux = aux + 'storeg ' + str(sp) + '\n\n'
        corpo = corpo + aux

        aux=""
        
    if (tupleX[0] == 'Declaracao_e_AtribuicaoReturn'):
        dict_var[tupleX[1]] = sp
        sp+=1
    if (tupleX[0] == 'DEFINEEMPTY') :#('DEFINEEMPTY', "_nome_", tuplex de bloco de codigo)
    
        dict_varaux = {}
        contador_de_Ciclosaux=contador_de_Ciclos
        spaux=0
        extrapointeraux=0
        cabecaaux=""
        corpoaux=""
        extraaux=[]
        
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        bloco_de_codigo_da_funcao=tupleX[2]
        
        aux=aux+'\t'+str(tupleX[1])+': nop\n'
                
        s,cabecaaux,corpoaux,extraaux,contador_de_Ciclos,delayaux,dict_var,extrapointeraux= assembliza(bloco_de_codigo_da_funcao,sp,contador_de_Ciclosaux,False,cabecaaux,corpoaux,extraaux,dict_var,extrapointeraux)

        cabeca=cabeca+cabecaaux
        aux=aux+corpoaux
        
        aux=aux+'return\n'
        
        extra.append(aux)
        
        aux=""
  
    return sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer

# é preciso ter em atenção a ordem da recursividade e que algumas das cenas devemos verificar se tem outros tuplos dentro
    


def assembliza_ARRAY(tupleX,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer):
    if (tupleX[0] == 'FOR_ARRAY_IN') :#('FOR', indice , tamanho,nome )
        aux="" 
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        indice = tupleX[1]
        tamanho = tupleX[2]
        nome = tupleX[3]

        # assembliza-declaração do indice
        sp-=1
        tuplexAux= ('Declaracao','INT',indice)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        #('Atribuicao', 'c', ('Var', ('NUM', '0')))
        dict_var[nome] = sp
        sp+=1
        #Criação Labelfor_
        aux=aux+'\tForArray'+str(cicleID)+':\n'
        corpo=corpo+aux
        aux=""
        
        #
        aux=aux+'pushg '+str(dict_var.get(indice))+'\n'
        aux=aux+'pushg '+str(dict_var.get(tamanho))+'\ninf\n'
        sp+=1
        corpo=corpo+aux
        aux=""
        
        #+ jz para fim
        aux=aux+'jz EndOfForArray'+str(cicleID)+'\n\n'
        corpo=corpo+aux
        aux=""
        #assembliza-BlocoCodigo
        aux=aux+'pushi 0\n'
        sp+=1
        corpo=corpo+aux
        aux=""
        
        #assembliza-Operacao
        aux=aux+'pushg '+str(dict_var.get(indice))+'\n\n'
        aux=aux+'pushi 1\nadd\n'
        sp+=1
        aux=aux+'storeg '+str(dict_var.get(indice))+'\n\n'
        sp-=1
        corpo=corpo+aux
        aux=""
        
        
        #jump Labelfor_
        aux=aux+'jump ForArray'+str(cicleID)+'\n'
        corpo=corpo+aux
        aux=""
        aux=aux+'\tEndOfForArray'+str(cicleID)+':\n'
        corpo=corpo+aux
        aux=""
        
    if (tupleX[0] == 'FOR_ARRAY_STDIN') :#('FOR', indice , tamanho )
        aux="" 
        nome = tupleX[2]
        indice = tupleX[1]
        
        
        #
        aux=aux+'pushgp\npushi '+str(dict_var.get(nome))+'\npadd\n'
        sp+=1
        aux=aux+'pushg  '+str(dict_var.get(indice))+'\n'
        sp+=1
        aux=aux+'read\natoi\nstoren\n\n'
        corpo=corpo+aux
        aux=""

    if (tupleX[0] == 'FOR_ARRAY_STDOUT') :#('FOR', indice , tamanho )
        aux="" 
        indice = tupleX[1]
        nome = tupleX[2]
        
        
        #
        aux=aux+'pushgp\npushi '+str(dict_var.get(nome))+'\npadd\n'
        sp+=1
        aux=aux+'pushg  '+str(dict_var.get(indice))+'\n'
        sp+=1
        aux=aux+'loadn\nwritei\npushs "\\n"\nwrites\n'
        
        corpo=corpo+aux
        aux=""

    return sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer


