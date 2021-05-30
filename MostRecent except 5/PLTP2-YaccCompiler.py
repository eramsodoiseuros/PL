

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
    
def p_Declaracao_AtribuicaoR(p):
    "Declaracao :  INTR ID '=' Expressao ';'"
    tupleX= ('Declaracao_e_AtribuicaoReturn',p[2])
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

def p_BlocoLerSTDIN_STRUCTARRAY(p):
    " BlocoLerSTDIN : STRUCTARRAY ID ID '=' STDIN '(' ')' ';' "
    tupleX=('STRUCTARRAY_STDIN', p[2],p[3] )
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
    
def p_Bloco_EscreverSTDOUT_STRUCTARRAY(p):
    " Bloco_EscreverSTDOUT : STDOUT '(' STRUCTARRAY ID ID ')' ';' "
    tupleX=('STRUCTARRAY_STDOUT',p[4],p[5])
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
def p_Codigo_Return(p):
    "Codigo  : Bloco_Return"
    #print('Parsing p_Codigo_Comentario' , p[1])
    p[0]=p[1]   
    
def p_Bloco_ReturnID(p):
    " Bloco_Return : RETURN ID ';' "
    #print('Parsing p_Bloco_Comentario '  , p[1])
    tupleX= ('RETURNID',p[2])
    p[0]=tupleX

def p_Bloco_ReturnNUM(p):
    " Bloco_Return : RETURN NUM ';' "
    #print('Parsing p_Bloco_Comentario '  , p[1])
    tupleX= ('RETURNNUM',p[2])
    p[0]=tupleX
    
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

def p_Bloco_CALLFUNC_EMPTYID(p):
    " Bloco_CALLFUNC :  ID '=' CALL FUNC '(' ';' ')' ';'"
    tupleX=('CALLEMPTYID',p[1],p[4])
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


def p_Codigo_ARRAY(p):
    "Codigo  :  Array "
    p[0]=p[1]

def p_Codigo_ARRAYNUM(p):
    "Array  :  ARRAYNUM NUM ID ';' "
    tupleX=('ARRAYNUM',p[2],p[3])
    p[0]=tupleX
    
def p_Codigo_ARRAYID(p):
    "Array  :  ARRAYID ID ID ';' "
    tupleX=('ARRAYID',p[2],p[3])
    p[0]=tupleX


def p_Codigo_BlocoFOR(p):
    "Codigo  : BlocoFOR"
    
    p[0]=p[1]   
    
