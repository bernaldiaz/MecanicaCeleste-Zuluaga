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
#  .//Fundamentos.Conicas.Geometria.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Conicas.Algebra.ipynb
# ########################################

def rota_puntos(R,x,y,z):
    from spiceypy import mxv
    from numpy import zeros_like
    N=len(x)
    xp=zeros_like(x)
    yp=zeros_like(y)
    zp=zeros_like(z)
    for i in range(N):
        xp[i],yp[i],zp[i]=mxv(R,[x[i],y[i],z[i]])
    return xp,yp,zp


def polinomio_segundo_grado(coeficientes,x,y):
    A,B,C,D,E,F=coeficientes
    P=A*x**2+B*x*y+C*y**2+D*x+E*y+F
    return P


# ########################################
#  .//Fundamentos.Conicas.Anomalias.ipynb
# ########################################

def puntos_conica(p,e,df=0.1):

    #Compute fmin,fmax
    from numpy import pi
    if e<1:
        fmin=-pi
        fmax=pi
    elif e>1:
        from numpy import arccos
        psi=arccos(1/e)
        fmin=-pi+psi+df
        fmax=pi-psi-df
    else:
        fmin=-pi+df
        fmax=pi-df
            
    #Valores del ángulo
    from numpy import linspace,pi
    fs=linspace(fmin,fmax,500)

    #Distancias 
    from numpy import cos
    rs=p/(1+e*cos(fs))

    #Coordenadas
    from numpy import sin
    xs=rs*cos(fs)
    ys=rs*sin(fs)
    from numpy import zeros_like
    zs=zeros_like(xs)
    
    return xs,ys,zs


# ########################################
#  .//Fundamentos.Conicas.Rotaciones.ipynb
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
    return fig


# ########################################
#  .//ProblemaNCuerpos.SolucionNumerica.ConstantesMovimiento.ipynb
# ########################################

def ncuerpos_solucion(sistema,ts):
    #Condiciones iniciales
    from pymcel.export import sistema_a_Y
    N,mus,Y0s=sistema_a_Y(sistema)
    
    #Masa total
    M=sum(mus)
    
    #Número de tiempos
    Nt=len(ts)
    
    #Solución
    from scipy.integrate import odeint
    solucion=odeint(edm_ncuerpos,Y0s,ts,args=(N,mus))
    
    #Extracción de las posiciones y velocidades
    from pymcel.export import solucion_a_estado
    rs,vs=solucion_a_estado(solucion,N,Nt)
    
    #Calcula las constantes de movimiento
    from numpy import zeros
    PCM=zeros(3)
    for i in range(N):
        PCM=PCM+mus[i]*vs[i,0,:]

    #Posición del CM como función del tiempo    
    RCM=zeros((Nt,3))
    for i in range(N):
        RCM=RCM+mus[i]*rs[i,:,:]
    RCM/=M

    #Momento angular
    from numpy import zeros,cross
    L=zeros(3)
    for i in range(N):
        L=L+mus[i]*cross(rs[i,0,:],vs[i,0,:])

    #Energía total
    from numpy.linalg import norm
    K=zeros(Nt)
    U=zeros(Nt)
    for i in range(N):
        K=K+0.5*mus[i]*norm(vs[i,:,:],axis=1)**2
        for j in range(N):
            if i==j:continue
            rij=norm(rs[i,:,:]-rs[j,:,:],axis=1)
            U+=-0.5*mus[i]*mus[j]/rij
    E=K[0]+U[0]
    
    #Constantes
    constantes=dict(M=M,
                    RCM=RCM,PCM=PCM,
                    L=L,K=K,U=U,E=E)
        
    #Posiciones y velocidades relativas al centro de masa    
    from numpy import subtract
    rps=rs-RCM
    vps=subtract(vs,PCM/M)
    
    #Devuelve las posiciones y velocidades
    return rs,vs,rps,vps,constantes


# ########################################
#  .//Problema2Cuerpos.ipynb
# ########################################

# ########################################
#  .//Problema2Cuerpos.Motivacion.ipynb
# ########################################

# ########################################
#  .//Problema2Cuerpos.ProblemaRelativo.ipynb
# ########################################
