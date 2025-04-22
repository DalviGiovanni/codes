#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Caça ao Ouro no Mundo do Wumpus
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def le_mundo(Mundo,arquivo): 
    Mundo0=[]
    with open(arquivo,"r",encoding="utf-8")as arq:      #Suponho que os arquivos recebidos sejam strings. 
            for u in arq: 
                Mundo0.append(u)        #Construo uma lista com os elementos para manipulá-los, onde cada elemento é uma linha do arquivo de texto.
    Mundo1=[]        #Matrizes intermediárias para construção da matriz mundo.
    Mundo2=[]
    for h in Mundo0:
        Mundo1.append(h.strip())        #Retiro todos os strings antes das letras em cada elemento da lista.
    for v in Mundo1:
        Mundo2.append(v.split())        #Divido as letras juntas em novas matrizes elemento por elemento da antiga matriz.
    for p in Mundo2:
        i=0
        while i<len(p): 
            p[i]=int(p[i])          #Transformo os elementos da lista em inteiros
            i+=1
    i=0             #Reutilizar o contador
    j=0
    linha=[]            #Construirei a matriz mundo linha por linha
    d=Mundo2[0][0]
    while j<d:
        linha.append(0)         #Inicialmente a matriz será recheada de linha com apenas o elemento 0.
        j+=1
    while i<d:
        Mundo.append(linha[:])          #Essa atitude é necessária para que as linhas da matriz sejam listas independentes, caso contrário elas serão a mesma lista e modificar uma acarretará na modificação de todas.
        i+=1
    for elemento in Mundo2[1:]:         #Todos os entes dos elementos da matriz Mundo2 com excessão do elemento zero, responsável por indicar as dimensões da matriz, têm uma amarração entre si. A saber o primeiro e o segundo números da lista elemento indicam, respectivamente, a linha e a coluna de ocorrência do terceiro número na matriz mundo. Se não há ocorrência de alguma linha ou coluna basta manter o zero.
        z=elemento[0]
        x=elemento[1]
        y=elemento[2]
        Mundo[z][x]=y
