import ply.lex as lex
import ply.yacc as yacc

tokens = ('a', 'b')

t_a = r'a'
t_b = r'b'

def t_error(t):
    print("Símbolo ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

def p_S(p):
    ''' S : S a
          | S b
          | empty '''
    pass

def p_empty(p):
    ''' empty : '''
    pass

def p_error(p):
    global s
    if p:
        print("Error de sintaxis en '%s'" % p.value)
        print(s," no está en el lenguaje")
    else:
        print("Error de sintaxis en EOF")
        print(s," no está en el lenguaje")
yacc.yacc()

while 1:
    try:
        s = input('> ')
    except EOFError:
        break
    if not s: continue
    t = yacc.parse(s)


