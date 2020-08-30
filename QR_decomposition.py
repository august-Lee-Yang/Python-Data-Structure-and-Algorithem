# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:25:35 2020

@author: Administrator
"""
import numpy as np

def house(x):
    colmax=np.max(np.abs(x))
    x=x/colmax
    sigma=np.dot(x[1:],x[1:])
    u=x.copy()
    u[0]=1
    if sigma==0:
        beta=0
    else:
        mu=np.linalg.norm(x)
        if x[0]<=0:
            u[0]=x[0]-mu
        else:
            u[0]=-sigma/(x[0]+mu)
    beta=2*u[0]**2/(sigma+u[0]**2)
    u=u/u[0]
    return u,beta

def givens(xi,xj):
    if xj==0:
        c=1
        s=0
    elif np.abs(xi)>np.abs(xj):
        t=xj/xi
        s=1/np.sqrt(1+t**2)
        c=s*t
    else:
        t=xi/xj
        c=1/np.sqrt(1+t**2)
        s=c*t
    return s,c

def multi(c,s,x,y):
    temp=x.copy()
    x=c*x+s*y
    y=-s*temp+c*y
    return x,y

def givens_qr(A):
    m,n=A.shape
    for i in range(min(m-1,n)):
        for j in range(i+1,m):
            c,s=givens(A[i,i],A[j,i])
            A[i,:],A[j,:]=multi(c=c,s=s,x=A[i,:],y=A[j,:])
    return A

#A=np.array([[1,2,0],[-1,4,1],[-3,1,2]])



def house_qr(A):
    m,n=A.shape
    r=min(m-1,n)
    Q=np.eye(m,n)
    beta_list=np.zeros(r)
    for i in range(r):
        u,beta=house(A[i:m,i])
        w=np.dot(A[i:m,i:n].T,u)
        A[i:m,i:n]=A[i:m,i:n]-beta*np.outer(u,w)
        A[i+1:m,i]=u[1:m]
        beta_list[i]=beta
    for i in range(r-1,-1,-1):
        u=np.zeros(m)
        u[i]=1
        u[i+1:m]=A[i+1:m,i]
        w=np.dot(Q[i:m,i:n].T,u[i:m])
        Q[i:m,i:n]=Q[i:m,i:n]-beta_list[i]*np.outer(u[i:m],w)
    return Q,A
        



        
#D=np.array([[1,5,-1,8,3],[-1,4,12,6,-9],[0,3,16,-1,-6],[8,1,4,9,-2],[1,2,7,8,0],[15,22,17,-1,5],[23,-7,1,7,9]],dtype=float)
#D=house_qr(D)

#q,r=np.linalg.qr(D)

def house_hessenberg(A):
    
    m,n=A.shape
    if m!=n:
        raise IndexError('Matrix must be a square')
    for i in range(n-2):
        u,beta=house(A[i+1:n,i])
        w=np.dot(A[i+1:n,i:n].T,u)
        A[i+1:n,i:n]=A[i+1:n,i:n]-beta*np.outer(u,w)
        w=np.dot(A[:,i+1:n],u)
        A[:,i+1:n]=A[:,i+1:n]-beta*np.outer(w,u)
    return A

#B=np.array([[9,5,1,2,1],[9,7,10,5,8],[1,7,2,4,3],[4,3,2,10,5],[6,5,4,10,6]],dtype=float)
#A=np.array([[8,6,10,10],[9,1,10,5],[1,3,1,8],[10,6,10,1]],dtype=float)
#H=house_hessenberg(A) 
    
def qr_iteration(A):
    #此处执行了一次QR分解，并且计算R*Q,A是一个n-by-n矩阵，然后计算RQ，没有必要显性计算正交矩阵Q,A的上半部分存储R矩阵，下半部分
    #存储household向量u[1:]，为了计算RQ(Q=Q1*Q2*Q3****Q(n-1)),Qi=I-beta*u*u.T,u的前(i-1)个分量为0,第i个分量为1，剩余的
    #部分存储在A[i+1:n,i]
    n=len(A)
    beta_list=np.zeros(n-1)
    for i in range(n-1):
        u,beta=house(A[i:n,i])
        w=np.dot(A[i:n,i:n].T,u)
        A[i:n,i:n]=A[i:n,i:n]-beta*np.outer(u,w)
        A[i+1:n,i]=u[1:]
        beta_list[i]=beta
    R=A.copy()
    for i in range(n):
        R[i+1:n,i]=0
    for i in range(n-1):
        u=np.zeros(n)
        u[i]=1
        u[i+1:n]=A[i+1:n,i]
        w=np.dot(R[i:n,i:n],u[i:n])
        R[i:n,i:n]=R[i:n,i:n]-beta_list[i]*np.outer(w,u[i:n])
    return R

A=np.array([[8,6,10,10],[9,1,10,5],[1,3,1,8],[10,6,10,1]],dtype=float)
B=A.copy()
H=house_hessenberg(A)
#H=qr_iteration(H)        
Q,R=np.linalg.qr(H)
#m=np.dot(R,Q)
q,r=house_qr(H)
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        