def atualiza_percepcaoEagente(Percebe, Mundo, Acao, Agente, Estado,Jogo,Sentido): 
    if Acao=="D":           #Ação de girar 90º para a direita:
        if Agente[2]=="^":
            Agente[2]=">"
        elif Agente[2]==">":
            Agente[2]="v"
        elif Agente[2]=="v":
            Agente[2]="<"
        elif Agente[2]=="<":
            Agente[2]="^"
    if Acao=="E":           #Ação de girar 90º para a esquerda:
        if Agente[2]=="^":
            Agente[2]="<"
        elif Agente[2]==">":
            Agente[2]="^"
        elif Agente[2]=="v":
            Agente[2]=">"
        elif Agente[2]=="<":
            Agente[2]="v"
    if Acao=="M":           #Ação de movimento:
        if Agente[2]=="^":
            if Agente[0]!=0:            #A cada movimento o programa confere se não haverá a saída do personsagem do mundo, caso isso ocorra há a colisão, caso contrário o personagem é livre para executar a ação.
                Agente[0]=Agente[0] - 1
            else:
               Sentido[0]="C"           #colisão! A matriz Sentido guardará o que os sentidos do personagem captaram, como colisões ou a audição do personagem.
        elif Agente[2]==">":
            if Agente[1]!=(len(Mundo)-1):
                Agente[1]=Agente[1] + 1
            else:
                Sentido[0]="C"          #colisão!
        elif Agente[2]=="v":
            if Agente[0]!=(len(Mundo)-1):
                Agente[0]=Agente[0] + 1
            else:
                Sentido[0]="C"          #colisão!
        elif Agente[2]=="<":
            if Agente[1]!=0:
                Agente[1]=Agente[1] - 1
            else:
                Sentido[0]="C"          #colisão!
    if Acao=="T" and Estado[1]==1:          #Caso o jogador deseja atirar, esse necessita deter a flecha. Adicionei um tiro na parede para o jogador perceba que perdeu a flecha.
        Estado[1]=0             #Perde a flecha  
        if (not(Agente[2]=="^" and Agente[0]==0)) and (not(Agente[2]=="v" and Agente[0]==len(Mundo)-1)) and (not(Agente[2]=="<" and Agente[1]==0)) and (not(Agente[2]==">" and Agente[1]==len(Mundo)-1)): #Todos os casos que levarão a problemas de comparação, ou seja, aqui estão os casos que levariam o programa a efetuar uma comparação com um elemento da matriz que não existe.
            if Agente[2]=="^" and Mundo[Agente[0]-1][Agente[1]]==2:         #Atira para a casa de cima, se o Wumpus estiver na casa certa ele o matará, logo o estado do monstro passará para morto (0), o personagem ganhará 50 pontos e ouvirá um urro.
                 Estado[0]=0 
                 Estado[3]+=50
                 Sentido[1]="U"
            elif Agente[2]==">" and Mundo[Agente[0]][Agente[1]+1]==2:       #Atira para a casa da direita
                 Estado[0]=0
                 Estado[3]+=50
                 Sentido[1]="U"
            elif Agente[2]=="v" and Mundo[Agente[0]+1][Agente[1]]==2:       #Atira para a casa de baixo
                 Estado[0]=0
                 Estado[3]+=50
                 Sentido[1]="U"
            elif Agente[2]=="<" and Mundo[Agente[0]][Agente[1]-1]==2:        #Atira para a casa da esquerda
                 Estado[0]=0
                 Estado[3]+=50
                 Sentido[1]="U"
    if Acao=="G" and Mundo[Agente[0]][Agente[1]]==3 and Estado[2]==1:       #O personagem pega o ouro, para isso deve haver ouro a ser pego e ele deve estar na mesma sala do ouro.
        Estado[2]=0         #Não há mais ouro para ser pego
    if Acao=="S" and Agente[0]==len(Mundo)-1 and Agente[1]==0:          #Sair do jogo, para isso o personagem deve estar na casa inicial
        if Estado[2]==0:        #Se ele pegou o ouro:
            Estado[3]+=100
        else:       #Se ele não pegou o ouro:
            Estado[3]+=-10000
        Jogo[1]=0       #Marcador de passagem que indica que o jogo acabou mas o personagem ainda está vivo.
    if Mundo[Agente[0]][Agente[1]]==3:          #Pegar o ouro
        Percebe[Agente[0]][Agente[1]]="R"       #Caso o personagem esteja na mesma casa do ouro esse brilhará. Seu brilho permanece mesmo que seja pego, como explicitado nas orientações do EP
    if (Mundo[Agente[0]][Agente[1]]==1) or (Mundo[Agente[0]][Agente[1]]==2 and Estado[0]==1):       #Morte por Wumpus ou por burraco, a segunda condição exige que o protagonista adentre a casa do monstro com o mesmo vivo
        Jogo[0]=0       #Indicador de morte do personagem, que acarreta fim de jogo.
        Estado[3]=Estado[3]-10000       #Perda de pontos pela morte do personagem.
    if Agente[0]!=0:        #O programa certifica-se que não há a possibilidade de ocorrência de comparação com um elemento da lista com índice não existente, isso é, há garantia que não se sairá da lista.
        if (Mundo[Agente[0]-1][Agente[1]]==2):      #Caso o Wumpus esteja na linha acima do personagem isso acarretará que o personagem sentirá seu cheiro.
            Percebe[Agente[0]][Agente[1]]="1"       #Fedor! #A matriz Percebe recebe a informação do cheiro do monstro. A construção da informação Percebida ocorrerá através da contatenação das informações referentes ao cheiro do animal, a brisa do buraco e, finalmente o reflexo do ouro.
    if Agente[0]!=(len(Mundo)-1):       #Aqui utiliza-se (len(Mundo)-1), porque o número de elementos da lista é uma unidade maior que o número de posições da lista, ou seja, a lista começa do elemento 0.
        if (Mundo[Agente[0]+1][Agente[1]]==2):      #Caso o Wumpus esteja na linha abaixo do personagem isso acarretará que o personagem sentirá seu cheiro.
            Percebe[Agente[0]][Agente[1]]="1"       #Fedor!
    if Agente[1]!=0:
        if (Mundo[Agente[0]][Agente[1]-1]==2):      #Caso o Wumpus esteja na coluna à esquerda do personagem isso acarretará que o personagem sentirá seu cheiro.
            Percebe[Agente[0]][Agente[1]]="1"       #Fedor!
    if Agente[1]!=(len(Mundo)-1):
        if (Mundo[Agente[0]][Agente[1]+1]==2):       #Caso o Wumpus esteja na coluna à direita do personagem isso acarretará que o personagem sentirá seu cheiro.
            Percebe[Agente[0]][Agente[1]]="1"       #Fedor!
    if (Mundo[Agente[0]][Agente[1]]==2):        #A Casa do monstro também conserva seu cheiro. Só é acessável em caso de morte do mesmo.
            Percebe[Agente[0]][Agente[1]]="1"       #Fedor!
    if Percebe[Agente[0]][Agente[1]]!="1":
            Percebe[Agente[0]][Agente[1]]="0"       #Se após todas as direções forem checadas e, inclusive a própria sala, não se encontrar o monstro, isso é, não haver fedor, então não pode haver fedor nessa sala.
    if Agente[0]!=0 and (Percebe[Agente[0]][Agente[1]]!="01" and Percebe[Agente[0]][Agente[1]]!="11"):      #A primeira condição é análoga a do cheiro do monstro, ela evita comparação com elemento que não existem, já a segunda e terceira condições garante a não repetição da informação de brisa caso haja uma mesma casa adjacente a 2 buracos.
        if (Mundo[Agente[0]-1][Agente[1]]==1):
            Percebe[Agente[0]][Agente[1]]+="1"      #Brisa!
    if Agente[0]!=(len(Mundo)-1) and (Percebe[Agente[0]][Agente[1]]!="01" and Percebe[Agente[0]][Agente[1]]!="11"):         #Podem haver 2 buracos adjacentes, para evitar tal problema não se efetua a comparação no caso de encontro de um buraco adjacente.
        if (Mundo[Agente[0]+1][Agente[1]]==1):
            Percebe[Agente[0]][Agente[1]]+="1"      #Brisa!
    if Agente[1]!=0 and (Percebe[Agente[0]][Agente[1]]!="01" and Percebe[Agente[0]][Agente[1]]!="11"):
        if (Mundo[Agente[0]][Agente[1]-1]==1):
            Percebe[Agente[0]][Agente[1]]+="1"      #Brisa!
    if Agente[1]!=(len(Mundo)-1)and (Percebe[Agente[0]][Agente[1]]!="01" and Percebe[Agente[0]][Agente[1]]!="11"):
        if (Mundo[Agente[0]][Agente[1]+1]==1):
            Percebe[Agente[0]][Agente[1]]+="1"      #Brisa!
    if (Percebe[Agente[0]][Agente[1]]!="01") and (Percebe[Agente[0]][Agente[1]]!="11"):
            Percebe[Agente[0]][Agente[1]]+="0"      #Se após todas as direções forem checadas e não se encontrar um buraco, isso é, não haver brisa naquela casa, então a matriz Percebe recebe essa informação sobre essa casa.
    if Mundo[Agente[0]][Agente[1]]==3:      #Caso seja a sala do tesouro, então ele emitirá seu brilho através de um reflexo, como visto no exemplo fornecido, o brilho permanece mesmo que o ouro seja retirado.
        Percebe[Agente[0]][Agente[1]]+="1"      #Reflexo
    else:
        Percebe[Agente[0]][Agente[1]]+="0"      #Caso não seja a sala do tesouro devemos acrescentar essa informação à matriz Percebe.
