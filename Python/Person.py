#!/usr/bin/python3
# -*- coding: utf-8 -*- 

class Person( object ) : 
    def __init__(self,
                 firstname       = None, lastname        = None, extrainfo    = None, 
                 generaltitle    = None, title           = None, speciality   = None, 
                 cellphone       = None, address         = None, email        = None, 
                 webpage         = None, quote           = None, pseudo       = None, 
                 jobeltsnb       = None, trainingeltsnb  = None, skilleltnb   = None, 
                 skills          = [], jobs              = [], trainings      = []):
        self.firstname      = firstname
        self.lastname       = lastname
        self.generaltitle   = generaltitle
        self.title          = title
        self.speciality     = speciality
        self.cellphone      = cellphone
        self.address        = address
        self.email          = email
        self.webpage        = webpage
        self.quote          = quote
        self.extrainfo      = extrainfo
        self.pseudo         = pseudo
        self.skilleltnb     = skilleltnb
        self.jobeltsnb      = jobeltsnb
        self.trainingeltsnb = trainingeltsnb
        self.hardSkills     = []
        self.softSkills     = []
        self.skills         = skills
        self.jobs           = jobs
        self.trainings      = trainings
        self.tool           = []
    
    ## implement it if bug need ! => print( [ <instance>] )
    # def __repr__(self) : 
    #     return "Test a:% s b:% s" % (self.a, self.b)  
    
    ## implement for str representation ! => print( [ <instance>] )
    def __str__(self) : 
        str = "Person ( % s , % s ) \n"  % (self.lastname, self.firstname)
        str += "\t General Title: %s \n" % (self.generaltitle)
        str += "\t Title: %s \n" % (self.title)
        str += "\t Speciality: %s \n" % (self.speciality)
        str += "\t CellPhone: %s \n" % (self.cellphone)
        str += "\t Address: %s \n" % (self.address)
        str += "\t eMail: %s \n" % (self.email)
        str += "\t WebPage: %s \n" % (self.webpage)
        str += "\t Quote: %s \n" % (self.quote)
        str += "\t Extra Info: %s \n" % (self.extrainfo)
        str += "\t Pseudo: %s \n" % (self.pseudo)
        str += "\t skilleltnb: %s \n" % (self.skilleltnb)
        str += "\t jobeltsnb: %s \n" % (self.jobeltsnb)
        str += "\t trainingeltsnb: %s \n" % (self.trainingeltsnb)
        str += "\t skills: %d \n" % ( len( self.skills ) )
        for elt in self.skills : 
            str += "\t\t %s \n" % ( elt )
        str += "\t jobs: %s \n" % ( len( self.jobs ) )
        for elt in self.jobs : 
            str += "\t\t %s \n" % ( elt )
        str += "\t trainings: %s \n" % ( len( self.trainings ) )
        for elt in self.trainings : 
            str += "\t\t %s \n" % ( elt )
        return str
    
    def export( self ) : 
        str = self.lastname + "\t" + self.firstname + "\t"
        str += "generated" + "\t"
        str += self.address + "\t" + self.pseudo + "\t"
        str += self.webpage + "\t" + self.email + "\t"
        str += self.quote + "\t"
        str += ";".join( map("::".join, self.skills) ) + "\t"
        str += ";".join( map("::".join, self.jobs) ) + "\t"
        str += ";".join( map("::".join, self.trainings) ) + "\t"
        str += self.generaltitle + "\t"
        str += self.title + "\t"
        str += self.speciality + "\t"
        str += self.cellphone + "\t"
        return str


