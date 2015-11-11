# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:36:23 2015

@author: Skyeyes
"""

class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def introduce(self): 
        return "My name is %s. I am %d years old." % (self.__name, self.__age)
