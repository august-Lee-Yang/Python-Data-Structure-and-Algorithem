
import numpy as np

def forward_substitution(L,b):
    '''前向替代法，用于线性方程: Lx=y, L为下三角矩阵'''
    n=len(b)
    x=[None]*n
    for k in range(n):
        x[k]=(b[k]-np.dot(L[k,0:k-1],x[0:k-1]))/L[k,k]
    return x

def backward_substitution(U,b):
    '''后向替代法，用于解线性方程Ux=y，U为上三角矩阵'''
    n=len(b)
    x=[None]*n
    for k in range(n-1,-1,-1):
        x[k]=(b[k]-np.dot(U[k,k+1:n],x[k+1:n]))/U[k,k]
    return x

def gaussain_elimination(A,b):
    '''高斯消元法，A为n-by-n矩阵,经过变换后，A的上上三角部分存储变换后的元素
    如果需要返回L矩阵，则将高斯算子multiplier存储到A[i,k]的位置。如果需要节省内存空间
    可以用b存储x
    for k in range(n-1,-1,-1):
        b[k]=(b[k]-np.dot(A[k,k+1:n),b[k+1:n])/A[k,k]
    return b'''
    n=len(b)
    for k in range(n-1):
        '''遍历列'''
        for i in range(k+1,n):
            if A[i,k]!=0:
                multiplier=A[i,k]/A[k,k]
                A[i,k+1:n]=A[i,k+1:n]-multiplier*A[k,k+1]
                b[i]=b[i]-multiplier*b[k]
    x=backward_substiturion(A,b)
    return x

def swaprows(v,i,j):
    '''换行函数，当v是一个向量时，交换i-th, j-th元素'''
    '''当v是一个矩阵时，交换i-th,j-th行'''
    if len(v.shape)==1:
        v[i],v[j]=v[j],v[i]
    else:
        temp=v[i].copy()
        v[i]=v[j]
        v[j]=temp

def swapcol(v,i,j):
    temp=v[:,j].copy()
    v[:,j]=v[:,i]
    v[:,i]=temp

def gaussPivot(A,b,tol=1.0e-9):
    '''s[i]=np.max(np.abs(A[i,:]))第i-th行绝对值最大的元素'''
    n=len(b)
    s=np.zeros(n)
    for i in range(n):
        s[i]=np.max(np.abs(A[i,:]))
    for k in range(n-1):        
        p=np.argmax(np.abs(A[k:n,k])/s[k:n])+k
        if np.abs(A[p,k])<tol:
            raise ValueError('Matrix is singular')
        if p!=k:
            swaprows(b,k,p)
            swaprows(s,k,p)
            swaprows(A,k,p)
            
        for i in range(k+1,n):
            if A[i,k]!=0:
                multiplier=A[i,k]/A[k,k]
                A[i,k+1:n]=A[i,k+1:n]-multiplier*A[k,k+1]
                b[i]=b[i]-multiplier*b[k]
    x=backward_substitution(A,b)
    return x
    
def jacobi_method(A,b,x0,max_iter=1000,tol=1.0e-9):
    m,n=A.shape
    if m!=n:
        raise IndexError('Matrix must be a square')
    for k in range(n):
        A[k,:]=-A[k,:]/A[k,k]
        b[k]=b[k]/A[k,k]
        A[k,k]=0
    x_list=[]
    for _ in range(max_iter):
        x=np.dot(A,x0)+b
        if np.max(np.abs(x-x0))/np.max(np.abs(x))<tol:
            break
        x_list.append(x)
        x0=x
    return x_list

def gausse_seidel(A,b,x0,max_iter=1000,tol=1.0e-9):
    m,n=A.shape
    if m!=n:
        raise IndexError('Matrix must be a square')
    for k in range(n):
        A[k,:]=-A[k,:]/A[k,k]
        b[k]=b[k]/A[k,k]
        A[k,k]=0
    x_list=[]
    for _ in range(max_iter):
        x=x0
        for k in range(n):
            x[k]=np.dot(A[k,:],x)+b
        if np.max(np.abs(x-x0))/np.max(np.abs(x))<tol:
            break
        x_list.append(x)
    return x_list

def conjugate_gradient(A,b,x0,max_iter=1000,tol=1.0e-9):
    '''
    共轭梯度法
    A----正定矩阵
    '''
    r0=b-np.dot(A,x0)
    v1=r0.copy()
    x_list=[]
    for _ in range(max_iter):
        w=np.dot(A,v1)
        u=np.dot(r0.T,r0)
        t=u/np.dot(v1.T,w)
        x1=x0+t*v1
        if np.max(np.abs(x1-x0))<tol:
            break
        r1=r0-t*w
        s=np.dot(r1.T,r1)/u
        v1=r1+s*v1
        r0=r1
        x0=x1
        x_list.append(x1)
    return x_list
'''
A=np.array([[4,3,0],[3,4,-1],[0,-1,4]],dtype=float)
x=np.array([0,0,0],dtype=float).reshape(3,1)
b=np.array([24,30,-24],dtype=float).reshape(3,1)
x_list=conjugate_gradient(A=A,b=b,x0=x)
'''














































































       