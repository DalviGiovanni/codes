import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.integrate import odeint

'''
Esse módulo simula equações diferenciais do comportamento de algumas partículas no
 universo primordial, de acordo com o desenvolvimento termodinâmico proposto por
Escudero. nesse caso usamos apenas 1 temperatura para todas as espécimes de 
neutrinos.
'''

'''
DIÁRIO DE PROGRAMAÇÃO - 08/09
Hoje tratei a pressão e densidade de energia dos prótons como análoga a dos elétrons
com isso espero não precisar resolver a EDO para a densidade de energia total
Afinal, ao saber a energia, em tese, saberei as densidades de energia e, portanto,
consigo retirar suas derivadas e o valor de H.

O programa fornece um gráfico, mas ele está incorreto

09/09

Retirei a equação da densidade de energia e obtive um gráfico sem pontos.
Talvez devesse printar alguns dos dados.
Aumentar os limites de integração deve ser cogitado!

10/09

O programa roda, mas fornece muitas mensagens de que o erro está subsestimado.

Não há evolução das variáveis. Ou seja, as 2 componentes do array solução são constantes

Coloquei GF, a constante de Fermi em unidades de GeV^-2

Corrigi mpl na expressão da taxa de Hubble

11/09

A partir de alguns testes pude concluir que o problema do programa é a condição inicial

***  Ideias  ***

1. Mudar a forma de integração
2. Colocar o eixo x com ln

Problema: estagnação dos valores. Por que?

Porque as derivadas tem valores muito pequenos (e-14)

16/09

Coloquei tudo em Mev e ajustei o tempo.

23/09

Tirei os prótons, eles não existiam à época.

'''

''' Definindo variáveis: '''

'''
Tv = temperatura dos neutrinos
Te = temperatura dos elétrons
Tg = temperatura do fótons (Te = Tg para nós)

As densidades a seguir se referem a energia:

pv = densidade de energia dos neutrinos
pg = densidade de energia dos fótons
pe = densidade de energia dos elétrons
pp = densidade dos prótons (Não serão utilizadas)
pT = densidade total
pT= pv + pg + pe 

Precisamos tirar a densidade de energia de prótons a partir das outras densidades.

Pressão:
Pe = pressão dos elétrons
Pg = pressão dos fótons
PT = Pe + Pg

Estamos supondo que neutrinos interagem tão fracamente que não exercem pressão
a pressão dos prótons não parece muito relevante, mas precisamos ver, um argumento pode ser 
que ele não são partículas relativísticas.

Não usaremos prótons porque os mesmos não existiam na época que analisamos.

Preciso analisar se todas variáveis estão em Mev, em especial a massa das partículas!

h estava errado no expoente do numerador


'''


'''
Vamos definir algumas funções úteis
'''

def pv(T):
    return 2 * 7 * np.pi**2 * T**4/(8 * 30)

def dpv_dT(T):
    return 4 * pv(T)/T

def pg(T):
    return 2 * np.pi**2 * T**4/30
    
def dpg_dT(T):
    return 4 * pg(T)/T

def pe(T):
    me = 0.511 #MeV
    res , err = integrate.quad(g,me,np.inf,args = (T,me))
    return (2/ (np.pi**2))* res

def g(E,T,m):
    return E**2 * np.sqrt(E**2-m**2)/(np.exp(E/T)+1)

def h(E,T,m):
    return np.sqrt(E**2-m**2)**3/(np.exp(E/T)+1)

'''
def pp(Tg):
    mp = 938.27
    res , err = integrate.quad(g,mp,np.inf,args = (Tg,mp))
    return (2/ (np.pi**2)) *  res
'''
'''
def Pp(T):
    mp = 938.27
    res, err = integrate.quad(h,mp,np.inf, args = (T,mp))
    return (2/3 * np.pi**2)* res
'''

def Pe(T):
    me= 0.511
    res , err = integrate.quad(h,me,np.inf, args = (T,me))
    return (2/(3 * np.pi**2))* res

def Pg(T):
    return pg(T)/3

def PT(Tg):
    return Pg(Tg)+ Pe(Tg) 

