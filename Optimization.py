# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 14:59:17 2020

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

'''
x1=np.linspace(start=-10,stop=10,num=100)
x2=np.linspace(start=-10,stop=10,num=100)
x1,x2=np.meshgrid(x1,x2)
y=np.sqrt(np.square(x1)+np.square(x2))
#plt.scatter(x1,x2,c=y,cmap='rainbow')
plt.figure(figsize=(12,12))
plt.style.use('seaborn-paper')
cp=plt.contour(x1,x2,y)
plt.clabel(cp,inline=1,fontsize=10)
plt.savefig(fname=r'D:/used_car/pic.pdf',dpi=1000)
'''



def gradient_descent(x0,max_iter=1000,tol=1.0e-7,rate=0.01):
    '''
    f(x)=x.T*A*x+b.T*x
    max_iter----最大迭代次数
    tol----允许误差
    rate----每次迭代步长
    '''
    A=np.array([[2,1],[1,1]],dtype=float)
    b=np.array([[1],[-1]],dtype=float)
    f=lambda x:np.dot(A,x)+np.dot(b.T,x)
    df=lambda x:2*np.dot(A,x)+b
    x_list=[]
    for _ in range(max_iter):
        x1=x0-rate*df(x0)
        criteria=np.max(np.abs(x1-x0))<tol or np.max(df(x1))<tol
        if criteria:
            break
        x0=x1
        x_list.append(x0)
    return x_list
        

def plot_contour(start,stop,x=None,file_name=None):
    
    plt.figure(figsize=(12,12))
    plt.style.use('ggplot')
    f=lambda x1,x2:x1-x2+2*np.square(x1)+np.square(x2)+2*x1*x2
    x1=np.linspace(start=start,stop=stop,num=100)
    x2=np.linspace(start=start,stop=stop,num=100)
    x1,x2=np.meshgrid(x1,x2)
    cp=plt.contour(x1,x2,f(x1,x2))
    plt.clabel(cp,inline=1,fontsize=10)
    if x is not None:
        for value in x:
            plt.scatter(value[0],value[1])
    if file_name is not None:
        plt.savefig(fname=file_name,dpi=1000)
    else:
        plt.savefig(fname=r'D:/used_car/contour.pdf',dpi=1000)
    


   


def conjugate_gradient(A,b,x0,max_iter=100,tol=1.0e-7,rate=0.15):
    
    df=lambda x:2*np.dot(A,x)+b
    s=-df(x0)
    x_list=[]
    for _ in range(max_iter):
        x1=x0+rate*s
        df_x1=df(x1)
        criteria=np.max(np.abs(x1-x0))<tol or np.max(np.abs(df_x1))<tol
        if criteria:
            break
        u=np.dot(df_x1.T,df_x1)/np.dot(df(x0).T,df(x0))
        s=-df_x1+u*s
        x0=x1
        x_list.append(x1)
    return x_list


def DFP(A,b,x0,max_iter=100,tol=1.0e-7,rate=0.15):
    n=len(A)
    B=np.eye(n,n)
    df=lambda x:2*np.dot(A,x)+b
    x_list=[]
    for _ in range(max_iter):
        s=-np.dot(B,df(x0))
        x1=x0+rate*s
        d=x1-x0
        g=df(x1)-df(x0)
        if np.max(np.abs(d))<tol or np.max(np.abs(g))<tol:
            break
        u=np.dot(B,g)
        delta_B=rate*np.outer(s,s)/np.dot(s.T,g)-np.outer(u,u)/np.dot(g.T,u)
        B=B+delta_B
        x0=x1
        x_list.append(x0)
    return x_list


def BFGS(A,b,x0,max_iter=100,tol=1.0e-7,rate=0.15):
    n=len(A)
    B=np.eye(n)
    df=lambda x:2*np.dot(A,x)+b
    x_list=[]
    for _ in range(max_iter):
        s=-np.dot(B,df(x0))
        x1=x0+rate*s
        d=rate*s
        g=df(x1)-df(x0)
        if np.max(np.abs(d))<tol or np.max(np.abs(d))<tol:
            break
        u=np.dot(d.T,g)
        w=np.outer(d,g)
        c=np.dot(d.T,g)
        c=(1+np.dot(g.T,np.dot(B,g))/c)
        delta_B=(c*np.outer(d,d)-np.dot(w,B)-np.dot(B,w.T))/u
        B=B+delta_B
        x0=x1
        x_list.append(x0)
    return x_list
    

if __name__=='__main__':
    A=np.array([[2,1],[1,1]],dtype=float)
    b=np.array([1,-1],dtype=float).reshape(2,1)
    x=np.array([0,0],dtype=float).reshape(2,1)
    y=DFP(A,b,x)




















    