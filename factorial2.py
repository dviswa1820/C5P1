# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:49:28 2019

@author: dviswa1820
"""


class factorial2: 
      
 def ret_fact_recursive(a):
       if((a==0)or(a==1)):
          fact=1
          return fact
       else:
           fact=a*factorial2.ret_fact_recursive(a-1)
           #fact=a*5
           return fact

       
  

    
 
