'''
Construirei uma classe (class ListaDuplamenteLigada) que define e manipula 
um objeto Lista Duplamente Ligada.
Os nós dos membros desta classe devem ser mantidos em ordem crescente do campo 
de informação.
'''

'''A seguir utilizei a classe ListaDuplamenteLigada '''

class ListaDuplamenteLigada:

    ''' operações sobre uma lista duplamente ligada. '''
    # classe _Node - interna
    
    class _Node:    
        __slots__ = '_info', '_prev', '_prox'

        def __init__ (self, info, prev, prox):
            
            # inicia os campos
            
            self._info = info
            self._prev = prev
            self._prox = prox

    # métodos de lista duplamente ligada
    
    def __init__ (self):
        
        ''' cria uma lista circular vazia.'''
        
        self._inicio = self._Node(None, None, None) # vazia
        self._final = self._Node(None, None, None) # vazia
        self._inicio._prox = self._final
        self._final._prev = self._inicio
        self._tamanho = 0 # tamanho da lista
    
    def __len__(self):
        
        ''' retorna o tamanho da pilha.'''
        
        return self._tamanho
    def is_empty(self):
        
        ''' retorna True se pilha vazia'''
        
        return self._tamanho == 0
    
    # A seguir a função __str__:
    
    def __str__(LA):
        
        # Inicialmente mostramos os termos que aparecem em toda chamada dessa 
        # função:
            
        print("Imprimindo a lista duplamente ligada:")
        print(f'{"Nó:":4}  {"Anterior:":14}  {"Informação:":14}  {"Posterior:":14} ')
        node=LA._inicio
        
        # Se o tamanho da lista é 0 é bem simples terminar, pois os dois 
        # elementos serão None e, como vimos em aula e o professor sugeriu,
        # antes da primeira e depois da 2º informação não há nada, para repre-
        # sentar tal fato uso "".
        
        if LA.is_empty():
            print(f'{"1":4}  {"":14}  {"None":14}  {"None":14} ')
            print(f'{"2":4}  {"None":14}  {"None":14}  {"":14} ')
            
        # Se o tamanho da fila não for 0 precisamos tomar cuidado com o primeiro
        # termo pois None e string não são comparáveis:
            
        else:    
            print(f'{"1":4}  {"":14}  {"None":14}  {node._prox._info:14} ')
            i=1
            
            # A seguir construimos as próximas linhas, corremos os elementos e 
            # para cada um deles analisamos a informação do anterior e do posterior
            # colocando-os, respectivamente, antes e depois da informação do 
            # elemento em questão. Tomamos cuidado com o caso None, pelo que foi 
            # explicado acima.
            
            while i <=len(LA):
                node=node._prox
                anterior =node._prev._info
                sucessor = node._prox._info
                if node._prev._info ==None: anterior = "None"
                if node._prox._info ==None: sucessor = "None"
                j=str(i+1)
                print(f'{j:4}  {anterior:14}  {node._info:14}  {sucessor:14}')
                i+=1
            j=str(i+1)
            
        # Por fim construímos o termo final da lista e encerramos a função com o
        # return para haver um espaço entre as saídas a fim de obtermos maior
        # nitidez:
            
        print(f'{j:4}  {node._info:14}  {"None":14}  {"":14} ')
        return ""
    
    # Como trata-se da função __str__ o termo acima será impresso como string
    # como de fato deveria ocorrer.

    # A seguir a função Adiciona:
        
    def Adiciona(LA, x):
        i=0
        antecessor=LA._inicio
        
        # Se a lista é tal que len(LA)==0, então devemos fazer o apontador do 
        # primeiro termo da lista indicar o elemento que será adicionado, para 
        # isso criamos um nó do mesmo, cujo apontador anterior apontará para o 
        # início da lista e o apontador final para o final da mesma. Além disso,
        # o apontador anterior do último termo da lista deve apontar para o 
        # elemento adicionado:
        
        if len(LA)==0:
            sucessor=antecessor._prox
            novo = LA._Node(x, antecessor, sucessor)
            antecessor._prox = novo
            sucessor._prev = novo
            
        # Se a lista tem elementos precisamos tomar cuidado com o caso None, 
        # pois o Python não admite comparar um string com None, dessa forma,
        # analisamos os termos até que encontremos um None, ou até que o elemento
        # a ser adicionado seja maior que os termos percorridos na lista. Quando
        # uma dessas condições é satisfeita sabemos que devemos adicionar o 
        # elemento, fazemos isso criando um nó cuja informação seja o que desejamos
        # adicionar e fazemos o apontamento anterior dele apontar para o último elemento
        # da lista menor que ele e o apontador posterior para o mesmo elemento
        # que o apontador posterior do elemento anterior apontava e fazemos esse
        # apontar para o nó que adicionamos. Se o termo seguinte for None, devemos
        # acrescentar a informação logo antes do mesmo seguindo o roteiro explicado acima.
 
        else:
            while i < len(LA)+1 and antecessor._prox._info != None and antecessor._prox._info  < x:
                antecessor=antecessor._prox
                i+=1
            sucessor=antecessor._prox
            novo = LA._Node(x, antecessor, sucessor)
            antecessor._prox = novo
            sucessor._prev = novo
        
        # Por fim incrementamos o tamanho da lista e a mostramos:
            
        LA._tamanho+=1    
    
    # A seguir a função Remove, seu funcionamento consiste em percorrer todos 
    # os elementos da lista a partir do primeiro até encontrar o elemento 
    # desejado, se isso ocorrer somamos 1 num contador que começa em 0, e elimi-
    # mos o termo em questão, fazendo o apontador posterior do elemento anterior
    # ao que desejamos retirar apontar para onde o apontador posterior do elemento em questão
    # apontava e fazemos o apontador anterior do elemento posterior ao elemento que será 
    # retirado apontar para o mesmo elemento que o apontador anterior do elemento 
    # a ser retirado apontava.
    
    def Remove(LA, x):
        n=0
        if len(LA)==0: return 0
        node=LA._inicio._prox
        for i in range(len(LA)):
            if x==node._info:
                anterior=node._prev
                sucessor=node._prox
                anterior._prox=sucessor
                sucessor._prev=anterior
                n+=1
                LA._tamanho-=1
            node=node._prox
        return n
    
    # A função a seguir é a função Conta, ela corre todos os elementos da lista
    # duplamente ligada, começando do início, quando encontra o elemento procu-
    # rado soma 1 em um contador e retorna tal contador:
    
    def Conta(LA, x):
        n=0
        y=LA._inicio
        for i in range(len(LA)+1):
            if x== y._info:
                n+=1
            y=y._prox
        return n
            
            
            
# Meus testes:            
if __name__ == "__main__":
    
# Programa teste exemplo da classe ListaDuplamenteLigada

    lx = ListaDuplamenteLigada() 
    while True:
        f = input("Entre com a informação:")
        if f == 'fim': break
        lx.Adiciona(f)
        print(lx)
   
    while True:
        f = input("Entre com a informação a remover:")
        if f == 'fim': break
        print("removidos", lx.Remove(f), "elementos")
        print(lx)

        #print(lx)

    # teste conta
    
    while True:
        f = input("Entre com a informação a contar:")
        if f == 'fim': break
        print("contados", lx.Conta(f), "elementos")
        print(lx)
