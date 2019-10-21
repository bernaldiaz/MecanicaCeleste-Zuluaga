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
#  .//Fundamentos.Calculo.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Calculo.Vectores.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Calculo.CalculoInfinitesimal.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Calculo.EcuacionesDiferenciales.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Calculo.CalculoVariacional.ipynb
# ########################################

# ########################################
#  .//Mecanica.ipynb
# ########################################

# ########################################
#  .//Mecanica.Cinematica.Cantidades.ipynb
# ########################################

# ########################################
#  .//Mecanica.Cinematica.SolucionEdM.ipynb
# ########################################

# ########################################
#  .//Mecanica.Cinematica.SolucionNumerica.ipynb
# ########################################

# ########################################
#  .//Mecanica.Dinamica.Cantidades.ipynb
# ########################################

# ########################################
#  .//Mecanica.Dinamica.Postulados.ipynb
# ########################################

# ########################################
#  .//Mecanica.Dinamica.SistemaParticulas.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.Formulacion.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.SolucionAnalitica.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.SolucionAnalitica.ConstantesMovimiento.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.SolucionAnalitica.Energia.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.SolucionAnalitica.Sintesis.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.TeoremaVirial.ipynb
# ########################################

# ########################################
#  .//ProblemaNCuerpos.SolucionNumerica.ipynb
# ########################################

def edm_ncuerpos(Y,t,N=2,mus=[]):    
    from numpy import zeros,floor
    dYdt=zeros(6*N)

    #Primer conjunto de ecuaciones
    dYdt[:3*N]=Y[3*N:]
    
    #Segundo conjunto de ecuaciones
    for k in range(3*N,6*N):
        l=k%3
        i=int(floor((k-3*N)/3))
        for j in range(N):
            if j==i:continue
            rij=(Y[3*i]-Y[3*j])**2+                (Y[3*i+1]-Y[3*j+1])**2+                (Y[3*i+2]-Y[3*j+2])**2
            dYdt[k]+=-mus[j]*(Y[3*i+l]-Y[3*j+l])/rij**1.5
            
    return dYdt


def sistema_a_Y(sistema):
    mus=[]
    r0s=[]
    v0s=[]
    N=0
    for particula in sistema:
        m=particula['m']
        if m>0:
            mus+=[m]
            r0s+=list(particula["r"])
            v0s+=list(particula["v"])
            N+=1
    from numpy import array
    Y0s=array(r0s+v0s)
    mus=array(mus)
    return N,mus,Y0s


def solucion_a_estado(solucion,Nparticulas,Ntiempos):
    from numpy import zeros
    rs=zeros((Nparticulas,Ntiempos,3))
    vs=zeros((Nparticulas,Ntiempos,3))
    for i in range(Nparticulas):
        rs[i]=solucion[:,3*i:3*i+3]
        vs[i]=solucion[:,3*Nparticulas+3*i:3*Nparticulas+3*i+3]
    return rs,vs


def plot_ncuerpos_3d(rs,vs,**opciones):
    #Número de partículas
    N=rs.shape[0]
    
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig=plt.figure()
    ax=fig.gca(projection='3d')

    for i in range(N):
        ax.plot(rs[i,:,0],rs[i,:,1],rs[i,:,2],**opciones);

    from pymcel.plot import fija_ejes3d_proporcionales
    fija_ejes3d_proporcionales(ax);
    fig.tight_layout();
    plt.show();


# ########################################
#  .//ProblemaNCuerpos.SolucionNumerica.ConstantesMovimiento.ipynb
# ########################################