def p_BlocoFOR(p):
    " BlocoFOR : FOR ID  '(' Condicional ')'  Atribuicao  '{' BlocosCodigo '}'  "
    tupleX=('FOR',p[2],p[4],p[6],p[8])
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
        
    
        if(tupleX[2] in dict_var): print('TESTE')
            
        else:
            cabeca=cabeca + 'pushi 0\n'
            
            dict_var[tupleX[2]] = sp
            sp+=1
        
    
    if (tupleX[0] == 'Declaracao_e_Atribuicao') :#('Declaracao_e_Atribuicao',dec , atribuicao)
    
        cabeca=cabeca + 'pushi '+ str(tupleX[2][2][1][1]) +'\n'
        
        dict_var[tupleX[1][2]] = sp
        sp+=1
    
        
    
    if (tupleX[0] == 'Declaracao_STDIN') :#('Declaracao_STDIN', 'INT', ('STDIN', 'n'))
    
        
        corpo=corpo+'read\natoi\n'
            
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
            #print(tupleX)
        
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
    
        corpo=corpo+aux
    
    
    
       
    
    
        
        #print(tupleX)
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
        
        
        aux+='jz ENDSimpleIF'+str(cicleID)+'\n'
        
        corpo=corpo+aux
        aux=""
        
        
        
        extrapointer=extraID
        delayaux=delay
        
       
            
        
        
        #Do de IF
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[2],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        delay=delayaux
        
        aux=aux+'ENDSimpleIF'+str(cicleID)+':       \n'
        
        corpo=corpo+aux
        aux=""
        
        extrapointer=extraID
        
        #
        
        
        
        
    if (tupleX[0] == 'IFELSE') :
    
        aux=""
        
        contador_de_Ciclos+=1
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
    
        
        #---------------
        #condição do if
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        
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
        corpo=corpo+'jump ENDIFELSE'+str(cicleID)+'\n'
        aux=""   
        
        #---------------
        #tarefas do IfELSE --- ELSE
        #Else de IFElse
        corpo=corpo+'\tELSE'+str(cicleID)+':\n'
        aux=""   
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[3],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        extrapointer=extraID
        
        delay=delayaux
        
        
        aux=aux+'ENDIFELSE'+str(cicleID)+':     \n'
        corpo=corpo+aux
        aux=""
        
    if (tupleX[0] == 'ID') :#('ID', 'x')
    
        aux='pushg '+str(dict_var.get(tupleX[1]))+'\n'
        sp+=1
        corpo=corpo+aux
        
        
    if (tupleX[0] == 'STDOUTPAL') :
        
        corpo=corpo+'pushs '+tupleX[1]+'\n' +'writes\n'
        sp+=1
    if (tupleX[0] == 'STDOUT') :#('STDOUT', ('ID', 'x')) 
        
        if(tupleX[1][0]=='ID'):
            
                corpo=corpo+'pushg '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\n'
                
        
        if(tupleX[1][0]=='NUM'):
            corpo=corpo+'pushi '+ str(dict_var.get(tupleX[1][1]))+'\n' + 'writei\n' 
            
                
        if(tupleX[1][0]=='TRUE'):
            corpo=corpo+'pushs "TRUE" '+'\n' + 'writes\n'
            
        if(tupleX[1][0]=='FALSE'):
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
        
        
        aux=aux+'While'+str(cicleID)+':            \n'
        corpo=corpo+aux
        aux=""
        
        extrapointer=extraID
        #Condição de While
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tupleX[1],sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        extrapointer=extraID
        aux=aux+'jz EndOfWhile'+str(cicleID)+'\n'
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
        
        aux=aux+'EndOfWhile'+str(cicleID)+':         \n'
        corpo=corpo+aux
        aux=""
        
        
    
        #print(tupleX)
    if (tupleX[0] == 'NUM') :#('NUM', '1')
        aux='pushi '+str(tupleX[1])+'\n'
        sp+=1#
        corpo=corpo+aux
        
        
    if (tupleX[0] == 'ARRAYNUM') :#ARRAYNUM NUM ID ';' "  DONE
        cabeca=cabeca + 'pushn '+ tupleX[1]+'\n'
        
        dict_var[tupleX[2]] = sp
        sp+=1
    
    if (tupleX[0] == 'ARRAYID') :#ARRAYID ID ID ';' "
        print(tupleX)
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
        aux=aux+'\tFor'+str(cicleID)+':\n'
        corpo=corpo+aux
        aux=""
        
        #assembliza-codigo da condição 
        tuplexAux= tupleX[2]
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        #+ jz para fim
        aux=aux+'jz EndOfFor'+str(cicleID)+'\n'
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
        aux=aux+'\tEndOfFor'+str(cicleID)+':\n'
        corpo=corpo+aux
        aux=""
        
        
        
        
    if (tupleX[0] == 'STRUCTARRAY_STDIN') :#('STRUCTARRAY_STDIN', p[2],p[3] )
        print(tupleX)
        cicleID = contador_de_Ciclos
        variavel_array=tupleX[1]
        variavel_indice=tupleX[2]
        
        
        #('FOR', 'j', ('OperacaoCondicional', '<', ('ID', 'j'), ('ID', 'tamanho')), ('Atribuicao', 'j', ('Operacao', '+', ('Var', ('ID', 'j')), ('NUM', '1'))), ('Atribuicao', 'i', ('Var', ('NUM', '0')))))
        
        tuplexAux= ('FOR_ARRAY_STDIN',  variavel_indice, variavel_array)
        sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer = assembliza_ARRAY(tuplexAux,sp,contador_de_Ciclos,delay,cabeca,corpo,extra,dict_var,extrapointer)
        
        
        #ciclo For Para Criar Array
        
        
        sp+=1
    if (tupleX[0] == 'STRUCTARRAY_STDOUT') :#ARRAYID ID ID ';' "
        
        cicleID = contador_de_Ciclos
        variavel_array=tupleX[1]
        variavel_indice=tupleX[2]
        
        dict_var[variavel_array] = sp
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
        sp-=1
        sp+=1
        corpo=corpo+aux
        aux=""
    if (tupleX[0] == 'RETURN') :#('RETURN', "1")
        aux=""
        cicleID = contador_de_Ciclos
        extraID=extrapointer
        
        aux=aux+'pushi '+str(tupleX[1])+'\nstorel -1\n\n'
        corpo=corpo+aux
        sp-=1
        sp+=1
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
        
        
        aux=aux+'pushi 1\npusha '+str(tupleX[2])+'\ncall\nnop\npushs "\\na funcao devolveu:\\n"\nwrites\nwritei\npushs "\\ndebug :FIM\\n"\nwrites\n'
        
        corpo=corpo+aux
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
        print('EXEMPLO::::',dict_varaux)
        print(cabecaaux)
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
        aux=aux+'pushg '+str(dict_var.get(tamanho))+'\nsup\n'
        corpo=corpo+aux
        aux=""
        
        #+ jz para fim
        aux=aux+'jz EndOfForArray'+str(cicleID)+'\n'
        corpo=corpo+aux
        aux=""
        #assembliza-BlocoCodigo
        aux=aux+'pushi 0\n'
        corpo=corpo+aux
        aux=""
        
        #assembliza-Operacao
        aux=aux+'pushg '+str(dict_var.get(indice))+'\n\n'
        aux=aux+'pushi 1\nadd\n'
        aux=aux+'storeg '+str(dict_var.get(indice))+'\n\n'
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
        nome = tupleX[1]
        indice = tupleX[2]
        
        
        #
        aux=aux+'pushgp\npushi '+str(dict_var.get(nome))+'\npadd\n'
        aux=aux+'pushi  '+str(dict_var.get(indice))+'\n'
        aux=aux+'read\natoi\nstoren\n\n'
        corpo=corpo+aux
        aux=""
        
        
       
    if (tupleX[0] == 'FOR_ARRAY_STDOUT') :#('FOR', indice , tamanho )
        aux="" 
        nome = tupleX[1]
        indice = tupleX[2]
        
        
        #
        aux=aux+'pushgp\npushi '+str(dict_var.get(nome))+'\npadd\n'
        aux=aux+'pushi  '+str(dict_var.get(indice))+'\n'
        aux=aux+'load\nwritei\n'
        corpo=corpo+aux
        aux=""
        
        
    
    
    
    return sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer




        
