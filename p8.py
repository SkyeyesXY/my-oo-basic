# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:47:50 2015

@author: Skyeyes
"""

class Class(object):
    leader = 'None'
    def __init__(self, number):
        self.number = number
        
    def assignLeader(self, cls):
        self.leader = cls.get_name()
        return self.leader

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is %s. I am %d years old." % (self.name, self.age)
    
    def get_name(self):
        return self.name
        
class Student(Person):
    def __init__(self, name, age, number):
        super(Student, self).__init__(name, age)
        self.__class = Class(number).number

    def introduce(self, cls):
        if self.name == cls.leader:            
            return super(Student, self).introduce() + "I am a Student. I am Leader of Class %d." %  self.__class       
        else:
            return super(Student, self).introduce() + "I am a Student. I am at Class %d." %  self.__class

class Teacher(Person):
    def __init__(self, name, age, _class = 0):
        super(Teacher, self).__init__(name, age)
        self.__class = _class

    def introduce(self):
        if self.__class == 0:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach No Class."
        else:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach Class %d." % self.__class