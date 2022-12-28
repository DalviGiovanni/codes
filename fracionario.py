'''
Esse programa realiza operações entre frações mantendo a notação fracionária, para isso utilizei a notação pós-fixa.
Todas operações usuais são permitidas
Para encerrar o programa basta digitar 'fim' sem aspas.
'''

import re

'''A função mdc será usada apenas quando acionado o comando print, assim
evitamos repetições da mesma.'''

def mdc(n, m):
    resto = n % m
    while resto != 0:
        n = m
        m = resto   
        resto = n % m
    return m

class Fração:

    '''Define a classe Fração Ordinária exatamente como na 1º atividade.''' 
    
    # Construtor da classe:
        
    def __init__(self, topo = 0, base = 1):
        
        #Primeiro iremos assegurar que o denominador não é 0.
        
        if base == 0: 
            raise ValueError("Denominador igual a zero")
        #Caso não seja prosseguimos.
        self.num = topo
        self.den = base
        
    # A soma será:
        
    def __add__(a1, a2):
        xnum = a1.num * a2.den + a1.den * a2.num
        xden = a1.den * a2.den
        return Fração(xnum , xden)
    
    # A subtração será:
        
    def __sub__(a1,a2):
        xnum = a1.num * a2.den - a1.den * a2.num
        xden = a1.den * a2.den
        return Fração(xnum , xden)

    # A multiplicação será:
        
    def __mul__(a1,a2):
        xnum = a1.num * a2.num
        xden = a1.den * a2.den
        return Fração(xnum , xden)
    
    '''A divisão será: multiplicamos o numerador do 1º pelo deno-
    minador do 2º e esse será o novo numerador e multiplicamos o numerador
    do 2º com o denominador do 1º e esse será o novo denominador.'''
    
    def __truediv__(a1,a2):
        xnum = a1.num * a2.den
        xden = a1.den * a2.num
        return Fração(xnum , xden)
    
    # A potenciação será:

    def __pow__(a1,n):
        
        # Tomamos cuidado com o caso de n<0, para isso usamos o if a seguir, a
        # fim de, nesse caso, inverter numerador e denominador e usar -n>0.
        # Aqui operamos com expoente inteiro. 
        
        if n >=0:
            xnum = (a1.num)**n
            xden = (a1.den)**n
        else:
            xnum = (a1.den)**(-n)
            xden = (a1.num)**(-n)
        return Fração(xnum , xden)
            
    # Transforma em string para o print:
        
    def __str__(self):
        
        '''Nesse ponto, para apresentar a fração irredutível ao usuário, 
        usamos a função mdc, evitando repetições do programa'''
        
        xmdc = mdc(self.num, self.den)
        self.num = self.num // xmdc
        self.den = self.den // xmdc
        if self.den !=1:
            return str(self.num) + "/" + str(self.den)
        else:
            return str(self.num) 

    # Compara dois elementos da classe quanto à igualdade:
    def __eq__(a1, a2):
        pri_fator = a1.num * a2.den
        seg_fator = a1.den * a2.num
        return pri_fator == seg_fator
    
    # Compara dois elementos da classe quando à desigualdade:
    def __ne__(a1,a2):
        pri_fator = a1.num * a2.den
        seg_fator = a1.den * a2.num
        return pri_fator != seg_fator
    
    # Analisa se o primeiro é menor que o segundo:
    def __lt__(a1,a2):
        pri_fator = a1.num * a2.den
        seg_fator = a1.den * a2.num
        return pri_fator < seg_fator
    
    # Analisa se o primeiro é menor ou igual ao segundo:
    def __le__(a1,a2):
        pri_fator = a1.num * a2.den
        seg_fator = a1.den * a2.num
        return pri_fator <= seg_fator
    
    # Analisa se o primeiro é maior que o segundo:
    def __gt__(a1,a2):
        pri_fator = a1.num * a2.den
        seg_fator = a1.den * a2.num
        return pri_fator > seg_fator
    
    # Analisa se o primeiro é maior ou igual ao segundo:
    def __ge__(a1,a2):
        pri_fator = a1.num * a2.den
        seg_fator = a1.den * a2.num
        return pri_fator >= seg_fator
    
''' A seguir construímos a classe pilha, baseado no material fornecido em aula:'''

