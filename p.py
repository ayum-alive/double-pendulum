import numpy as np
g=9.8
def f(s):
    a,b,w1,w2=s;d=a-b
    den=2-np.cos(2*d)
    dw1=(-g*3*np.sin(a)-g*np.sin(a-2*b)-2*np.sin(d)*(w2**2+w1**2*np.cos(d)))/den
    dw2=(2*np.sin(d)*(2*w1**2+2*g*np.cos(a)+w2**2*np.cos(d)))/den
    return np.array([w1,w2,dw1,dw2])
def run(a0):
    s=np.array([a0,a0,0,0.]);xs=[];dt=0.005
    for i in range(8000):
        k1=f(s);k2=f(s+dt/2*k1);k3=f(s+dt/2*k2);k4=f(s+dt*k3);s=s+dt/6*(k1+2*k2+2*k3+k4)
        xs.append((np.sin(s[0])+np.sin(s[1]),-np.cos(s[0])-np.cos(s[1])))
    return np.array(xs)
out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2.2 -2.2 4.4 4.4"><rect x="-3" y="-3" width="6" height="6" fill="#101420"/>'
for k,(a,c) in enumerate([(2.0,"#ff6b6b"),(2.0001,"#6bd5ff")]):
    P=run(a);out+='<polyline fill="none" stroke="%s" stroke-width=".008" points="%s"/>'%(c," ".join("%.3f,%.3f"%tuple(q) for q in P[::4]))
open('p.svg','w').write(out+'</svg>')
