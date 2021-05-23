#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:25:13 2021

@author: 
"""

def assembliza(tupleX,fp,labelStack,contador_de_Ciclos):
    if (tupleX[0] == 'CodigoRec') :# ('Codigorec' ,BlocodeCodigo, Codigo )
        fp,contador_de_Ciclos=assembliza(tupleX[1],fp,labelStack,contador_de_Ciclos)
        fp,contador_de_Ciclos=assembliza(tupleX[2],fp,labelStack,contador_de_Ciclos)
    
    if (tupleX[0] == 'Declaracao') :#('Declaracao', 'INT', 'x')
        
        print('pushi 0')
        dict_var[tupleX[2]] = fp
        fp+=1
        
    
    if (tupleX[0] == 'Declaracao_e_Atribuicao') :#('Declaracao_e_Atribuicao',dec , atribuicao)
        print(tupleX)
        fp,contador_de_Ciclos=assembliza(tupleX[1],fp,labelStack,contador_de_Ciclos)
        fp,contador_de_Ciclos=assembliza(tupleX[2],fp,labelStack,contador_de_Ciclos)
        
        
    
    if (tupleX[0] == 'Declaracao_STDIN') :#('Declaracao_STDIN', ( ('STDIN', 'n') )
        
        print ('read')
        print ('atoi')
        
        dict_var[tupleX[2][1]] = fp
        fp+=1






    if (tupleX[0] == 'Atribuicao') :#('Atribuicao', 'c', ('Var', ('NUM', '0')))
    
    
        fp,contador_de_Ciclos=assembliza(tupleX[2],fp,labelStack,contador_de_Ciclos)
        
        print('storeg', dict_var.get(tupleX[1]))
        
    if (tupleX[0] == 'Operacao') :#('Operacao', '-', ('Var', ('ID', 'n')), ('NUM', '1')))
    
    
        fp,contador_de_Ciclos=assembliza(tupleX[2],fp,labelStack,contador_de_Ciclos)
        fp,contador_de_Ciclos=assembliza(tupleX[3],fp,labelStack,contador_de_Ciclos)
        
        if(tupleX[1]=='-'):
            print('sub')
        if(tupleX[1]=='+'):
            print('add')   
        if(tupleX[1]=='/'):
            print('div')   
        if(tupleX[1]=='*'):
            print('add')   
        
        
    if (tupleX[0] == 'STDIN') :#('STDIN', 'n')
        
        print(tupleX)
        print(tupleX[1])
        dict_var[tupleX[1]] = fp
        fp=fp+1
        
    if (tupleX[0] == 'OperacaoLogica') :#
        #fp=assembliza(tupleX[], fp)
        if(tupleX[1]=='&&'):
            fp,contador_de_Ciclos=assembliza(tupleX[2], fp,labelStack,contador_de_Ciclos)
            if(tupleX[2][0]!= 'OperacaoLogica'): print('jz label_IF_ELSE_'+str(contador_de_Ciclos))
            fp,contador_de_Ciclos=assembliza(tupleX[3], fp,labelStack,contador_de_Ciclos)
            if(tupleX[2][0]!= 'OperacaoLogica'): print('jz label_IF_ELSE_'+str(contador_de_Ciclos))
        
        
        #print(tupleX)
    if (tupleX[0] == 'OperacaoCondicional') :#('OperacaoCondicional', '>', ('ID', 'n'), ('NUM', '0'))
        if(tupleX[1]=='>'):
            print('pushg ', dict_var.get(tupleX[2][1]))
            print('pushg ', dict_var.get(tupleX[3][1]))
            print('sup')
            fp+=1
        if(tupleX[1]=='=<'):
            print('pushg ', dict_var.get(tupleX[2][1]))
            print('pushg ', dict_var.get(tupleX[3][1]))
            print('inf')
            fp+=1
    
        if(tupleX[1]=='=='):
            print('pushg ', dict_var.get(tupleX[2][1]))
            print('pushg ', dict_var.get(tupleX[3][1]))
            print('equal')
            fp+=1
    
    
        
        #print(tupleX)
    if (tupleX[0] == 'IF') :#('IF', ('OperacaoLogica', '&&', ('OperacaoLogica', '&&', ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'y')), ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'w'))), ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'z'))), ('STDOUT', ('ID', 'a')))
        assembliza(tupleX[1],fp,labelStack,contador_de_Ciclos)
        
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        print ('label_Startof_SimpleIF:')
        print('jump label_SimpleIF_DO'+str(cicleID))
        #Do de IFElse
        fp,text=assemblizatoList(tupleX[2],fp,labelStack,contador_de_Ciclos)
        l.append('label_IF_DO_'+str(cicleID)+':\n'+text+'stop')
        
        #print(tupleX)
        
        
    if (tupleX[0] == 'IFELSE') :
        
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        print ('label_Startof_IFELSE:')
        #Condição de IFElse
        fp,contador_de_Ciclos=assembliza(tupleX[1],fp,labelStack,contador_de_Ciclos)
        
        print('jump label_IF_DO_'+str(cicleID))
        print('jz label_IF_ELSE_'+str(cicleID))
        
        #Do de IFElse
        fp,text=assemblizatoList(tupleX[2],fp,labelStack,contador_de_Ciclos)
        l.append('label_IF_DO_'+str(cicleID)+':\n'+text+'stop')
        
        
        #Else de IFElse
        fp,text=assemblizatoList(tupleX[3],fp,labelStack,contador_de_Ciclos)
        l.append('label_IF_ELSE_'+str(cicleID)+':\n'+text+'stop')
        
        
    
        
        
        #print(tupleX)
    if (tupleX[0] == 'ID') :#('ID', 'x')
        print('pushg', dict_var.get(tupleX[1]))
        
        
    if (tupleX[0] == 'STDOUT') :#('STDOUT', ('ID', 'x')) 
        #print(tupleX)
        
        if(tupleX[1][0]=='ID'):
            print('pushg ', dict_var.get(tupleX[1][1]))
        else:
            print('pushs ', tupleX[1][0])
            
        print('writes')    
        
        
    if (tupleX[0] == 'COMMENT') :#('COMMENT', '*/ atenção aqui estou ainda a pensar como garantir que o numero é INT /*')
        
        print(tupleX)
        
    
        
        
    if (tupleX[0] == 'Var') : #('Var', ('ID', 'x'))
        fp,contador_de_Ciclos=assembliza(tupleX[1],fp,labelStack,contador_de_Ciclos)
        
    if (tupleX[0] == 'WHILE') :#('WHILE', ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'x')), 'DO', ('Declaracao', 'INT', 'y'))
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        print ('label_Startof_While:')
        
        #Condição de While
        fp,contador_de_Ciclos=assembliza(tupleX[1],fp,labelStack,contador_de_Ciclos)
        
        print('jump label_While_On_'+str(cicleID))
        
        
        
        
        #Do de While
        fp,text=assemblizatoList(tupleX[3],fp,labelStack,contador_de_Ciclos)
        l.append('label_While_On_'+str(cicleID)+':\n'+text+'stop')
        
        
        
    
        #print(tupleX)
    if (tupleX[0] == 'NUM') :#('NUM', '1')
        
        print('pushi',tupleX[1])
    
    
        
        
    return fp,contador_de_Ciclos

# é preciso ter em atenção a ordem da recursividade e que algumas das cenas devemos verificar se tem outros tuplos dentro
    


def assemblizatoList(tupleX,fp,labelStack,contador_de_Ciclos):
    aaa=""
    if (tupleX[0] == 'STDOUT') :#('STDOUT', ('ID', 'x')) 
        #print(tupleX)
        
        
        if(tupleX[1][0]=='ID'):
            aaa=aaa+'pushg '+ str(dict_var.get(tupleX[1][1]))+'\n'
        else:
            aaa=aaa+'pushs '+ tupleX[1][0] +'\n'
            
        aaa=aaa + 'writes \n'   
        
        
    
    
    
    if (tupleX[0] == 'Declaracao_STDIN') :#('Declaracao_STDIN', ( ('STDIN', 'n') )
        
        aaa=aaa+'read\n'
        aaa=aaa+'atoi\n'
        
        dict_var[tupleX[2][1]] = fp
        fp+=1

    return fp,aaa

        