class Pilha:
    
    # Construtor da classe Pilha:
    
    def __init__(self):
        self._pilha = [] # lista que conterá a pilha
        
 # Retorna o tamanho da pilha
 
    def __len__ (self):
        return len(self._pilha)
 
 # Retorna True se pilha vazia:
     
    def is_empty(self):
        return len(self._pilha) == 0
 
 # Empilha novo elemento "e":
     
    def push(self, e):
        self._pilha.append(e)
        
 # Para a função a seguir, note que a pilha não pode estar vazia se a 
 # expressão estiver adequadamente digitada, em todo caso não foi requisitado 
 # nenhum indicativo nas orientações do EP para um marcador para pilha vazia e,
 # caso haja algum problema aceitável no programa, como divisão por 0, a função 
 # CalcPosFixa indicará "None":
     
 # Retorna o elemento do topo da pilha sem retirá-lo
     
    def top(self):
        if self.is_empty( ): return print("")
        return self._pilha[-1]
    
 # Desempilha elemento, aqui mantivemos um indicativo de erro que, caso a 
 # expressão esteja bem escrita, como suposto, não deve ocorrer: 
     
    def pop(self):
        
        if self.is_empty( ):
            print("Erro")
        return self._pilha.pop( )
    
'''A seguir definimos a função que indica a prioridade dos operadores ou se o
elemento analisado é operando através de um número inteiro. Com o aumento do 
valor temos aumento de prioridade dos operadores, com exceção do abre e fecha 
parênteses que não são operadores mas também estão relacionados a números e os
operandos que são levados em 0'''

def Prioridade(x):
    if x == "+": return 1
    elif x == "-": return 1
    elif x == '*': return 2
    elif x == '/': return 2
    elif x == '**': return 3
    elif x == '(': return 4 # caso particular
    elif x == ')': return 5 # caso particular
    else: return 0 # não é operador

'''A seguir construiremos a função requisitada TraduzPosFixa, usando a dica do 
professor.'''

def TraduzPosFixa(exp):
    r = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", exp)
    
    '''A seguir tratamos o caso "**", para isso ao aparecer um "*" analisaremos
    o próximo termo e se esse for novamente o mesmo termo, então excluiremos um
    deles e substituiremos o outro por "**", o que seria equivalente a juntá-los '''
    
    # O range vai até len(r)-1 porque para nós só é necessário analisar o primeiro
    # dos dois "*" para precisar avaliar se há um "**".
    
    for j in range(len(r)-1):
        if r[j]== '*' and r[j+1] =='*':
            r.pop(j+1)
            r[j] ='**'
    pos=[]
    
    # A seguir a pilha de operandos requisitada
    
    Operadores=Pilha()
    
    '''O código a seguir trabalha para traduzir a expressão para notação pós-fixa 
    a partir das regras vistas em classe, no caso de os operadores terem mesma 
    prioridade optamos por colocar aquele na pilha de operadores na expressão 
    pós-fixa e o outro tomar seu lugar na pilha (como vimos em sala há duas
    opções nesse caso, mas essa é mais prática).
    '''
    
    for i in range(len(r)):
        
# No caso de operandos esses devem ir direto para a expressão pós-fixa

        if Prioridade(r[i]) ==0:
            pos.append(r[i])
            
# Caso não haja operadores na pilha dos mesmo então devemos empilhar o
# operador que aparecer:
    
        elif len(Operadores)==0: 
            Operadores.push(r[i])
            
# O código a seguir analisa se a prioridade do próximo operador é maior que a 
# do que está no topo da pilha de operadores e se for o caso empilha. Respeitando
# o caso de haver, eventalmente um "(" na pilha de operadores.

        elif 4 > Prioridade(r[i]) > Prioridade(Operadores.top()) and Prioridade(Operadores.top())!= 4:
            Operadores.push(r[i])
            
# O código a seguir atua se a prioridade do próximo operador da expressão pós-
# fixa for menor que a do operador no topo da pilha, então o operador no topo da
# pilha vai para a expressão pós-fixa e o outro é empilhado na pilha de operadores.

        elif Prioridade(r[i]) <= Prioridade(Operadores.top()) < 4:
            pos.append(Operadores.top())
            Operadores.pop()
            Operadores.push(r[i])
            