def imprime_percepcao(Percebe,Agente,Mundo,Sentido): 
    i=0         #Os contadores farão a construção gráfica do mundo
    j=0
    h=0 
    p=""        #Divisão entre as linhas.
    c=""        #Construção da sala caso o explorador esteja nela.
    if Percebe[Agente[0]][Agente[1]]=="100":        #Construção do cenário caso o herói esteja na casa.
        c="F" 
    elif Percebe[Agente[0]][Agente[1]]=="110":
        c="FB"
    elif Percebe[Agente[0]][Agente[1]]=="101":
        c="FR"
    elif Percebe[Agente[0]][Agente[1]]=="111":
        c="FBR"
    elif Percebe[Agente[0]][Agente[1]]=="010":
        c="B"
    elif Percebe[Agente[0]][Agente[1]]=="011":
        c="BR"
    elif Percebe[Agente[0]][Agente[1]]=="001":
        c="R"
    elif Percebe[Agente[0]][Agente[1]]=="000":
        c=" "
    print("")       #Espaço em branco para não embolar as informações antigas e novas.
    print("Percepção após a última ação:")
    print("[",(Sentido[0]+Sentido[1]+c),"]")
    print("Mundo conhecido pelo agente:")
    while h<len(Mundo):         #Construção da divisão entre as linhas.
        p=p+"-------"       #Tamanho ideal para cada sala da linha.
        h+=1
    while i<len(Mundo):         #Esse while irá fazer a ligação entre a matriz Percebe e o jogador.
        a=""        #Esse elemento construirá cada uma das linhas da sala, ao terminar uma linha ele retorna ao elemento neutro dos strings
        j=0         #Garante que toda a linha seja reconstruida do 0
        while j< len(Percebe[i]):
            if (Agente[0]==i) and (Agente[1]==j):       #Coloca a orientação do explorador, ou seja, indica em que direção ele estã olhando. As condições listadas estão explicitadas nas orientações do EP.
                if len(c)==1:       #A partir do tamanho dos strings colocamos o número de espaços em branco para garantir uniformidade de tamanho entre as salas ao se adicionar a orientação do explorador.
                    a+="|  "+ Agente[2]+ c+ " |" 
                if len(c)==2:
                    a+="|"+ Agente[2]+ c+ "  |" 
                if len(c)==3:
                    a+="|"+ Agente[2]+ c+ " |"
            else:        #Casos em que o personagem não está na casa em questão, a cada número da matriz Percebe uma imagem distinta é mostrada ao jogador.
                if Percebe[i][j]=="-1":
                    a+="|  ?  |"
                elif Percebe[i][j]=="100":
                    a+="|  F  |"
                elif Percebe[i][j]=="110":
                    a+="|  FB |"
                elif Percebe[i][j]=="101":
                    a+="|  FR |"
                elif Percebe[i][j]=="111":
                    a+="| FBR |"
                elif Percebe[i][j]=="010":
                    a+="|  B  |"
                elif Percebe[i][j]=="011":
                    a+="|  BR |"
                elif Percebe[i][j]=="001":
                    a+="|  R  |"
                elif Percebe[i][j]=="000":
                    a+="|     |"
            j+=1
        i+=1
        print(p)        #Printa a divisão das linhas.

        print(a)        #Printa as linhas.
    print(p)        #Printa, finalmente a última divisão das linhas.
