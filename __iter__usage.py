# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:32:58 2020

@author: Administrator
"""
class range_num:
    
    def __init__(self,stop,start=0):
        
        self._start=start-1
        self._stop=stop
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        self._start+=1
        if self._start==self._stop:
            raise StopIteration
        return self._start    
    


class Squares:
    
    def __init__(self,start,stop):
        
        self._value=start-1
        self._stop=stop
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        if self._value==self._stop:
            raise StopIteration
        self._value+=1
        return self._value**2


class Fibonacci:
    
    def __init__(self,stop):
        
        self._start=0
        self._stop=stop
        self._value=1
        self._step=0
        
    def __iter__(self):
        
        return self
    
    def __next__(self):
        
        if self._step==self._stop:
            raise StopIteration
        self._step+=1
        self._start,self._value=self._value,self._start+self._value
        return self._value
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    