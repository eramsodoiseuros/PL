

from PLTP02_lex import tokens
from PLTP02_Perguntas import pList
import ply.yacc as yacc
import sys

a3_WHILEDO= """INT x = STDIN(); 
        WHILE(x==x) 
        DO{STDOUT(x);}
        """

a1_Atribuicao= """INT x = (1+1)+2;"""

        







def p_Programa(p):
    "Programa : BlocosCodigo"
    #print('Parsing completed succesfully! Value synthesized: ', p[1])
    #print(p[1])
    p[0]=p[1]
    
    
    ####----------------------------------------------------------------------
def p_BlocoCodigo_fin(p):
    "BlocosCodigo  :  Codigo "
    #print('Parsing Codigo succesfully! ID DID' , p[1])
    p[0]=p[1]

def p_BlocosCodigo_Rec(p):
    "BlocosCodigo  :  BlocosCodigo Codigo "
    #print('Parsing Codigo succesfully! ID DID' , p[1])
    tupleX=('CodigoRec',p[1],p[2])
    p[0]=tupleX
    
    ####----------------------------------------------------------------------
### p_Declaracao

def p_Codigo_Declaracao(p):
    "Codigo  :  Declaracao "
    #print('Parsing Declaracao' , p[1])
    p[0]=p[1]
    
def p_Declaracao(p):
    "Declaracao :  INT ID ';' "
    tupleX= ('Declaracao',p[1],p[2])
    #print(','.join(tupleX))
    p[0]=tupleX

def p_Declaracao_Atribuicao(p):
    "Declaracao :  INT ID '=' Expressao ';'"
    tupleX= ('Declaracao_e_Atribuicao',('Declaracao',p[1],p[2]),('Atribuicao',p[2],p[4]))
    #print(','.join(tupleX))
    p[0]=tupleX

def p_Declaracao_STDIN(p):
    "Declaracao :  INT BlocoLerSTDIN "
    tupleX= ('Declaracao_STDIN',p[1],p[2])
    #print(','.join(tupleX))
    p[0]=tupleX

    ####----------------------------------------------------------------------
### Atribuição
def p_Codigo_Atribuicao(p):
    "Codigo  : Atribuicao  "
    #print('Parsing Atribuicao' , p[1])
    p[0]=p[1]

def p_Atribuicao(p):
    " Atribuicao : ID '=' Expressao ';' "
    tupleX= ('Atribuicao',p[1],p[3])
    #a=','.join(p[1])
    #b=','.join(p[3])
    #print('Atribuicao',a,b)
    p[0]=tupleX
    
def p_Atribuicao_FUNC(p):
    " Atribuicao : ID '=' Bloco_CALLFUNC "
    tupleX= ('Atribuicao',p[1],p[3])
    #a=','.join(p[1])
    #b=','.join(p[3])
    #print('Atribuicao',a,b)
    p[0]=tupleX



def p_Expressao_fin(p):
    " Expressao : Var "
    tupleX=('Var',(p[1]))
    p[0]=tupleX

def p_Var_NUM(p):
    " Var : NUM "
    tupleX = ('NUM',p[1])
    #print(','.join(tupleX))
    p[0]=tupleX
    
def p_Var_ID(p):
    " Var : ID "
    tupleX = ('ID',p[1])
    #print(','.join(tupleX))
    p[0]=tupleX
def p_Var_TRUE(p):
    " Var : TRUE "
    tupleX = ('TRUE',p[1])
    #print(','.join(tupleX))
    p[0]=tupleX
def p_Var_FALSE(p):
    " Var : FALSE "
    tupleX = ('FALSE',p[1])
    #print(','.join(tupleX))
    p[0]=tupleX



def p_Expressao_Rec1(p):
    " Expressao : Expressao Operador Var "
    tupleX = ('Operacao',p[2],p[1],p[3])
    p[0]=tupleX

def p_Expressao_Rec2(p):
    " Expressao : '(' Expressao  ')' "
    
    p[0]=p[2]
    

    
def p_Operador_MAIS(p):
    " Operador : '+' "
    p[0]=p[1]

def p_Operador_Minus(p):
    " Operador : '-' "
    p[0]=p[1]
