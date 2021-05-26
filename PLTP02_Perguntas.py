#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 16:34:10 2021

@author: G30
"""


#Perguntas 

pergunta_1= """ 
INT x = STDIN();
INT y = STDIN();
INT w = STDIN();
INT z = STDIN();



IFELSE((x==y)&&(x==w)&&(x==z)) { STDOUT(TRUE); }  ELSE { STDOUT(FALSE); }
"""

 


pergunta_2=""" 
INT n ;

n = STDIN();
INT y;
INT x;

IFELSE (n > 1) 
{
    y = STDIN();
    n = n - 1;
    WHILE(n > 0) DO 
    {
        IFELSE(n == 1) 
        {
            x = STDIN();
            IFELSE(x < y) 
            {
                STDOUT(x);
            } 
            ELSE 
            {
                STDOUT(y);
            }
        } 
        ELSE {
            x = STDIN();
            IF(x < y) {
                y = x;
            }
        }

        n = n - 1;
    }

} 
ELSE 
{

    IF(n == 1)
    {
        x = STDIN();
        STDOUT(x);
    } 
} """
        


p_extra="""


INT n = STDIN();
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
INT n = 10;
INT novo ;

INT total = 1;

WHILE(n > 0) DO { 
    novo = STDIN();
    total = total*novo;
    n = n-1; 
}
    
STDOUT(total);"""

pergunta_4=""" 
INT conta = 0;
INT aux;
INT atual = 1;
INT fim = 8;

STDOUT("INICIO");

WHILE( atual != fim ) DO { 
    aux = atual % 2;
    
    IF( aux != 0 ) {
        conta = conta + 1;
        STDOUT(atual);
    }
    atual = atual + 1;
}

STDOUT("FIM"); """


pList=[pergunta_1,pergunta_2,pergunta_3,pergunta_4]











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
     