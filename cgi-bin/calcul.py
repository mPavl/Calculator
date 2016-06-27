"""!/usr/bin/python
   -*- coding:utf-8 -*-"""
import cgi
form = cgi.FieldStorage()
first_number = form.getfirst("first_number")
operator_input = form.getfirst('?')
second_number = form.getfirst("second_number")
       
if first_number.isdigit() and second_number.isdigit():
    first_number = float(first_number)
    second_number = float(second_number)
    """Prevent by division in zero"""
    if operator_input == '/' and second_number == 0: 
        print('You can not divide by zero')
    else:
        """Using vocabulary perform operations on numbers"""
        operator = ('+', '-', '*', '/')
        operetion_of_numbers =(first_number + second_number, first_number - second_number, first_number * second_number, first_number / second_number)
        def operetion(operator_input):  
            switcher = dict(zip(operator, operetion_of_numbers))
            result = switcher.get(operator_input)
            return result
        print("Content-Type: text/html\n", 'Your result is: {0:.2f}'.format(operetion(operator_input)))
else:
    print('<h1>ERROR</h1>')