# Aqui tratamos do caso de haver um parênteses, vamos levar "(" para a 
# pilha de operadores, ele atuará como um marcador, como ficará claro a seguir.
# Se temos um parênteses devemos empilhar no topo da pilha "(" e o operador logo a 
# seguir nessa ordem. Algo diferente deve ocorrer se aparecer o termo ")". 
# Nesse caso explicaremos a seguir, numa próxima função.
# Mas note que nunca teremos "(" seguido por ")" sem um operador no meio, caso 
# a expressão esteja adequadamente escrita.

        elif Prioridade(Operadores.top()) == 4:
            Operadores.push(r[i]) 
            
#A seguir empilhamos "(" se ele aparecer na expressão:
    
        elif Prioridade(r[i]) ==4:
            Operadores.push(r[i])
            
# Finalmente se ocorrer um ")" então devemos desempilhar a lista colocando seus 
# elementos na expressão pós-fixa respeitando as operações de pilha até a pilha 
# de operadores apresentar um "(", quando isso ocorrer devemos excluí-lo e parar
# o processo de retirar elementos da pilha e colocá-los na expressão pós-fixa.

        elif Prioridade(r[i])==5:
            while Prioridade(Operadores.top())!=4:
                pos.append(Operadores.top())
                Operadores.pop()
                
# Após o processo descrito acima de colocar os operadores dentro dos  
# parênteses na expressão pós-fixa da maneira explicada, devemos prosseguir com 
# a retirada do operador "(" que se encontrará no topo da lista:
    
            Operadores.pop()
            
# Finalmente depois de percorrer toda a expressão devemos descarregar todos os
# operadores que sobraram da pilha de operadores na expressão pós-fixa, do últi-
# mo para o primeiro, o que é facilitado pelas operações de Pilha:
    
    while Operadores.is_empty()!=True:
        pos.append(Operadores.top())
        Operadores.pop()
    return pos

# Como acima fica claro a saída do programa será a lista "pos".

'''Os problemas que CalcPosFixa podem ter estão relacionados 
 a operadores unários ou divisões por 0, com termos que não são inteiros que
 são colocados para se operar, como strigns, ou elevação à frações, por exemplo.
 Como a orientação do programa supõe que o usuário digitou a expressão correta-
 mente, então a única excessão relevante, nesse caso, seria a divisão por 0.
 E essa será devidamente tratada, quando a mesma ocorrer a função retornará
 "None".
 '''
 
def CalcPosFixa(listaexp):
    
# Usaremos essa pilha para guardar os operandos:
    
    Operandos=Pilha()
    
    # Se for um operando deve ir para a pilha acima:
        
    for i in range(len(listaexp)):
        if Prioridade(listaexp[i]) == 0:
            
        # Como sugestão do professor, transformo todos os elementos em fração
        # e após opero com eles. Mas para isso devo primeiro transformar
        # os strings em inteiros e a seguir em frações:
                
            Operandos.push(Fração(int(listaexp[i])))
            
    # Se não for devemos operar os dois últimos termos da pilha de Operandos
    # na ordem que aparecem na mesma:
        
        else:
            x2=Operandos.top()
            Operandos.pop()
            x1=Operandos.top()
            Operandos.pop()
            try:
                if listaexp[i]=="**":
                    
# Como a orientação do programa supõe que o expoente será sempre inteiro, em 
# particular, toda sua informação relevante estará em seu numerador, pois o 
# denominador será 1, desse modo a operação de elevação se reduzirá a:
    
                    Operandos.push(x1 ** x2.num)
                    
# Faço isso pois na classe Fração as operações "**" são de frações com inteiros 
# (o primeiro a base e o segundo o expoente da operação),
# o numerador de x2 é um inteiro e é o elemento que x1 deve ser elevado.

# As outras operações são bem simples, uma vez que definimos cada operadorando
# como uma fração:
    
                elif listaexp[i]=="+":
                    Operandos.push(x1 + x2)
                elif listaexp[i]=="-":
                    Operandos.push(x1 - x2)
                elif listaexp[i]=="*":
                    Operandos.push(x1 * x2)
                elif listaexp[i]=="/":
                    Operandos.push(x1 / x2)
                    
# Enquanto houver operando realizo as operações, quando esses acabam eu paro a 
# repetição e retorno o elemento, único, da pilha dos operandos:

            except:
                break
    return Operandos.top()
x=0

# A seguir a rotina repetida que o programa deve manter até se digitar "fim":
    
while True:
    x=input(">>> ")
    if x == "fim":
        break
    y=CalcPosFixa(TraduzPosFixa(x))
    print(y)
    
# Caso o usuário digite "fim" o break garante o término da execução do programa.