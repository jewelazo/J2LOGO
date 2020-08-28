from itertools import product
def cuenta_subcadenas_ax(cadena):
    A=[]
    X=[]
    a=0
    b=0
    for i in cadena:
    	if i=='A':
    		A.append(a)
    	elif i=='X':
    		X.append(a)
    	a+=1
    for i,j in product(A,X):
    	if j>i:
    		b+=1
    print(b)

cuenta_subcadenas_ax('AXAXAXAXAX')
cuenta_subcadenas_ax('CAXAAYXZA')