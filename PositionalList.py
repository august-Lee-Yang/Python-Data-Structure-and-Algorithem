# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:57:30 2020

@author: Administrator
"""

from DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    
    class Position:
        
        def __init__(self,container,node):
            
            self._container=container
            self._node=node
            
        def get_element(self):
            
            return self._node._element
    
    def _validate(self,position):
        
        return position._node
    
    def _make_position(self,node):
        
        if node is None:
            return None
        else:
            return self.Position(container=self,node=node)
        
    def first(self):
        
        return self._make_position(node=self._header._subsequent)
    
    def last(self):
        
        return self._make_position(node=self._trailer._previous)
        
    def before(self,position):
        
        node=self._validate(position=position)
        return self._make_position(node=node._previous)
    
    def after(self,position):
        
        node=self._validate(position=position)
        return self._make_position(node=node._subsequent)
    
    def __iter__(self):
        
        cursor=self.first()
        while cursor is not None:
            yield cursor.get_element()
            cursor=self.after(position=cursor)
    
    def _insert_between(self,element,previous,subsequent):
        
        node=super()._insert_between(element=element,previous=previous,subsequent=subsequent)
        return self._make_position(node=node)
    
    def _add_first(self,element):
        
        return self._insert_between(element=element,previous=self._header,subsequent=self._header._subsequent)
    
    def _add_last(self,element):
        
        return self._insert_between(element=element,previous=self._trailer._subsequent,subsequent=self._trailer)
    
    def _add_before(self,element,position):
        
        node=self._validate(position=position)
        return self._insert_between(element=element,previous=node._previous,subsequent=node)
    
    def _add_after(self,element,position):
        
        node=self._validate(position=position)
        return self._insert_between(element=element,previous=node,subsequent=node._subsequent)
    
    def _delete(self,position):
        
        node=self._validate(position=position)
        return self._delete_node(node=node)














    







































    