def p_Operador_MUL(p):
    " Operador : '*' "
    p[0]=p[1]
def p_Operador_Div(p):
    " Operador : '/' "
    p[0]=p[1]
def p_Operador_Rest(p):
    " Operador : '%' "
    p[0]=p[1]




    ####----------------------------------IF------------------------------------
def p_Codigo_BlocoIF(p):
    "Codigo  : BlocoIF"
    #print('Parsing BlocoIF' , p[1])
    p[0]=p[1]


    
def p_BlocoIF(p):
    " BlocoIF : IF '(' ListaCondicionais ')' '{' BlocosCodigo '}' "
    tupleX=('IF', p[3],p[6])
    p[0]=tupleX

def p_BlocoIF_ELSE(p):
    " BlocoIF : IFELSE '(' ListaCondicionais ')' '{' BlocosCodigo '}' ELSE '{' BlocosCodigo '}'"
    tupleX=('IFELSE', p[3],p[6],p[10])
    p[0]=tupleX


def p_ListaCondicionais_fin(p):
    " ListaCondicionais : Condicional"
    #print('Parsing p_ListaCondicionais_fin '  , p[1])
    p[0]=p[1]
    
def p_ListaCondicionais_Capsulado(p):
    " ListaCondicionais : '(' ListaCondicionais ')' "
    
    p[0]=p[2]

def p_ListaCondicionais_Neg(p):
    "ListaCondicionais : '!' '(' ListaCondicionais ')'"
    tupleX=('!',p[3])
    p[0]=tupleX

def p_ListaCondicionais_Rec(p):
    " ListaCondicionais : ListaCondicionais OperadorLogico Condicional"
    
    tupleX=('OperacaoLogica',p[2],p[1],p[3])
    p[0]=tupleX
    #print('--------------')
    
    

def p_OperadorLogico_AND(p):
    "OperadorLogico : AND"
    #print('Parsing p_OperadorLogico_AND '  , p[1])
    p[0]=p[1]

def p_OperadorLogico_OR(p):
    "OperadorLogico : OR"
    #print('Parsing p_OperadorLogico_OR '  , p[1])
    p[0]=p[1]
    
    
    
    
def p_Condicional_Var(p):
    "Condicional : Var"
    #print('Parsing p_Condicional_Var '  , p[1])
    p[0]=p[1]
def p_Condicional_Neg(p):
    "Condicional : '!' '(' Condicional ')'"
    tupleX=('!',p[3])
    #print('Parsing p_Condicional_Neg '  , p[1])
    p[0]=tupleX
    
def p_Condicional_Capsulado(p):
    "Condicional : '(' Condicional ')'"
    p[0]=p[2]
    
def p_Condicional_OperadorCondicional(p):
    "Condicional : Condicional OperadorCondicional Condicional"
    tupleX= ( 'OperacaoCondicional' ,p[2],p[1],p[3] )
    #print('Parsing p_Condicional_OperadorCondicional '  , p[1])
    #a=p[2]
    #c=','.join(p[3])
    #print('OperacaoCondicional' ,a,b,c )
    p[0]=tupleX
    
def p_OperadorCondicional_Maior(p):
    "OperadorCondicional : '>'"
    #print('Parsing  p_OperadorCondicional_Maior'  , p[1])
    p[0]=p[1]    
def p_OperadorCondicional_BIGEQUAL(p):
    "OperadorCondicional : BIGEQUAL "
    #print('Parsing p_OperadorCondicional_BIGEQUAL '  , p[1])
    p[0]=p[1]    
def p_OperadorCondicional_MENOR(p):
    "OperadorCondicional : '<'"
    #print('Parsing  p_OperadorCondicional_MENOR'  , p[1])
    p[0]=p[1]    
def p_OperadorCondicional_LESSEREQUAL(p):
    "OperadorCondicional : LESSEREQUAL"
    #print('Parsing p_OperadorCondicional_LESSEREQUAL '  , p[1])
    p[0]=p[1]    
def p_OperadorCondicional_EQUALS(p):
    "OperadorCondicional : EQUALS"
    #print('Parsing p_OperadorCondicional_EQUALS '  , p[1])
    p[0]=p[1]

