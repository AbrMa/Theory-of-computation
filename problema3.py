Sigma = ['0','1','2']
Q = ['q0','q1','q2']
s = 'q0'
F = ['q0','q1']

delta = { ('q0','0'):'q0',
          ('q0','2'):'q0',
          ('q0','1'):'q1',
          ('q1','0'):'q0',
          ('q1','1'):'q1',
          ('q1','2'):'q2',
          ('q2','0'):'q2',
          ('q2','1'):'q2',
          ('q2','2'):'q2'}

ejemplos = ['', '12', '21', '111111112', 
            '2222222222221', '012', '102', 
            '21002120', '02000211', '12002200', 
            '21021202', '12210011' '212']

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