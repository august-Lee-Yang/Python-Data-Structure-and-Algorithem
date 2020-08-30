# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:19:28 2020

@author: Administrator
"""

class Empty(ValueError):
    
    pass

class LinkedQueue:
    
    class _Node:
        
        __slots__='_element','_sub'
        
        def __init__(self,element,sub):
            
            self._element=element
            self._sub=sub
            
    def __init__(self):
        
        self._head=None
        self._tail=None
        self._size=0
        
    def __len__(self):
        
        return self._size
    
    def is_empty(self):
        
        return self._size==0
    
    def first(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element
    
    def enqueue(self,element):
        
        node=self._Node(element=element,sub=None)
        if self.is_empty():
            self._head=node
        else:
            self._tail._sub=node
        self._tail=node
        self._size+=1
        
    def dequeue(self):
        
        if self.is_empty():
            raise Empty('Queue is Empty')
        answer=self._head._element
        self._head=self._head._sub
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    