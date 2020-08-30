# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:20:12 2020

@author: Administrator
"""

def bisection(left,right,tol=1.0e-9,max_iter=100):
    if f(left)==0:
        return left
    if f(right)==0:
        return right
    if f(left)*f(right)>0:
        raise ValueError('No root in the interval')
    i=0
    if np.abs(f(left)-f(right))<tol and i<max_iter :
        middle=(right+left)/2
        if f(middle)==0:
            return middle
        elif f(middle)*f(left)>0:
            left=middle
        else:
            right=middle
        i+=1
    print('Root is occured at x=%s'%(left+right)/2)
    print('Number of iterations:',i)
    
    

def newton_method(x0,tol=1.0e-9,max_iter=100):
    if f(x0)==0:
        return x0
    for i in range(max_iter):
        x=x0-f(x0)/df(x0)
        if np.abs(f(x)-f(x0))<tol:
            return x
        x0=x
    print('Root is occured at x=',x)
    print('Number of iterations:',i)
    return x




def newton_bisection(left,right,tol=1.0e-9,max_iter=100):
    if f(left)==0:
        return left
    if f(right)==0:
        return right
    if f(right)*f(left)>0:
        raise ValueError('No root')
    i=0
    if np.abs(f(left)-f(right))<tol and i<max_iter:
        x=(left+right)/2
        if np.abs(f(x))<tol:
            return x
        if f(left)*f(x)>0:
            left=x
        else:
            right=x
        try:
            dx=-f(x)/df(x)
        except ZeroDivisionError:dx=right-left
        x=x+dx
        i+1
    print('Root is occured at x=%s'%(left+right)/2)
    print('Number of iterations:',i)
    
        
        
    
    
    
            