def p_OperadorCondicional_NOTEQUALS(p):
    "OperadorCondicional : NOTEQUALS"
    #print('Parsing p_OperadorCondicional_EQUALS '  , p[1])
    p[0]=p[1]
    
    
    ####---------------------------------WHILEDO-------------------------------------
def p_Codigo_BlocoWhileDo(p):
    "Codigo  : BlocoWhileDo"
    
    p[0]=p[1]   
    
def p_BlocoWhileDo(p):
    " BlocoWhileDo : WHILE  '(' ListaCondicionais ')' DO '{' BlocosCodigo '}'  "
    tupleX=('WHILE',p[3],'DO',p[7])
    p[0]=tupleX
    
    ####---------------------------------LERSTDIN-------------------------------------
def p_Codigo_LerSTDIN(p):
    "Codigo  : BlocoLerSTDIN"
    #print('Parsing p_Codigo_LerSTDIN' , p[1])
    p[0]=p[1]
    
def p_BlocoLerSTDIN(p):
    " BlocoLerSTDIN : ID '=' STDIN '(' ')' ';' "
    tupleX=('STDIN', p[1] )
    #print(','.join(tupleX))
    p[0]=tupleX

    ####---------------------------STDOUT-------------------------------------------
def p_Codigo_EscreverSTDOUT(p):
    "Codigo  : Bloco_EscreverSTDOUT"
    p[0]=p[1]   
    
def p_Bloco_EscreverSTDOUT(p):
    " Bloco_EscreverSTDOUT : STDOUT '(' Var ')' ';' "
    tupleX=('STDOUT',p[3])
    #a=  '('+','.join(p[3])+')'
    #print('STDOUT',a)
    p[0]=tupleX
    
def p_Bloco_EscreverSTDOUT_PAL(p):
    " Bloco_EscreverSTDOUT : STDOUT '(' PAL ')' ';' "
    tupleX=('STDOUTPAL',p[3])
    #a=  '('+','.join(p[3])+')'
    #print('STDOUT',a)
    p[0]=tupleX
        
    ####---------------------------Comentario-------------------------------------------
def p_Codigo_Comentario(p):
    "Codigo  : Bloco_Comentario"
    #print('Parsing p_Codigo_Comentario' , p[1])
    p[0]=p[1]   
    
def p_Bloco_Comentario(p):
    " Bloco_Comentario : COMMENT "
    #print('Parsing p_Bloco_Comentario '  , p[1])
    tupleX= ('COMMENT',p[1])
    p[0]=tupleX
    
    ####----------------------------------------------------------------------
    
    ####--------------------------DEFINEFUNC--------------------------------------------
def p_Codigo_DEFINEFUNC(p):
    "Codigo  : Bloco_DEFINEFUNC"
    #print('Parsing Bloco_DEFINEFUNC' , p[1])
    p[0]=p[1]   
    
def p_Bloco_DEFINEFUNC_EMPTY(p):
    " Bloco_DEFINEFUNC : DEFINE FUNC '(' ')' '{' BlocosCodigo '}'"
    #print('Parsing p_BlocoLerSTDIN '  , p[1])
    tupleX=('DEFINEEMPTY',p[2],p[6])
    p[0]=tupleX

def p_Bloco_DEFINEFUNC_Atributos(p):
    " Bloco_DEFINEFUNC : DEFINE FUNC '(' ListaAtributos  ')' '{' BlocosCodigo '}'"
    #print('Parsing p_BlocoLerSTDIN '  , p[1])
    tupleX=('DEFINEFILL', p[2],p[4],p[7])
    p[0]=tupleX
    
def p_ListaAtributos_fin(p):
    " ListaAtributos : Atributo"
    #print('Parsing p_BlocoLerSTDIN '  , p[1])
    tupleX=('Atributo',p[1])
    p[0]=tupleX

def p_ListaAtributos_Rec(p):
    " ListaAtributos : ListaAtributos ',' Atributo"
    #print('Parsing p_BlocoLerSTDIN '  , p[1])
    tupleX=('AtributoRec',p[1],p[3])
    p[0]=tupleX


