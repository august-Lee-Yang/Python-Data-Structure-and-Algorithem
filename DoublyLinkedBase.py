# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:15:45 2020

@author: Administrator
"""
class Empty(ValueError):
    
    pass


class _DoublyLinkedBase:
    
    class _Node:
        
        __slots__='_element','_previous','_subsequent'
        
        def __init__(self,element,previous,subsequent):
            
            self._element=element
            self._previous=previous
            self._subsequent=subsequent
            
    def __init__(self):
        
        self._header=self._Node(element=None,previous=None,subsequent=None)
        self._trailer=self._Node(element=None,previous=None,subsequent=None)
        self._header._subsequent=self._trailer
        self._trailer._previous=self._header
        self._size=0
        
    def is_empty(self):
        
        return self._size==0
    
    def __len__(self):
        
        return self._size
    
    def _delete_node(self,node):
        
        previous=node._previous
        subsequent=node._subsequent
        subsequent._previous=previous
        previous._subsequent=subsequent
        self._size-=1
        element=node._element
        node._previous=node._subsequent=node._element=None
        return element
        
    def _insert_between(self,element,previous,subsequent):
        
        node=self._Node(element=element,previous=previous,subsequent=subsequent)
        previous._subsequent=node
        subsequent._previous=node
        self._size+=1
        return node
    
class LinkedDeque(_DoublyLinkedBase):
    
    def first(self):
        
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._header._subsequent._element
    
    def last(self):
        
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._trailer._previous
    
    def insert_first(self,element):
        
        self._insert_between(element=element,previous=self._header,subsequent=self._header._subsequent)
        
    def insert_last(self,element):
        
        self._insert_between(element=element,previous=self._trailer._previous,subsequent=self._trailer)
        
    def delete_first(self):
        
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._delete_node(self._header._subsequent)
    
    def delete_last(self):
        
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._delete_node(self._trailer._previous)
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        