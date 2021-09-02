#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Use Faker Library
## cf. https://pypi.org/project/Faker/

from faker import Faker

## fake1 = Faker()
## print( fake1.name() )
## print( fake1.address() )
## ## fake.text()
## print( "" )

fake2 = Faker( "fr_FR" )
## print( fake2.name() )
print( fake2.address() )
print( fake2.license_plate() )
print( fake2.ssn() )
print( "" )

## https://www.regular-expressions.info/creditcard.html
## see also https://faker.readthedocs.io/en/master/providers/faker.providers.credit_card.html
## 'amex', 'diners', 'discover', 'jcb', 'jcb15', 'jcb16', 'maestro', 'mastercard', 'visa', 'visa13', 'visa16', 'visa19'

## print( fake2.credit_card_full() )
print( fake2.credit_card_full( 'visa16' ) )
## print( fake2.credit_card_full( 'mastercard' ) )
print( "*****" )

for i in range(1, 100):
  print( fake2.credit_card_full( 'visa16' ) )