pergunta5="""


INT tt = 5;
INT tamanho = 4;

ARRAYID tt v;

"""



aaaa=""" 

FOR j (j < tamanho) j=j+1; {
   i = 0;
}

FOR i (i < tamanho) i=1+i; {
    STRUCTARRAY v i = STDIN();
}

FOR c (c < tamanho) c=c-1; {
    STDOUT(STRUCTARRAY v c);
}

"""



pergunta = pList[5]#pergunta_2#a3_WHILEDO# pergunta5#



dict_var = {}
l=[]
contador_de_Ciclos=0
sp=0
extrapointer=0
cabeca=""
corpo=""
extra=[]#"","","","","","","",""]



print('--------Pergunta--------\n')

print(pergunta)
print('--------Estrutura Parsed--------\n')
struct_to_assemblizar=parser.parse(pergunta)
print(struct_to_assemblizar)
if parser.success:

   print('Parsing completed!\n')
   



sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer= assembliza(struct_to_assemblizar,sp,contador_de_Ciclos,False,cabeca,corpo,extra,dict_var,extrapointer)


    
print('/*--------Dicionário de Variaveis:-----*/')
print('/*',dict_var,'*/')
print('/*--------Assembly Code:-----*/')

final=""
print(cabeca)
final+=cabeca+'start'+corpo+'stop'
print('start')
print(corpo)
print('stop')
#print('/*--------extra:-----*/')
ecna=0
for i in extra:
    #print('/*------------------------extra',ecna,':-----*/')
    final+=i
    print(i)
    ecna+=1

f = open("pFile.vm", "a")
f.write(final)
f.close()