def p_Atributo(p):
    " Atributo : INT"
    #print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]
    
    

    ####--------------------------Call_FUNC--------------------------------------------
def p_Codigo_CALLFUNC(p):
    "Codigo  : Bloco_CALLFUNC"
    p#rint('Parsing p_Codigo_CALLFUNC' , p[1])
    p[0]=p[1]
    
def p_Bloco_CALLFUNC_EMPTY(p):
    " Bloco_CALLFUNC : CALL FUNC '(' ')' ';'"
    tupleX=('CALLEMPTY',p[2])
    p[0]=tupleX
    
## CALL _isNUMBER_(x)
def p_Bloco_CALLFUNC_Atributos(p):
    " Bloco_CALLFUNC : CALL FUNC '(' INPUTVar  ')' ';' "
    tupleX=('CALLFILL',p[2],p[4])
    p[0]=tupleX  

def p_INPUTVar_fin(p):
    " INPUTVar : Var "
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]  

def p_INPUTVar_Rec(p):
    " INPUTVar : INPUTVar ',' Var "
    tupleX=('RecVar',p[1],p[3])
    p[0]=tupleX  

def p_error(p):
    parser.success = False
    print('Syntax error!', p)



###inicio do parsing
parser = yacc.yacc()
parser.success = True





#a1_Atribuicao= """INT x; x = (1+1)+2;"""

