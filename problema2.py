Sigma = ['a','b']
Q = ['q0','q1']
s = 'q0'
F = ['q0']

delta = { ('q0','a'):'q1',
        ('q0','b'):'q0',
        ('q1','a'):'q0',
        ('q1','b'):'q1' }

ejemplos = ['aaa','abab']

def cambio_estado(q,s):
    global delta
    return delta[(q,s)]

for w in ejemplos:
    estado = s
    for c in w:
        estado = cambio_estado(estado,c)

    if estado in F:
        print(w + " si está en el lenguaje")
    else:
        print(w + " no está en el lenguaje")
