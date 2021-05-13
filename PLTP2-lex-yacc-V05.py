import ply.yacc as yacc
import sys
import ply.lex as lex

tokens=['INT','ID','NUM','IF','OR','AND','BIGEQUAL','LESSEREQUAL','EQUALS','WHILE','DO','STDIN','STDOUT','COMMENT','NOTEQUALS','TRUE','FALSE','DEFINE','FUNC', 'CALL']

literals=('=', '+','-','*','/','%', ';', '!', '>','<',')','(','{','}')

t_INT = r'INT'
t_IF = r'IF'
t_WHILE = r'WHILE'
t_DO = r'DO'
t_CALL = r'CALL'
t_DEFINE = r'DEFINE'
t_TRUE = r'TRUE'
t_FALSE = r'FALSE'
t_STDIN = r'STDIN'
t_STDOUT = r'STDOUT'
t_ID= r'[a-z]'
t_NUM = r'\d+'
t_OR = r'\|\|'
t_AND = r'\&\&'
t_BIGEQUAL = r'>='
t_LESSEREQUAL = r'<='
t_EQUALS = r'=='
t_NOTEQUALS= r'!='
t_COMMENT = r'\*\/[^\/\*]*/\*'
t_FUNC = r'\_\w+\_'



#t_ = r''

t_ignore  = ' \n\t'

def t_error(t):
    print('Illegal character: %s', t.value[0])

lexer = lex.lex()

def p_Programa(p):
    "Programa : BlocosCodigo"
    #print('Parsing completed succesfully! Value synthesized: ', p[1])
    
    
    ####----------------------------------------------------------------------
def p_BlocoCodigo_fin(p):
    "BlocosCodigo  :  Codigo "
    #print('Parsing Codigo succesfully! ID DID' , p[1])
    p[0]=p[1]

def p_BlocosCodigo_Rec(p):
    "BlocosCodigo  :  BlocosCodigo Codigo "
    #print('Parsing Codigo succesfully! ID DID' , p[1])
    p[0]=p[1]
    
    ####----------------------------------------------------------------------
### p_Declaracao

def p_Codigo_Declaracao(p):
    "Codigo  :  Declaracao "
    #print('Parsing Declaracao' , p[1])
    p[0]=p[1]
    
def p_Declaracao(p):
    "Declaracao :  INT ID ';' "
    tupleX= ('Declaracao',p[1],p[2])
    print(','.join(tupleX))
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
    a=','.join(p[1])
    b=','.join(p[3])
    print('Atribuicao',a,b)
    p[0]=tupleX
    
def p_Atribuicao_FUNC(p):
    " Atribuicao : ID '=' Bloco_CALLFUNC "
    a=','.join(p[1])
    b=','.join(p[3])
    print('Atribuicao',a,b)
    p[0]=tupleX



def p_Expressao_fin(p):
    " Expressao : Var "
    p[0]=p[1]

def p_Var_NUM(p):
    " Var : NUM "
    tupleX = ('Var',p[1])
    print(','.join(tupleX))
    p[0]=tupleX
    
def p_Var_ID(p):
    " Var : ID "
    tupleX = ('Var',p[1])
    print(','.join(tupleX))
    p[0]=tupleX
def p_Var_TRUE(p):
    " Var : TRUE "
    tupleX = ('Var',p[1])
    print(','.join(tupleX))
    p[0]=tupleX
def p_Var_FALSE(p):
    " Var : FALSE "
    tupleX = ('Var',p[1])
    print(','.join(tupleX))
    p[0]=tupleX

def p_Expressao_Rec1(p):
    " Expressao : Expressao Operador Var "
    print('Parsing p_Expressao_Rec1' , p[1])
    p[0]=p[1]

def p_Expressao_Rec2(p):
    " Expressao : '(' Expressao  ')' "
    print('Parsing p_Expressao_Rec2' , p[1])
    p[0]=p[1]
    
def p_Operador_MAIS(p):
    " Operador : '+' "
    print('Parsing p_Operador_MAIS' , p[1])
    p[0]=p[1]

def p_Operador_Minus(p):
    " Operador : '-' "
    print('Parsing p_Operador_Minus' , p[1])
    p[0]=p[1]
def p_Operador_MUL(p):
    " Operador : '*' "
    print('Parsing p_Operador_MUL' , p[1])
    p[0]=p[1]
def p_Operador_Div(p):
    " Operador : '/' "
    print('Parsing p_Operador_Div' , p[1])
    p[0]=p[1]
