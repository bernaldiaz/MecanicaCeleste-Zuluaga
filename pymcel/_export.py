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
#  .//Fundamentos.Calculo.Series.ipynb
# ########################################

def coeficientes_fourier(funcion,T,k,args=()):
    #Funciones externas
    from scipy.integrate import quad
    from numpy import sin,cos

    #Parametro omega
    w=2*pi/T
    
    #Determina los coeficientes en t:
    f=lambda t:funcion(t,*args)
    As=[2*quad(f,0,T,args=args)[0]/T]
    Bs=[0]
    for n in range(1,k+1):
        f_cos_n=lambda t:funcion(t,*args)*cos(n*w*t)
        As+=[2*quad(f_cos_n,0,T)[0]/T]
        f_sin_n=lambda t:funcion(t,*args)*sin(n*w*t)
        Bs+=[2*quad(f_sin_n,0,T)[0]/T]
    
    return As,Bs


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
#  .//Fundamentos.Conicas.Areas.ipynb
# ########################################

# ########################################
#  .//Fundamentos.Conicas.Rotaciones.ipynb
# ########################################

def conica_de_elementos(p=10.0,e=0.8,i=0.0,Omega=0.0,omega=0.0,
                        df=0.1,
                        elev=30,azim=60,
                        figreturn=False):

    #Convierte elementos angulares en radianes
    from numpy import pi
    p=float(p)
    e=float(e)
    i=float(i)*pi/180
    Omega=float(Omega)*pi/180
    omega=float(omega)*pi/180
    
    #Compute fmin,fmax
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

    #Distancia al periapsis
    q=p/(1+e)

    #Distancia al foco
    from numpy import sin,cos
    rs=p/(1+e*cos(fs))

    #Coordenadas
    xs=rs*(cos(Omega)*cos(omega+fs)-cos(i)*sin(Omega)*sin(omega+fs))
    ys=rs*(sin(Omega)*cos(omega+fs)+cos(i)*cos(Omega)*sin(omega+fs))
    zs=rs*(cos(fs)*sin(omega)*sin(i)+sin(fs)*cos(omega)*sin(i))
    
    #Posición del periapsis (f=0)
    xp=q*(cos(Omega)*cos(omega)-cos(i)*sin(Omega)*sin(omega))
    yp=q*(sin(Omega)*cos(omega)+cos(i)*cos(Omega)*sin(omega))
    zp=q*sin(omega)*sin(i)
    
    #Posición del nodo ascendente
    rn=p/(1+e*cos(omega))
    xn=rn*cos(Omega)
    yn=rn*sin(Omega)
    zn=0
    
    #Gráfico
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    plt.close("all")
    fig=plt.figure()
    ax=fig.gca(projection='3d')

    #Gráfica de los puntos originales
    ax.plot(xs,ys,zs,'b-')
    
    #Posición del periapsis
    ax.plot([0,xp],[0,yp],[0,zp],'r-')

    #Posición del nodo ascendente
    ax.plot([0,xn],[0,yn],[0,zn],'g-')

    #Fija punto de vista
    ax.view_init(elev=elev,azim=azim)
    
    #Decoración
    from pymcel.plot import fija_ejes3d_proporcionales
    xrange,yrange,zrange=fija_ejes3d_proporcionales(ax);

    ax.set_title(f"Cónica con:"+                 f"$p={p:.2f}$, $e={e:.2f}$, "+                 f"$i={i*180/pi:.2f}$, "+                 f"$\Omega={Omega*180/pi:.1f}$, "+                 f"$\omega={Omega*180/pi:.1f}$"
            )
    
    #Dibuja Ejes
    ax.plot([0,xrange[1]],[0,0],[0,0],'k-')
    ax.plot([0,0],[0,yrange[1]],[0,0],'k-')
    ax.plot([0,0],[0,0],[0,zrange[1]],'k-')
    ax.text(xrange[1],0,0,"$x$",ha='left',va='top')
    ax.text(0,yrange[1],0,"$y$",ha='left',va='top')
    ax.text(0,0,zrange[1],"$z$",ha='left',va='bottom')

    fig.tight_layout();
    
    if figreturn:return fig


# ########################################
#  .//Fundamentos.ProblemasSeleccionados.ipynb
# ########################################

# ########################################
#  ./build/probs/Fundamentos.Problemas.ipynb
# ########################################