def imprime_mundo(Mundo,Estado):        #Função que ao final mostra todo o mundo para o jogador.
    i=0
    j=0
    p=""
    h=0
    print("")        #Espaço para não embolar informações.
    print("Mundo completo:")
    while h<len(Mundo):     #Construiremos o mundo do 0.
        p=p+"-------"
        h+=1
    while i < len(Mundo):
        a=""
        j=0
        while j<len(Mundo[i]):       #Para cada valor na matriz mundo corresponde a uma sala distinta.
            if Mundo[i][j]==0:
                a+="|     |"
            elif Mundo[i][j]==1:
                a+="|  P  |"
            elif Mundo[i][j]==2:
                a+="|  W  |"
            elif Mundo[i][j]==3:
                a+="|  O  |"
            j+=1
        i+=1
        print(p)
        print(a)
    print(p)
    print("Fim de jogo! Pontuação final:",Estado[3])        # Mostra a pontuação final do jogador.
def main():         #Função que realiza as novas ações do personagem.
    Mundo=[]        #A princípio a matriz Mundo é vazia
    print("Bem vindo(a) ao Mundo de Whumpus!")
    arquivo=input("Por favor o Digite o arquivo para ser lido referente ao mapa:")         #Aqui será digitado o arquivo que construirá o mundo.
    le_mundo(Mundo,arquivo)      #Modifica-se a matriz Mundo a partir do arquivo lido
    d=len(Mundo)         # Medida utilizada para economizar tempo, haja vista que saber o tamanho de linha/ colunas da matriz Mundo será importante.
    Acao=""      #Ação é iniciada vazia
    Agente=[d-1,0,"^"]      #Posição inicial e orientação do protagonista, note que são d-1 colunas, pois as listas se iniciam no lemento 0.
    Estado=[1,1,1,0]        #Matriz estado, como especificado nas orientações do EP.
    Percebe=[]      #Matriz que recebe as percepções do personagem com o ambiente, será construida a seguir.
    Sentido=["",""]      #Essa matriz foi criada para captar os sentidos mais imediatos do personagem, tato e audição, ou seja, respectivamente colisão e urro.
    Jogo=[1,1]      #Lista que indica, respectivamente se o personagem está vivo e se o jogo ainda não acabou, isso é, se o personagem não saiu do jogo. 
    i=0
    j=0
    linha2=[]
    while i<d:
        linha2.append("-1")     #Faço todas as linhas sem informações, a seguir irei ofertar as informações da sala inicial.
        i+=1
    while j<d:
        Percebe.append(linha2[:])       #Adiciono as linhas uma a uma, utilizei linha2[:] para que todas elas sejam independentes entre si.
        j+=1
    atualiza_percepcaoEagente(Percebe, Mundo, Acao, Agente, Estado,Jogo,Sentido)        #Chamo a função para que a casa que o agente inicia tenha as informações retiradas.
    imprime_percepcao(Percebe, Agente,Mundo,Sentido)        #Mostro na tela o mundo antes do jogador escolher a primeira ação.
    while Jogo[0]==1 and Jogo[1]==1:        #Enquanto o personagem não morre ou não sai do jogo.
        Sentido=["",""]      #Sentido[0] irá se referir ao choque com a parede e Sentido[1] ao Urro do monstro. Aqui a lista Sentido é permanentemente atualizada, ou seja, as sensações do personagem como choque e urro se limitam a uma rodada.
        Acao=input("Digite a ação desejada (M/T/D/E/G/S):")
        Estado[3]+=-1       #A cada ação o personagem perde um ponto
        atualiza_percepcaoEagente(Percebe, Mundo, Acao, Agente, Estado,Jogo,Sentido)         #A partir da ação atualiza-se a matriz Percebe.
        if Jogo[0]==1 and Jogo[1]==1:       #Se ele não morrer ou não sair do jogo é mostrado o novo mundo conhecido na tela.
            imprime_percepcao(Percebe, Agente,Mundo,Sentido)
    imprime_mundo(Mundo,Estado)         #Se ele morrer ou sair do jogo então o mundo inicial é mostrado na tela.    