def p_Operador_Rest(p):
    " Operador : '%' "
    print('Parsing p_Operador_Rest' , p[1])
    p[0]=p[1]


    ####----------------------------------IF------------------------------------
def p_Codigo_BlocoIF(p):
    "Codigo  : BlocoIF"
    print('Parsing BlocoIF' , p[1])
    p[0]=p[1]   


    
def p_BlocoIF(p):
    " BlocoIF : IF '(' ListaCondicionais ')' '{' BlocosCodigo '}' "
    print('Parsing BlocoIF '  , p[1])
    p[0]=p[1]

def p_ListaCondicionais_fin(p):
    " ListaCondicionais : Condicional"
    print('Parsing p_ListaCondicionais_fin '  , p[1])
    p[0]=p[1]
    
def p_ListaCondicionais_Capsulado(p):
    " ListaCondicionais : '(' ListaCondicionais ')' "
    print('Parsing p_ListaCondicionais_fin '  , p[1])
    p[0]=p[1]

def p_ListaCondicionais_Neg(p):
    "ListaCondicionais : '!' '(' ListaCondicionais ')'"
    print('Parsing p_Condicional_Neg '  , p[1])
    p[0]=p[1]

def p_ListaCondicionais_Rec(p):
    " ListaCondicionais : ListaCondicionais OperadorLogico Condicional"
    print('Parsing p_ListaCondicionais_Rec '  , p[1])
    p[0]=p[1]

def p_OperadorLogico_AND(p):
    "OperadorLogico : AND"
    print('Parsing p_OperadorLogico_AND '  , p[1])
    p[0]=p[1]

def p_OperadorLogico_OR(p):
    "OperadorLogico : OR"
    print('Parsing p_OperadorLogico_OR '  , p[1])
    p[0]=p[1]
    
    
def p_Condicional_Var(p):
    "Condicional : Var"
    print('Parsing p_Condicional_Var '  , p[1])
    p[0]=p[1]
def p_Condicional_Neg(p):
    "Condicional : '!' '(' Condicional ')'"
    print('Parsing p_Condicional_Neg '  , p[1])
    p[0]=p[1]
    
def p_Condicional_Capsulado(p):
    "Condicional : '(' Condicional ')'"
    print('Parsing p_Condicional_Capsulado '  , p[1])
    p[0]=p[1]
    
def p_Condicional_OperadorCondicional(p):
    "Condicional : Condicional OperadorCondicional Condicional"
    print('Parsing p_Condicional_OperadorCondicional '  , p[1])
    p[0]=p[1]
    
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
    print('Parsing p_Codigo_BlocoWhileDo' , p[1])
    p[0]=p[1]   
    
def p_BlocoWhileDo(p):
    " BlocoWhileDo : WHILE  '(' ListaCondicionais ')' DO '{' BlocosCodigo '}'  "
    print('Parsing p_BlocoWhileDo '  , p[1])
    p[0]=p[1]    
    
    ####---------------------------------LERSTDIN-------------------------------------
def p_Codigo_LerSTDIN(p):
    "Codigo  : BlocoLerSTDIN"
    #print('Parsing p_Codigo_LerSTDIN' , p[1])
    p[0]=p[1]   
    
def p_BlocoLerSTDIN(p):
    " BlocoLerSTDIN : ID '=' STDIN '(' ')' ';' "
    tupleX=('STDIN', p[1] )
    print(','.join(tupleX))
    p[0]=p[1]

    ####---------------------------STDOUT-------------------------------------------
def p_Codigo_EscreverSTDOUT(p):
    "Codigo  : Bloco_EscreverSTDOUT"
    p[0]=p[1]   
    
def p_Bloco_EscreverSTDOUT(p):
    " Bloco_EscreverSTDOUT : STDOUT '(' Var ')' ';' "
    tupleX=('STDOUT',p[3])
    a=  '('+','.join(p[3])+')'
    print('STDOUT',a)
    p[0]=p[4]
        
    ####---------------------------Comentario-------------------------------------------
def p_Codigo_Comentario(p):
    "Codigo  : Bloco_Comentario"
    print('Parsing p_Codigo_Comentario' , p[1])
    p[0]=p[1]   
    
def p_Bloco_Comentario(p):
    " Bloco_Comentario : COMMENT "
    print('Parsing p_Bloco_Comentario '  , p[1])
    p[0]=p[1]
    
    ####----------------------------------------------------------------------
    
    ####--------------------------DEFINEFUNC--------------------------------------------
