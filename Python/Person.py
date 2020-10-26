#!/usr/bin/python3
# -*- coding: utf-8 -*- 

class Person( object ) : 
    def __init__(self,
                 firstname       = None, lastname        = None, age          = None, 
                 generaltitle    = None, title           = None, speciality   = None, 
                 cellphone       = None, address         = None, email        = None, 
                 webpage         = None, quote           = None, pseudo       = None, 
                 jobeltsnb       = None, trainingeltsnb  = None, trainings    = None):
        self.firstname      = firstname
        self.lastname       = lastname
        self.age            = age
        self.generaltitle   = generaltitle
        self.title          = title
        self.speciality     = speciality
        self.cellphone      = cellphone
        self.address        = address
        self.email          = email
        self.webpage        = webpage
        self.quote          = quote
        self.pseudo         = pseudo
        self.jobeltsnb      = jobeltsnb
        self.trainingeltsnb = trainingeltsnb
        self.hardSkills     = []
        self.softSkills     = []
        self.jobs           = []
        self.trainings      = []
        self.tool           = []
    
    def _get_kwargs(self):
        names = [
            'firstname',
            'lastname',
            'age',
            'generaltitle',
            'title',
            'speciality',
            'cellphone',
            'address',
            'email'
            'webpage',
            'quote',
            'pseudo',
            'jobeltsnb',
            'trainingeltsnb', 
            'hardSkills',
            'softSkills', 
            'jobs',
            'trainings',
            'tool'
        ]
        return [(name, getattr(self, name)) for name in names]
    
    ## implement it if bug need ! => print( [ <instance>] )
    # def __repr__(self) : 
    #     return "Test a:% s b:% s" % (self.a, self.b)  
    
    ## implement for str representation ! => print( [ <instance>] )
    def __str__(self) : 
        str = "Person ( % s , % s ) \n"  % (self.lastname, self.firstname)
        if (self.age != None) : 
            str += "\t % s years\n" % (self.age)
        str += "\t General Title: %s \n" % (self.generaltitle)
        str += "\t Title: %s \n" % (self.title)
        str += "\t Speciality: %s \n" % (self.speciality)
        str += "\t CellPhone: %s \n" % (self.cellphone)
        str += "\t Address: %s \n" % (self.address)
        str += "\t eMail: %s \n" % (self.email)
        str += "\t WebPage: %s \n" % (self.webpage)
        str += "\t Quote: %s \n" % (self.quote)
        str += "\t Pseudo: %s \n" % (self.pseudo)
        str += "\t jobeltsnb: %s \n" % (self.jobeltsnb)
        str += "\t trainingeltsnb: %s \n" % (self.trainingeltsnb)
        return str

