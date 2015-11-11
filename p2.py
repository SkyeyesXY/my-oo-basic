# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:34:28 2015

@author: Skyeyes
"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self): 
        return "My name is %s. I am %d years old." % (self.name, self.age)
        
class Student(Person):
    def __init__(self, name, age, _class):
        super(Student, self).__init__(name, age)
        self.__class = _class
        
    def introduce(self):
        return "I am a Student. I am at Class %d." % self.__class