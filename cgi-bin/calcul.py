"""!/usr/bin/python
   -*- coding:utf-8 -*-"""

import cgi

form = cgi.FieldStorage()
first_number = float(str(form.getfirst('0')))
operator = str(form.getfirst('='))
second_number = float(str(form.getfirst('0')))
"""Using vocabulary perform operations on numbers"""
def operetion(z):  
    switcher = {
        '+': first_number + second_number,
        '-': first_number - second_number,
        '*': first_number * second_number,
        '/': first_number / second_number,
    }
    return switcher.get(z)

"""Prevent by division in zero"""
if operator == '/' and second_number == 0: 
    print('You can not divide by zero')

i = operetion(operator)
print('Your result is: {0:.2f}'.format(i))
print ("Content-Type: text/html\n")
print("<html><body>")
