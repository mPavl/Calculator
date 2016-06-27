first_number_input = input("Welcome to the calculator. Input your first number:")
operator_input = input("Input operator:")
second_number_input = input("Input your second number:")

def admission(argument1, argument2):
    if argument1.isdigit() and argument2.isdigit():
        argument1 = float(argument1)
        argument2 = float(argument2)
        """Prevent by division in zero"""
        if operator_input == '/' and argument2 == 0:
            print('You can not divide by zero')
        else:
            def calculation(switcher):
                operetion_of_numbers =(argument1 + argument2, argument1 - argument2, argument1 * argument2, argument1 / argument2)
                operator = ('+', '-', '*', '/')            
                """Using vocabulary perform operations on numbers"""
                switcher = dict(zip(operator, operetion_of_numbers))
                def out(symbol):
                    result = switcher.get(symbol)
                    print('Your result is: {0:.2f}'.format(result))
                    return result 
                return out
            return calculation
    else:
        print('Your first number and second number must be numbers!')
 
@admission(first_number_input, second_number_input)
def check(argument):
    return argument
    
check(operator_input)


