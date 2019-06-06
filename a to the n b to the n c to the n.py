def isInL(w):
    a = 0; b = 0; c = 0; auxA = 0; auxB = 0;
    for ch in w:
        if ch == 'a':
            a += 1
        elif ch == 'b':
            b += 1
        elif ch == 'c':
            c += 1
    for i in range(0,a):
        if w[i] == 'a':
            auxA += 1
    for i in range(a,a+b):
        if w[i] == 'b':
            auxB += 1
    if a == b and b == c and auxA == a and auxB == b:
        print(w + " Está en el lenguaje")
    else:
        print(w + " no está en el lenguaje")

w = ""
isInL(w)
