# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:16:38 2020

@author: Administrator
"""
from PositionalList import PositionalList

def insertion_sort(A):
    if len(A)>1:
        marker=A.first()
        while marker!=A.last():
            pivot=A.after(position=marker)
            value=pivot.get_element()
            if value>marker.get_element():
                marker=pivot
            else:
                walk=marker
                if walk!=A.first() and walk.get_element()>value:
                    walk=A.before(walk)
                A._delete(pivot)
                A._add_before(element=value,position=walk)
'''        
x=[15,22,25,29,36,23,53,11,42]
A=PositionalList()
marker=A._add_first(element=15)
for value in x[1:]:
    marker=A._add_after(element=value,position=marker)
B=insertion_sort(A=A)

print(A.before(position=marker).get_element())
marker=A.first()
print(marker.get_element())
walk=A.after(position=marker)
print(walk.get_element())
if marker.get_element()>walk.get_element():
    print('True')
else:
    print('False')
'''


def merge(A1,A2,A):
    id_1=id_2=0
    while id_1+id_2<len(A):
        if id_2==len(A2) or (id_1<len(A1) and A1[id_1]<A2[id_2]):
            A[id_1+id_2]=A1[id_1]
            id_1+=1
        else:
            A[id_1+id_2]=A2[id_2]
            id_2+=1
            
def merge_sort(A):
    n=len(A)
    if n<2:
        return
    mid=n//2
    A1=A[0:mid]
    A2=A[mid:n]
    merge_sort(A1)
    merge_sort(A2)
    merge(A1,A2,A)
    

from LinkedQueue import LinkedQueue

def quick_sort(A):
    n=len(A)
    if n<2:
        return
    pivot=A.first()
    L=LinkedQueue()
    E=LinkedQueue()
    G=LinkedQueue()
    while not A.is_empty():
        if A.first()<pivot:
            L.enqueue(A.dequeue())
        elif p<A.first():
            G.enqueue(A.dequeue())
        else:
            E.enqueue(A.dequeue())
    quick_sort(L)
    quick_sort(G)
    while not L.is_empty():
        A.enqueue(L.dequeue())
    while not E.is_empty():
        A.enqueue(E.dequeue())
    while not G.is_empty():
        A.enqueue(G.dequeue())
        
            


























































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    