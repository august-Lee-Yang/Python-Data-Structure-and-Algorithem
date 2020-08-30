# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 09:09:39 2020

@author: Administrator
"""

import time



def add_fx(number_1,number_2):
    
    print('Now, the function is used to implement the addition of two scalars')
    total=number_1+number_2
    str_1='%d + %d = %d' %(number_1,number_2,total)
    time.sleep(2)
    print(str_1)
    print('The function is successfully implemented')

def cal_time(f):
    start_time=time.time()
    f()
    end_time=time.time()
    time_diff=end_time-start_time
    print('%d seconds used to implement the function %s' %(time_diff,f))

def deco_1(f):
    def wrapper():
        start_time=time.time()
        f()
        end_time=time.time()
        time_diff=end_time-start_time
        print('%d senconds used to implement the function %s' %(time_diff,f))
    return wrapper

@deco_1
def fx():
    print('Now, we are at the stage before executing the function')
    print('Now, we are executing the function')
    time.sleep(2)
    print('2+5=7')
    print('Now, we are at the stage after executing the function')











    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    