def dpe_dT(T):
    # function we want to integrate
    def f(E,T):
        me = 0.511
        return ((1 / ( 2 * np.pi**2))* E**3 * np.sqrt(E**2-me**2) / ( T**2 * (np.cosh(E/(2*T)))**2))
    me= 0.511
    # call quad to integrate f from 0.511 to 10000, warning about the upper integrant limit
    
    res, err = integrate.quad(f, me, np.inf, args = (T))

    return res

def FMB(T1,T2):
    return 32*(T1**9-T2**9) + 56* T1**4 * T2**4 *(T1-T2)

def dpve_dt(Tg,Tve,Tvmu):
    return (GF**2 / np.pi**5)*((1+4*sw2+8*sw2**2)*FMB(Tg,Tve)+2*FMB(Tvmu,Tve))

def dpvmu_dt(Tg,Tve,Tvmu):
    return (GF**2 / np.pi**5)*((1-4*sw2+8*sw2**2)*FMB(Tg,Tvmu)-FMB(Tvmu,Tve))

def H(pe,pv,pg):
    p= pe + 3*pv + pg
    m= 1.22 * 10**22
    H = np.sqrt((8 * np.pi/3)* p/m**2 )
    return H

def pT(Tg,Tv):
    return pe(Tg)+ pg(Tg)+ 3*pv(Tv)

    

'''
A seguir defino o lado direito das EDOs:
'''

def func1(y,t):
    Tv, Tg = y
    return - H(pe(Tg),pv(Tv),pg(Tg))*Tv + (dpve_dt(Tg, Tv, Tv) +  2* dpvmu_dt(Tg, Tv, Tv))/(3* dpv_dT(Tv))

def func2(y,t):
    Tv, Tg = y
    h = H(pe(Tg),pv(Tv),pg(Tg))
    return -(4 *h* pg(Tg)+3 * h * (pe(Tg)+ Pe(Tg)) + dpve_dt(Tg, Tv, Tv) + 2 * dpvmu_dt(Tg, Tv, Tv) ) / (dpg_dT(Tg) + dpe_dT(Tg))

def Func(y,t):
    Tv , Tg = y
    dy_dt = np.array([func1(y,t),func2(y,t)])
    return dy_dt

'''
A seguir defino a função main(), ela que resolverá a EDO
y0 serão as condições iniciais
'''

def main():
    global GF, sw2
    GF = 1.1664e-11
    sw2=0.223 
    #A condição inicial, presente a seguir, é dada apenas pela temperatura da massa primordial
    #T= 8.6217e21
    T=15
    y0 = np.array([T,T])
    t = np.linspace(1, 1e25, 10000001)
    sol = odeint(Func,y0,t)
    plt.plot(sol[:,1], sol[:, 1]/ sol[:, 0], 'b', label='T\u03B3/T\u03BD')
    plt.legend(loc='best')
    plt.xlabel('T\u03B3 [Mev]')
    #plt.grid()
    #x = np.array([10, 5, 3, 2, 1,0.6,0.1,0.03])
    #x = [0.03,5,3,2,1,0.6,0.1,0.03]
    #default_x_ticks = range(len(x))
    #plt.xticks(default_x_ticks, x)
    plt.xscale('log')
    #plt.scale.LogScale('xaxis', subs = x )
    plt.xlim([0.03, 10])
    plt.gca().invert_xaxis()
    plt.title('Temperatura de Desacoplamento de Neutrinos')
    plt.show()
    print('$N_{eff}$ = ',  (8/7) *(11/4)**(4/3) * ((3*pv(sol[:,0][-1])+pe(sol[:,1][-1]))/pg(sol[:,1][-1])))
    #print('$N_{eff}$ = ', (8/7) *(11/4)**(4/3) * ((pv(sol[:,0][-1])-pg(sol[:,1][-1]))/pg(sol[:,1][-1])))
    #print('$N_{eff}$ = ', 3 *(11/4)**(4/3) * ((sol[:,0][-1])/sol[:,1][-1]))
    
    
    
if __name__ == "__main__":
    main()
    
