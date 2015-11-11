# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:33:42 2015

@author: Skyeyes
"""

class Class(object):
    leader = 'None'
    def __init__(self, number):
        self.number = number
        
    def isIn(self, cls):
        if cls._class != self.number:
            return False
        else:
            return True
        
    def assignLeader(self, cls):
        if not self.isIn(cls):
            return 'It is not one of us.'
        self.leader = cls.get_name()
        return self.leader          
        
    def appendMember(self, cls):
        cls._class = self.number
        
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return "My name is %s. I am %d years old." % (self.name, self.age)

class Student(Person):
    def __init__(self, name, age, number):
        super(Student, self).__init__(name, age)
        self._class = Class(number).number

    def introduce(self, cls):
        if self.name == cls.leader:            
            return super(Student, self).introduce() + "I am a Student. I am Leader of Class %d." %  self._class       
        else:
            return super(Student, self).introduce() + "I am a Student. I am at Class %d." %  self._class
    
    def get_class(self):
        return self._class
        
    def get_name(self):
        return self.name
        
class Teacher(Person):
    def __init__(self, name, age, *args):
        super(Teacher, self).__init__(name, age)
        self.__classes = args

    def introduce(self):
        if len(self.__classes) == 0:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach No Class."
        else:
            return super(Teacher, self).introduce() + "I am a Teacher. I teach Class %s." % self.__classes 
            
    def isTeaching(self, cls):
        for i in self.__classes[0]:
            if Class(i).isIn(cls):
                return True
        return False