def p_Codigo_DEFINEFUNC(p):
    "Codigo  : Bloco_DEFINEFUNC"
    print('Parsing Bloco_DEFINEFUNC' , p[1])
    p[0]=p[1]   
    
def p_Bloco_DEFINEFUNC_EMPTY(p):
    " Bloco_DEFINEFUNC : DEFINE FUNC '(' ')' '{' BlocosCodigo '}'"
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]

def p_Bloco_DEFINEFUNC_Atributos(p):
    " Bloco_DEFINEFUNC : DEFINE FUNC '(' ListaAtributos  ')' '{' BlocosCodigo '}'"
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]
    
def p_ListaAtributos_fin(p):
    " ListaAtributos : Atributo"
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]

def p_ListaAtributos_Rec(p):
    " ListaAtributos : ListaAtributos ',' Atributo"
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]


def p_Atributo(p):
    " Atributo : INT"
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]
    
    

    ####--------------------------Call_FUNC--------------------------------------------
def p_Codigo_CALLFUNC(p):
    "Codigo  : Bloco_CALLFUNC"
    print('Parsing p_Codigo_CALLFUNC' , p[1])
    p[0]=p[1]   
    
def p_Bloco_CALLFUNC_EMPTY(p):
    " Bloco_CALLFUNC : CALL FUNC '(' ')' ';'"
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]
## CALL _isNUMBER_(x)
def p_Bloco_CALLFUNC_Atributos(p):
    " Bloco_CALLFUNC : CALL FUNC '(' INPUTVar  ')' ';' "
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]    

def p_INPUTVar_fin(p):
    " INPUTVar : Var "
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1]  

def p_INPUTVar_Rec(p):
    " INPUTVar : INPUTVar ',' Var "
    print('Parsing p_BlocoLerSTDIN '  , p[1])
    p[0]=p[1] 

def p_error(p):
    parser.success = False
    print('Syntax error!', p)

    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
#Perguntas 

pergunta_1= """ 
INT x;
INT y;
INT w;
INT z;

x = STDIN();
y = STDIN();
w = STDIN();
z = STDIN();

IF((x==y)&&(x==w)&&(x==z)) { STDOUT(a); } 
IF (!((x==y)&&(x==w)&&(x==z)&&(y==w)&&(y==z)&&(z==w))) { STDOUT(x) ; }"""

 
pergunta_2=""" 
INT n ;
n = STDIN();
INT x;
INT y;
x = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999;


WHILE (n > 0)  DO {  
    n = n - 1 ;
    y = STDIN();
    IF( y < x ) { x = y ; }
    }

STDOUT(x);"""



pergunta_3=""" 
INT n ; n = 5+1 ; INT x ; x = 1;
INT y ;

WHILE(n >0) 
DO { 
    n = n-1; 
    y = STDIN();
    x = x*y;
    }
    
STDOUT(x);"""

pergunta_4=""" 
INT x;
INT c;
INT a;
c = 0;
x= STDIN();
a = CALL _isNUMBER_(x);
WHILE( a )  
DO { a= x % 2;  */ atenção aqui estou ainda a pensar como garantir que o numero é INT /*
    IF(( a != 0 ))
        {
        c = c +1;
        STDOUT(x);
        }
    }
STDOUT(c); """

#pergunta_5=""" """


    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------
    ####----------------------------------------------------------------------







###inicio do parsing
parser = yacc.yacc()
parser.success = True




a1_Declaracao_e_Atribuicao= """INT i ; x = (1+1)+2;"""
a2_IF= """IF(x>x){INT y;}"""
a3_WHILEDO= """WHILE(x==x) DO{INT y;}"""
a4_STDIN= """x = STDIN() ; """
a5_STDOUT= """ STDOUT(x) ; """
a6_Comentario= """*/ AAASQDA< /*"""


aCompleto = """INT i ; x = (1+1)+2; z=TRUE;
                IF(x==x){INT y;}
                WHILE(x==x) DO{INT y;*/ AAASQDA< /*}
                x = STDIN() ;*/ Teste STDIN /*
                
                STDOUT(x) ; */ Teste STDOUT /*
                """


fonte = aCompleto


     



fonteoption=    """
     for linha in sys.stdinb():
         source+= linha
     result = parser.parse(source)
     """
     
     
parser.parse(pergunta_1)
if parser.success:
   print('Parsing completed!')