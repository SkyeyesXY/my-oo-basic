# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:39:24 2015

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
        return super(Student, self).introduce() + "I am a Student. I am at Class %d." %  self.__class
    
    def get_class(self):
        return self.__class
        
    def get_name(self):
        return self.name
class Teacher(Person):
    def __init__(self, name, age, _class = 0):
        super(Teacher, self).__init__(name, age)
        self.__class = _class

    def introduce(self):
        if self.__class == 0:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach No Class."
        else:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach Class %d." % self.__class
            
    def introduceWith(self, cls):
        if cls.get_class() == self.__class:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach %s." % cls.get_name()
        else:
            return super(Teacher, self).introduce() + "I am a Teacher. I don't teach %s." % cls.get_name()