def assembliza(tupleX,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer):
    
    if (tupleX[0] == 'CodigoRec') :# ('Codigorec' ,BlocodeCodigo, Codigo )
        
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
       
        
    if (tupleX[0] == 'Declaracao') :#('Declaracao', 'INT', 'x')
        
        cabeca=cabeca + 'pushi 0\n'
        
        dict_var[tupleX[2]] = sp
        sp+=1
        
    
    if (tupleX[0] == 'Declaracao_e_Atribuicao') :#('Declaracao_e_Atribuicao',dec , atribuicao)
    
        cabeca=cabeca + 'pushi '+ str(tupleX[2][2][1][1]) +'\n'
        
        dict_var[tupleX[1][2]] = sp
        sp+=1
    
        
    
    if (tupleX[0] == 'Declaracao_STDIN') :#('Declaracao_STDIN', 'INT', ('STDIN', 'n'))
    
        if(delay):
            extra[extrapointer]=extra[extrapointer]+'read\natoi\n'
        else:
            corpo=corpo+'read\natoi\n'
            
        dict_var[tupleX[2][1]] = sp
        sp+=1



    if (tupleX[0] == 'Atribuicao') :#('Atribuicao', 'c', ('Var', ('NUM', '0')))
    
        
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        if(delay):
            extra[extrapointer]=extra[extrapointer]+'storeg '+ str(dict_var.get(tupleX[1])) + '\n'
            sp-=1
        else:
            corpo=corpo+'storeg '+ str(dict_var.get(tupleX[1])) + '\n'
            sp-=1
        
        
        
    if (tupleX[0] == 'Operacao') :#('Operacao', '-', ('Var', ('ID', 'n')), ('NUM', '1')))
    
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        if(delay):
            if(tupleX[1]=='-'):
                extra[extrapointer]=extra[extrapointer]+'sub\n'
                sp-=1

            if(tupleX[1]=='+'):
                extra[extrapointer]=extra[extrapointer]+'add\n'
                sp-=1

            if(tupleX[1]=='/'):
                extra[extrapointer]=extra[extrapointer]+'div\n'
                sp-=1

            if(tupleX[1]=='*'):
                extra[extrapointer]=extra[extrapointer]+'mul\n'
                sp-=1
            
            if(tupleX[1]=='%'):
                extra[extrapointer]=extra[extrapointer]+'mod\n'
                sp-=1
                
        else:
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
    
        if(delay):
            extra[extrapointer]=extra[extrapointer]+'read\n'+ 'storeg' +str(dict_var.get(tupleX[1])) + '\n'
            sp-=1
        else:
            corpo=corpo+'read\n'+'atoi\n'+ 'storeg ' +str(dict_var.get(tupleX[1])) + '\n'
            sp-=1
        
        
        
        
    if (tupleX[0] == 'OperacaoLogica'):
        cicleTag=contador_de_Ciclos
        
        
        if(tupleX[1]=='&&'):
            
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
            
            sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
            
            if(delay):
                if(tupleX[2][0] != 'OperacaoLogica'): extra[extrapointer]=extra[extrapointer]+'mul\n'
                if(tupleX[3][0] != 'OperacaoLogica'): extra[extrapointer]=extra[extrapointer]+'mul\n'
                
            else:   
                if(tupleX[2][0] != 'OperacaoLogica' or tupleX[3][0] != 'OperacaoLogica'): corpo=corpo+'mul\n'

                
        
        
        
    if (tupleX[0] == 'OperacaoCondicional') :#('OperacaoCondicional', '>', ('ID', 'n'), ('NUM', '0'))
        aux=""
        
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
            

        
        
        
        if(tupleX[1]=='>'):
            aux=aux+'sup' + '\n'
            sp+=1
            
        if(tupleX[1]=='<'):
            aux=aux+'inf' + '\n'
            sp+=1
    
        if(tupleX[1]=='=='):
            aux=aux+'equal' + '\n'
            sp+=1
        if(tupleX[1]=='!='):
            aux=aux+'equal' + '\n'+'NOT' + '\n'
            sp+=1
    
        if(delay):
                extra[extrapointer]=extra[extrapointer]+aux
        else:
                corpo=corpo+aux
    
    
    
       
    
    
        
        #print(tupleX)
    if (tupleX[0] == 'IF') :#('IF', ('OperacaoLogica', '&&', ('OperacaoLogica', '&&', ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'y')), ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'w'))), ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'z'))), ('STDOUT', ('ID', 'a')))
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        
        extraID=extrapointer
        extraIDNext=extraID+1
        
        
        
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
        #---------------
        #condição do if
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        aux+='jz ENDSimpleIF'+str(cicleID)+'\n'
        
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
        
        
        extrapointer=extraID
        delayaux=delay
        
       
            
        
        
        #Do de IF
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        delay=delayaux
        
        aux=aux+'ENDSimpleIF'+str(cicleID)+':       \n'
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
        extrapointer=extraID
        
        #
        
        
        
        
    if (tupleX[0] == 'IFELSE') :
    
        aux=""
        
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        extraIDNext=extraID+1
        
    
        
        #---------------
        #condição do if
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        
        if(delay):
            extra[extraID]=extra[extraID]+'jz ELSE'+str(cicleID)+'\n'

        else:
            corpo=corpo+'jz ELSE'+str(cicleID)+'\n'
        aux=""   
        
        #---------------
        #tarefas do IfELSE
        
        extrapointer=extraID
        
        delayaux=delay
        
        #---------------
        #tarefas do IfELSE --- DO
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
       # print(extra)
        extrapointer=extraID
        if(delay):
            extra[extraID]=extra[extraID]+'jump ENDIFELSE'+str(cicleID)+'\n'

        else:
            corpo=corpo+'jump ENDIFELSE'+str(cicleID)+'\n'
        aux=""   
        
        #---------------
        #tarefas do IfELSE --- ELSE
        #Else de IFElse
        if(delay):
            extra[extraID]=extra[extraID]+'ELSE'+str(cicleID)+':\n'

        else:
            corpo=corpo+'ELSE'+str(cicleID)+':\n'
        aux=""   
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        extrapointer=extraID
        
        delay=delayaux
        
        
        aux=aux+'ENDIFELSE'+str(cicleID)+':     \n'
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
    if (tupleX[0] == 'ID') :#('ID', 'x')
    
        aux='pushg '+str(dict_var.get(tupleX[1]))+'\n'
    
        if(delay):
                extra[extrapointer]=extra[extrapointer]+aux
        else:
                corpo=corpo+aux
        
        
    if (tupleX[0] == 'STDOUTPAL') :
        
        if(delay):
            extra[extrapointer]=extra[extrapointer]+'pushs '+tupleX[1]+'\n' +'writes\n'
        else:
            corpo=corpo+'pushs '+tupleX[1]+'\n' +'writes\n'

    if (tupleX[0] == 'STDOUT') :#('STDOUT', ('ID', 'x')) 
        
        if(tupleX[1][0]=='ID'):
            if(delay):
                extra[extrapointer]=extra[extrapointer]+'pushg '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\n' 
            else:
                corpo=corpo+'pushg '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\n'
        
        if(tupleX[1][0]=='NUM'):
            if(delay):
                extra[extrapointer]=extra[extrapointer]+'pushi '+ dict_var.get(tupleX[1][1])+'\n' + 'writei\n' 
            else:
                corpo=corpo+'pushi '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\n' 
                
        if(tupleX[1][0]=='TRUE'):
            if(delay):
                extra[extrapointer]=extra[extrapointer]+'pushs "TRUE" ' +'\n' + 'writes\n' 
            else:
                corpo=corpo+'pushs "TRUE" '+'\n' + 'writes\n' 
        if(tupleX[1][0]=='FALSE'):
            if(delay):
                extra[extrapointer]=extra[extrapointer]+'pushs "FALSE" '+ +'\n' + 'writes\n' 
            else:
                corpo=corpo+'pushs "FALSE" '+'\n' + 'writes\n' 
            
           
            
            
            
           
        
        
    if (tupleX[0] == 'COMMENT') :#('COMMENT', '*/ atenção aqui estou ainda a pensar como garantir que o numero é INT /*')
        
        
        print('found comment')
        
    
        
        
    if (tupleX[0] == 'Var') : #('Var', ('ID', 'x'))
    
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
    
            
            
        
    if (tupleX[0] == 'WHILE') :#('WHILE', ('OperacaoCondicional', '==', ('ID', 'x'), ('ID', 'x')), 'DO', ('Declaracao', 'INT', 'y'))
        aux=""
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        extraIDNext=extraID+1
        
        
        aux=aux+'While'+str(cicleID)+':            \n'
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
        extrapointer=extraID
        #Condição de While
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        extrapointer=extraID
        aux=aux+'jz EndOfWhile'+str(cicleID)+'\n'
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
        
        delayaux=delay
        
        extrapointer=extraID
        
        
        #Do de While
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        aux=aux+'jump While'+str(cicleID)+'\n'
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        delay = delayaux
        
        aux=aux+'EndOfWhile'+str(cicleID)+':         \n'
        if(delay):
            extra[extraID]=extra[extraID]+aux
        else:
            corpo=corpo+aux
        aux=""
        
        
    
        #print(tupleX)
    if (tupleX[0] == 'NUM') :#('NUM', '1')
        aux='pushi '+str(tupleX[1])+'\n'
    
        if(delay):
                extra[extrapointer]=extra[extrapointer]+aux
        else:
                corpo=corpo+aux
    
        
        #print('pushi',tupleX[1])
    
    
        
        
    return sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer

