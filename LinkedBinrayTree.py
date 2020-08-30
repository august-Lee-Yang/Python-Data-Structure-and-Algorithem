# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:30:56 2020

@author: Administrator
"""
from LinkedQueue import LinkedQueue

class LinkedBinaryTree:
    
    class _Node:
        
        __slots__='_element','_parent','_left','_right'
        
        def __init__(self,element,parent=None,left=None,right=None):
            
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
            
    class Position:
        
        def __init__(self,container,n):
            
            self._container=container
            self._node=n
            
        def get_element(self):
            
            return self._node._element
        
    def _validate(self,p):
        
        if not isinstance(p,self.Position):
            raise TypeError('p must be Position class')
        if p._container is not self:
            raise ValueError('p does not belong to this class')
        if p._node is p._node._parent:
            raise ValueError('This class is not valid')
        return p._node
    
    def _make_position(self,node):
        
        if node is None:
            return None
        else:
            return self.Position(container=self,n=node)
    
    def __init__(self):
        
        self._root=None
        self._size=0
        
    def is_empty(self):
        
        return self._size==0
    
    def root(self):
        
        return self._make_position(self._root)
    
    def left(self,position):
        
        node=self._validate(p=position)
        return self._make_position(node=node._left)
    
    def right(self,position):
        
        node=self._validate(p=position)
        return self._make_position(node=node._right)
    
    def parent(self,position):
        
        node=self._validate(p=position)
        return self._make_position(node=node._right)
    
    def children(self,p):
        
        if self.left(position=p) is not None:
            yield self.left(position=p)
        if self.right(position=p) is not None:
            yield self.right(position=p)
    
    def _add_root(self,e):
        
        if self._root is not None:
            raise ValueError('Root exists')
        node=self._Node(element=e)
        self._root=node
        self._size+=1
        return self._make_position(node=node)
    
    def _add_right(self,e,position):
        
        node=self._validate(p=position)
        if node._left is not None:
            raise ValueError('Left child exists')
        node._left=self._Node(element=e,parent=node)
        self._size+=1
        return  self._make_position(node=node._left)
    
    def _add_left(self,e,position):
        
        node=self._validate(p=position)
        if node._right is not None:
            raise ValueError('Right child exists')
        node._right=self._Node(element=e,parent=node)
        self._size+=1
        return self._make_position(node=node._right)
    
    def _subtree_preorder(self,posi):
        
        yield posi
        for child in self.children(p=posi):
            for p in self._subtree_preorder(posi=child):
                yield p
    def _subtree_postorder(self,posi):
        
        for child in self.children(p=posi):
            for p in self._subtree_postorder(posi=child):
                yield p
        yield posi
        
    def _breadth(self,posi):
        
        fringe=LinkedQueue()
        fringe.enqueue(posi)
        while not fringe.is_empty():
            p=fringe.dequeue()
            yield p
            for child in self.children(p=p):
                fringe.enqueue(child)
                
                
    def position_pre(self):
        
        if not self.is_empty():
            for p in self._subtree_preorder(posi=self.root()):
                yield p
                
    def position_post(self):
        
        if not self.is_empty():
            for p in self._subtree_postorder(posi=self.root()):
                yield p
    
    def position_breadth(self):
        
        if not self.is_empty():
            for p in self._breadth(posi=self.root()):
                yield p



        
        
    
  


T=LinkedBinaryTree()
marker=T._add_root(e='Agust Lee')

T._add_left(e='Numerical Method',position=marker)
T._add_right(e='Steepest gradient descent',position=marker)
marker=T.left(position=marker)
T._add_left(e='Je suis chions',position=marker)
marker=T._add_right(e='Life is short,I am using Python',position=marker)
T._add_left(e='gausse seidel method to solve sparse matrix',position=marker)
marker=T._add_right(e='mathematical analysis',position=marker)
T._add_right(e='Linear Algrbra',position=marker)
T._add_left(e='Data structure and algorithm',position=marker)

if __name__=='__main__':
    for p in T.position_breadth():
        print(p.get_element())
    print('\n'*4)
    for p in T.position_post():
        print(p.get_element())
    print('\n'*4)
    for p in T.position_pre():
        print(p.get_element())




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            