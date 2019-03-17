Sigma = ['x','y']
Q = ['q0','q1','q2','q3']
s = 'q0'
F = ['q3']

delta = { ('q0','x'):'q2',
        ('q0','y'):'q1',
        ('q1','x'):'q3',
        ('q1','y'):'q0',
        ('q2','x'):'q0',
        ('q2','y'):'q3',
        ('q3','x'):'q1',
        ('q3','y'):'q2'}

ejemplos = ['xy','xyxy', 'yx', 'xyxyxy','xyxyxyxy', 'xxxyyy', '']

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
