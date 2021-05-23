import sys
import ply.lex as lex

tokens=['INT','ID','NUM','IF','OR','AND','BIGEQUAL','LESSEREQUAL','EQUALS','WHILE','DO','STDIN','STDOUT','COMMENT','NOTEQUALS','TRUE','FALSE','DEFINE','FUNC', 'CALL','ELSE']

literals=('=', '+','-','*','/','%', ';', '!', '>','<',')','(','{','}')

t_INT = r'INT'
t_IF = r'IF'
t_ELSE = r'ELSE'
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
