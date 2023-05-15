from typing import TextIO, Tuple

codewithnumbers:TextIO = open ('codewithnumbers.txt')
codewithoutnumbers:TextIO = open ('codewithoutnumbers.txt','w')
numeros:Tuple[str] = ('1','2','3','4','5','6','7','8','9','0')

def pasar_code_sin_numeros(d:TextIO) -> TextIO:
    newm:str = ''
    for i, m in enumerate(codewithnumbers):
        list(m)
        if m[0] in numeros:
            newm = m[hasta_donde(m)+1:len(m)]
            codewithoutnumbers.write(newm)
        else:
            codewithoutnumbers.write(m)
    return newm
def hasta_donde(b:TextIO) -> int:
    posiciones:int = 0
    b = list(b)
    for i,m in enumerate(b):
        if m in numeros:
            posiciones = i
        else:
            break
    return posiciones
            

