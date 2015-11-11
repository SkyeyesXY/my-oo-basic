# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:32:42 2015

@author: Skyeyes
"""

class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def introduce(self):
        return "My name is %s. I am %d years old." % (self.__name, self.__age)

class Student(Person):
    def __init__(self, name, age, _class):
        super(Student, self).__init__(name, age)
        self.__class = _class

    def introduce(self):
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