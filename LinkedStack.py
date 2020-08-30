# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:12:12 2020

@author: Administrator
"""

class Empty(ValueError):
    
    pass

class LinkedStack:
    
    class _Node:
        
        __slots__='_element','_sub'
        
        def __init__(self,element,sub):
            
            self._element=element
            self._sub=sub
    

    def __init__(self):
        
        self._head=None
        self._size=0
        
    def __len__(self):
        
        return self._size
    
    def is_empty(self):
        
        return self._size==0
    
    def push(self,element):
        
        self._head=self._Node(element=element,sub=self._head)
        self._size+1
        
    def top(self):
        
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        
        if self.is_empty():
            raise Empty('Stack is empty')
        answer=self._head._element
        self._head=self._head._sub
        self._size-=1
        return answer

def revserse_file(file_name):
    
    s=LinkedStack()
    for line in open(file_name):
        s.push(line.rstrip'\n'))
    output=open(file_name,'w')
    while not s.is_empty():
        output.write(s.pop()+'\n')
    output.close()

def is_matched(expression):
    
    left='([{'
    right=')]}'
    s=LinkedStack()
    for char in expression:
        if char in left:
            s.push(char)
        elif char in right:
            if s.is_empty():
                return False
            if right.index(char)!=left.index(s.pop()):
                return False
    return s.is_empty()

def is_matched_html(text):
    
    s=LinkedStack()
    idx_left=text.fing('<')
    while idx_left!=-1:
        idx_right=text.find('>',idx_left+1)
        if idx_right==-1:
            return False
        tag=text[idx_left+1:idx_right]
        if not tag.startwith('/'):
            s.push(tag)
        else:
            if s.is_empty():
                return False
            if tag[1:]!=s.pop():
                return False
        idx_left=text.find('<',idx_right+1)
    return s.is_empty()

        
            









































    






























    
        