if __name__ == "__main__":      
    print("Bem vindo(a) ao Mundo de Whumpus")
    print("Seguem as regras de movimento do jogo:")
    print('''
mover (“M”) para a sala imediatamente à sua frente (caso exista um muro o agente perceberá um choque e permanecerá na mesma localização);
girar 90º para a sua direita (“D”), i.e., giro no sentido horário;
girar 90º para a sua esquerda (“E”), i.e., giro no sentido anti-horário;
atirar (“T”) sua única flecha para frente (o Whumpus será morto e emitirá um urro caso a flecha
conseguir alcançar a sala em que o Whumpus vive);
pegar (grab) o ouro ("G") na sala em que ele estiver (caso o ouro não estiver na sala, nada
acontecerá); e
sair da caverna ("S"), somente se o agente estiver na sala inicial
          ''')
    print("Regras de Percepção:")
    print('''
● se ele estiver em uma sala adjacente (não na diagonal) a um Wumpus (“W”), sentirá um fedor (“F”);
● se ele estiver em uma sala adjacente (não na diagonal) a um poço (“P”), sentirá uma brisa (“B”);
● se ele estiver na mesma sala onde o ouro ("O") está, o agente perceberá o reflexo do seu brilho ("R");
● se ele tentar ir para além das bordas do ambiente, o agente percebe um choque com o muro ("C"); e
● se ele conseguir disparar uma flecha certeira (na mesma direção e sentido da localização do
Wumpus, que deve estar em uma sala adjacente), ouvirá um urro (“U”) agonizante.
          
          ''')
    
    print("Pontuação do Jogo:")

    print('''
          
O agente ganha 100 pontos por escalar a caverna para fora carregando o ouro; 50 pontos se matar o
Wumpus, -1 para cada ação que ele executar e -10000 pontos por ser morto pelo Wumpus, cair num poço ou
sair da caverna sem carregar o ouro
          ''')
    main()
