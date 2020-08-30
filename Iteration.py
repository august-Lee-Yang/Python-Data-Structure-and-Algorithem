# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:11:00 2020

@author: Administrator
"""

import numpy as np

A=np.array([[4,3,0],[3,4,-1],[0,-1,4]],dtype=float)

    
def conjugate(A,x,b,max_iter=500):
    r0=b-np.dot(A,x)
    v1=r0.copy()
    for k in range(max_iter):
        t=np.dot(r0.T,r0)/np.dot(v1.T,np.dot(A,v1))
        x=x+t*v1
        r1=r0-t*np.dot(A,v1)
        s=np.dot(r1.T,r1)/np.dot(r0.T,r0)
        v2=r1+s*v1
    return x



x=np.array([[0],[0],[0]])
b=np.array([[24],[30],[-24]])


tf=lambda r,v:np.dot(r.T,r)/np.dot(v.T,np.dot(A,v))
xf=lambda x,t,v:x+t*v
rf=lambda r,t,A,v:r-t*np.dot(A,v)
sf=lambda r1,r0:np.dot(r1.T,r1)/np.dot(r0.T,r0)
vf=lambda r,s,v:r+s*v


def conju_gradient(A,x,b,max_iter=10,tol=1.0e-9):
    r0=b-np.dot(A,x)
    v1=r0.copy()
    tf=lambda r,v:np.dot(r.T,r)/np.dot(v.T,np.dot(A,v))
    xf=lambda x,t,v:x+t*v
    rf=lambda r,t,v:r-t*np.dot(A,v)
    sf=lambda r1,r0:np.dot(r1.T,r1)/np.dot(r0.T,r0)
    vf=lambda r,s,v:r+s*v
    for k in range(max_iter):
        t=tf(r=r0,v=v1)
        x=xf(x=x,t=t,v=v1)
        r=rf(r=r0,t=t,v=v1)
        s=sf(r1=r,r0=r0)
        v=vf(r=r,s=s,v=v1)
        v1=v
        r0=r
    return x

'''
if __name__=='__main__':
    x0=np.array([[0],[0],[0]])
    b=np.array([[24],[30],[-24]])
    A=np.array([[4,3,0],[3,4,-1],[0,-1,4]],dtype=float)
    x=[]
    x.append(x0)
    for k in range(1,5):
        x0=conju_gradient(A=A,x=x0,b=b,max_iter=k)
        x.append(x0)
'''
'''
def jacobi(A,b,x,max_iter=100,tol=1.0e-9):
    x_list=[]
    x0=x
    x_list.append(x0)
    for i in range(max_iter):
        x1=np.dot(T,x0)+C
        if np.max(np.abs(x1-x0))<tol:
            break
        x_list.append(x1)
        x0=x1
    return x_list,i
'''
'''
if __name__=='__main__':
    A=np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
    b=np.array([6,25,-11,15]).reshape(4,1)
    x0=np.array([0,0,0,0]).reshape(4,1)
    x,num_iter=jacobi(A=A,b=b,x=x0)
        
'''
def matrix_transform(A,b):
    m,n=A.shape
    if m!=n:
        raise IndexError('Matrix must be a sqaure matrix')
    T=A.copy()
    C=b.copy()
    for i in range(n):
        T[i,:]=-A[i,:]/A[i,i]
        T[i,i]=0
        C[i]=b[i]/A[i,i]
    return T,C

def jacobi(T,C,x,max_iter=100,tol=1.0e-9):
    x_list=[]
    x0=x
    x_list.append(x0)
    for i in range(max_iter):
        x1=np.dot(T,x0)+C
        if np.max(np.abs(x1-x0))<tol:
            break
        x_list.append(x1)
        x0=x1
    return x_list,i

'''
if __name__=='__main__':
    A=np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],float)
    b=np.array([6,25,-11,15],float).reshape(4,1)
    x=np.array([0,0,0,0],dtype=float).reshape(4,1)
    T,C=matrix_transform(A=A,b=b)  
    x,num_iter=jacobi(T=T,C=C,x=x)
'''        
def gausse_seidel(A,b,x0,max_iter=100,tol=1.0e-9):
    m,n=A.shape
    if m!=n:
        raise IndexEError('Matrix must be a square matrix')
    T,C=matrix_transform(A=A,b=b)
    x1=x0.copy()
    x_list=[]
    x_list.append(x1)
    for _ in range(max_iter):
        for i in range(n):
            x1[i]=np.dot(T[i,:],x1)+C[i]
        if np.max(np.abs(x1-x0))<tol:
            break
        x_list.append(x1)
        x0=x1.copy()
    return x_list
'''
if __name__=='__main__':
    A=np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]],float)
    b=np.array([6,25,-11,15],float).reshape(4,1)
    x=np.array([0,0,0,0],dtype=float).reshape(4,1)
    x_1=gausse_seidel(A=A,b=b,x0=x)
'''






















    
