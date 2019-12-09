# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:48:08 2019

@author: dviswa1820
"""

import unittest
from factorial2 import factorial2
class test_factorial2(unittest.TestCase):
    def test_print_fact(self):
        fact1=factorial2.ret_fact_recursive(5)
        self.assertEqual(fact1,120)
        #self.assertTrue(fact1==120)
        print(fact1)
if __name__=="__main__":
    unittest.main()        
