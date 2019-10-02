#!/usr/bin/env python
# coding: utf-8

# ########################################
#  .//Prefacio.ipynb
# ########################################

# ########################################
#  .//Agradecimientos.ipynb
# ########################################

# ########################################
#  .//Introduccion.ipynb
# ########################################

def calcula_discriminante(a,b,c):
    """Calcula el discriminante de una ecuación de segundo grado.
    
    Argumentos:
    ==========
    a,b,c (float): Coeficientes
    
    Retorna:
    =======
    d (float): Valor del discriminante
    
    """
    a=1
    b=-1
    c=2
    disc=b**2-4*a*c
    return disc


# ########################################
#  .//Fundamentos.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Mecanica.Cinematica.Cantidades.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Mecanica.Cinematica.SolucionEdM.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Mecanica.Cinematica.SolucionNumerica.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.Formulacion.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.ConstantesMovimiento.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.ConstantesMovimiento.Energia.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.TeoremaVirial.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.SolucionNumerica.ipynb
# ########################################

def eom_ncuerpos(Y,t,N,mus):    
    import numpy as np
    dYdt=np.zeros(6*N)

    #Primer conjunto de ecuaciones
    dYdt[:3*N]=Y[3*N:]
    
    #Segundo conjunto de ecuaciones
    for k in range(3*N,6*N):
        l=k%3
        i=int(np.floor((k-3*N)/3))
        for j in range(N):
            if j==i:continue
            rij=(Y[3*i]-Y[3*j])**2+                (Y[3*i+1]-Y[3*j+1])**2+                (Y[3*i+2]-Y[3*j+2])**2
            dYdt[k]+=-mus[j]*(Y[3*i+l]-Y[3*j+l])/rij**1.5
            
    return dYdt


def sistema_a_Y(sistema):
    import numpy as np
    mus=[]
    rs=[]
    vs=[]
    N=0
    for particula in sistema:
        m=particula['m']
        if m>0:
            mus+=[m]
            rs+=particula["r"]
            vs+=particula["v"]
            N+=1
    Y=rs+vs
    return N,np.array(mus),np.array(Y)


def solucion_a_estado(solucion,Nparticulas,Ntiempos):
    rs=np.zeros((Nparticulas,Ntiempos,3))
    vs=np.zeros((Nparticulas,Ntiempos,3))
    for i in range(N):
        rs[i]=solucion[:,3*i:3*i+3]
        vs[i]=solucion[:,3*N+3*i:3*N+3*i+3]
    return rs,vs

