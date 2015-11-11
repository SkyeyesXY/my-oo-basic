# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:03:02 2015

@author: Skyeyes
"""

class Class(object):
    leader = 'None'
    master = 'None'
    master_age = 'None'
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
        return Teacher(self.master, self.master_age, self.number).Newleader(cls)        
        
    def appendMember(self, cls):
        cls._class = self.number
        return Teacher(self.master, self.master_age, self.number).Newstudent(cls)
        
        

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
            return super(Student, self).introduce() + " I am a Student. I am Leader of Class %d." %  self._class       
        else:
            return super(Student, self).introduce() + " I am a Student. I am at Class %d." %  self._class
    
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
            return super(Teacher, self).introduce() + " I am a Teacher. I teach No Class."
        else:
            return super(Teacher, self).introduce() + " I am a Teacher. I teach Class %s." % self.__classes 
            
    def isTeaching(self, cls):
        for i in self.__classes[0]:
            if Class(i).isIn(cls):
                return True
        return False
               
    def master_class(self, cls):
        cls.master = self.name
        cls.master_age = self.age
        
    def Newstudent(self, cls):
        return "I am %s. I know %s has joined Class %d." % (self.name, cls.name, cls._class)
        
    def Newleader(self, cls):
        return "I am %s. I know %s become Leader of Class %d." % (self.name, cls.name, cls._class)