# é preciso ter em atenção a ordem da recursividade e que algumas das cenas devemos verificar se tem outros tuplos dentro
    



        
perguntaX="""
INT x = 1;
WHILE(x==1)
DO{

IF(x==1)
    {
     IF(x==1){x=6;}x=8;
    
    
    }
ELSE{
INT y=2;}}
y=10;

"""
 



pergunta = pList[1]#pergunta_2#a3_WHILEDO



dict_var = {}
l=[]
contador_de_Ciclos=0
sp=0
extrapointer=0
cabeca=""
corpo=""
extra=["","","","","","","",""]



print('--------Pergunta--------\n')

print(pergunta)
print('--------Estrutura Parsed--------\n')
struct_to_assemblizar=parser.parse(pergunta)
print(struct_to_assemblizar)
if parser.success:

   print('Parsing completed!\n')
   



sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer= assembliza(struct_to_assemblizar,sp,contador_de_Ciclos,False,cabeca,corpo,extra,dict_var,extrapointer)


    
print('--------Dicionário de Variaveis:-----')
print(dict_var)
print('--------Assembly Code:-----\n')


print(cabeca)

print('start')
print(corpo)
print('stop')
print('--------extra:-----')
ecna=0
for i in extra:
    print('------------------------extra',ecna,':-----')
    print(i)
    ecna+=1

