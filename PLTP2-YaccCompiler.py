from PLTP02_lex import tokens
from PLTP02_Assembliza import assembliza
import ply.yacc as yacc
import sys
import os

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
    p[0]=p[1]

def p_BlocosCodigo_Rec(p):
    "BlocosCodigo  :  BlocosCodigo Codigo "
    tupleX=('CodigoRec',p[1],p[2])
    p[0]=tupleX

### ----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

def p_Expressao_Rec1(p):
    " Expressao : Expressao Operador Var "
    tupleX = ('Operacao',p[2],p[1],p[3])
    p[0]=tupleX

def p_Expressao_Rec2(p):
    " Expressao : '(' Expressao  ')' "
    
    p[0]=p[2]
    
####----------------------------------------------------------------------
    
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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

def p_OperadorLogico_AND(p):
    "OperadorLogico : AND"
    #print('Parsing p_OperadorLogico_AND '  , p[1])
    p[0]=p[1]

def p_OperadorLogico_OR(p):
    "OperadorLogico : OR"
    #print('Parsing p_OperadorLogico_OR '  , p[1])
    p[0]=p[1]

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

def p_Codigo_BlocoWhileDo(p):
    "Codigo  : BlocoWhileDo"
    
    p[0]=p[1]   
    
def p_BlocoWhileDo(p):
    " BlocoWhileDo : WHILE  '(' ListaCondicionais ')' DO '{' BlocosCodigo '}'  "
    tupleX=('WHILE',p[3],'DO',p[7])
    p[0]=tupleX

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

def p_Codigo_CALLFUNC(p):
    "Codigo  : Bloco_CALLFUNC"
    p[0]=p[1]
    
def p_Bloco_CALLFUNC_EMPTY(p):
    " Bloco_CALLFUNC : CALL FUNC '(' ')' ';'"
    tupleX=('CALLEMPTY',p[2])
    p[0]=tupleX

def p_Bloco_CALLFUNC_EMPTYID(p):
    " Bloco_CALLFUNC :  ID '=' CALL FUNC '(' ';' ')' ';'"
    tupleX=('CALLEMPTYID',p[1],p[4])
    p[0]=tupleX

def p_Bloco_CALLFUNC_Atributos(p):
    " Bloco_CALLFUNC : CALL FUNC '(' INPUTVar  ')' ';' "
    tupleX=('CALLFILL',p[2],p[4])
    p[0]=tupleX  

####----------------------------------------------------------------------

def p_INPUTVar_fin(p):
    " INPUTVar : Var "
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]  

def p_INPUTVar_Rec(p):
    " INPUTVar : INPUTVar ',' Var "
    tupleX=('RecVar',p[1],p[3])
    p[0]=tupleX  

####----------------------------------------------------------------------

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

####----------------------------------------------------------------------

def p_error(p):
    parser.success = False
    print('Syntax error!', p)


####----------------------------------------------------------------------


###inicio do parsing
parser = yacc.yacc()
parser.success = True

def main():
    
    if not os.path.exists('PastaAssembly'):
        os.mkdir('PastaAssembly')
    
    nomeFileAbrir = input("Selecione o Nome do Programa: ")   # Python 3
    with open('Perguntas/'+str(nomeFileAbrir)+'.txt','r') as file:
        pergunta = file.read()
    print(pergunta)
    
    dict_var = {}
    l = []
    contador_de_Ciclos = 0
    sp = 0
    extrapointer = 0
    cabeca = ""
    corpo = ""
    extra = []

    print('--------Estrutura Parsed--------\n')
    struct_to_assemblizar=parser.parse(pergunta)
    print(struct_to_assemblizar)
    if parser.success:
       print('Parsing completed!\n')
    
    sp,cabeca,corpo,extra,contador_de_Ciclos,delay,dict_var,extrapointer= assembliza(struct_to_assemblizar,sp,contador_de_Ciclos,False,cabeca,corpo,extra,dict_var,extrapointer)
     
    print('\n/*--------Dicionário de Variaveis:-----*/\n')
    print('/*',dict_var,'*/')
    print('\n/*--------Assembly Code:-----*/\n')
    
    final=""
    #print(cabeca)
    final+=cabeca+'\n\tstart\n'+corpo+'\n\tstop\n'
    #print('start')
    #print(corpo)
    #print('stop')
    #print('/*--------extra:-----*/')
    ecna=0
    for i in extra:
        #print('/*------------------------extra',ecna,':-----*/')
        final+=i
        #print(i)
        ecna+=1
    print(final)

    nomeFileAbrir = input("SELECIONE o nome final do ficheiro: ") 
    nomeHtml= 'PastaAssembly'+'/'+nomeFileAbrir+'.vm'
    f = open(nomeHtml, "a")
    
    assembly = ""
    for linha in final.split('\n'):
        if '\t' in linha:
            assembly = assembly + linha[1:] + '\n'
        else: 
            assembly = assembly + '\t' + linha + '\n'
    f.write(assembly)
    f.close()
    print()

if __name__ == "__main__":
    main()