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

class Student(Person):
    def __init__(self, name, age, _class):
        super(Student, self).__init__(name, age)
        self.__class = _class

    def introduce(self):
        return super(Student, self).introduce() + "I am a Student. I am at Class %d." %  self.__class

class Worker(Person):
    def __init__(self, name, age):
        super(Worker, self).__init__(name, age)

    def introduce(self):
        return super(Student, self).introduce() + "I am a Worker. I have a job."