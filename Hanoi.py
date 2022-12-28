'''
Esse programa resolve o famoso problema da Torre de Hanói, mostrando o passo-a-passo
da solução desse clássico desafio.

'''
'''
A ideia do programa é utilizar 3 listas O,D,A para representar, respectivamente,
a haste original, a destino e a auxiliar. Pode-se questionar por que não utilizei
pilhas ou filas. Tomei tal medida pois para apresentar o resultado seria necessário
percorrer todos os elementos da pilha ou lista em questão, algo pouco comum nesse
tipo de dado.
'''

'''
A função a seguir criará as listas em questão, ela é chamada na primeira vez
que a função Hanoi atua, ou seja, quando n==nmax.
'''

def Inicio(n,a,b,c):
    O=[]
    D=[]
    A=[]
# Cada disco será numerado de cima para baixo de acordo com a ordem na haste original 
    for i in range(n):
        O.append(i+1)
        D.append(" ")
        A.append(" ")
    
    print("\n* * * Movimentar",n,"discos * * *")
    print("\n* * * Situação Inicial: * * *")
    for i in range(n):
        print(O[i])
    print(a," ",b," ",c)
    return O,D,A

'''
Infelizmente tive que adicionar mais entradas para a função Hanoi, assim como
para a função Movimente, na primeira fixei o número máximo de discos, para saber
quando a função Inicio deveria atuar, além disso, foi necessário carregar as 
listas representando as hastes. Para que o programa funcionasse corretamente, a
primeira chamada da função Hanoi toma as listas em questão como vazio, mas 
nessa mesma já ocorrerá a alteração das mesmas. Já para a função Movimente
apenas carregamos as listas representando as hastes.
'''

def Hanoi(nmax,n, torreA, torreB, torreAux,O=[],D=[],A=[]): 
    if n==nmax:
        O,D,A=Inicio(nmax,torreA,torreB,torreAux)
    if n == 1:
 # mover disco 1 da torreA para a torreB
        Movimente(1, torreA, torreB,O,D,A)        
    else:
 # n - 1 discos da torreA para torreAux com torreB auxiliar
        Hanoi(nmax,n - 1, torreA, torreAux, torreB,O,D,A)
 # mover disco n da torreA para torreB
        Movimente(n, torreA, torreB,O,D,A)       
 # n - 1 discos da torreAux para a torreB com torreA auxiliar
        Hanoi(nmax,n - 1, torreAux, torreB, torreA,O,D,A)
        
'''
A função Movimente foi a que sofreu maior alteração. Sinteticamente analisei 
todos os casos possíveis de movimentos de um disco, são 3!=6 casos, a partir 
dos mesmos as listas representando cada haste foram alteradas, de forma que os 
discos ocupassem as posições mais próximas do início da torre.
'''

def Movimente(k, origem, destino,O,D,A):
    print("mover disco ", k, " da torre ", origem, " para a torre ", destino)
    if origem =="A" and destino =="B":
# Altero o elemento retirado por " ", para que a lista tenha um tamanho fixo e
# para que o print fique alinhado.
# A seguir retiro o elemento mais acima, para isso percorro os termos, evitando
# os elementos da lista que são " ":
        for i in range(len(O)):
            if O[i]!=" ":         
                O[i]=" "
                break
# A seguir percorro os termos da lista do último ao primeiro até encontrar uma
# posição livre para que o disco seja colocado e que seja mais próxima da base
# da haste em questão.
        for i in range(len(D)-1,-1,-1):
            if D[i]==" ":
                D[i]=k
                break
# A rotina acima é imposta a todos tipos de movimentos permitidos:
    elif origem =="A" and destino =="C":
        for i in range(len(O)):
            if O[i]!=" ":         
                O[i]=" "
                break
        for i in range(len(A)-1,-1,-1):
            if A[i]==" ":
                A[i]=k
                break
    elif origem =="B" and destino =="A":
        for i in range(len(D)):
            if D[i]!=" ":         
                D[i]=" "
                break
        for i in range(len(O)-1,-1,-1):
            if O[i]==" ":
                O[i]=k
                break
    elif origem =="B" and destino =="C":
        for i in range(len(D)):
            if D[i]!=" ":         
                D[i]=" "
                break
        for i in range(len(A)-1,-1,-1):
            if A[i]==" ":
                A[i]=k
                break
    elif origem =="C" and destino =="A":
        for i in range(len(A)):
            if A[i]!=" ":         
                A[i]=" "
                break
        for i in range(len(O)-1,-1,-1):
            if O[i]==" ":
                O[i]=k
                break
    elif origem =="C" and destino =="B":
        for i in range(len(A)):
            if A[i]!=" ":         
                A[i]=" "
                break
        for i in range(len(D)-1,-1,-1):
            if D[i]==" ":
                D[i]=k
                break
# Depois de analisados todos os casos possíveis e termos alterado as listas re-
# presentando as hastes mostramos como as mesmas estão:
    for i in range(len(O)):
        print(O[i]," ",D[i]," ",A[i])
    print("A"," ","B"," ","C")    
# Espera-se que o usuário determine o número de discos:
while True:
    n=input("Digite o número de discos:")
    # Se o usuário digitar "fim" o programa para.
    if n=="fim":
        break
    Hanoi(int(n),int(n), "A","B","C")

