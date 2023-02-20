#from mathematics import add


#x = mathematics.add(23,45)
#y = mathematics.subtract(89,34)

#print(x)

#import module  
import operators
import others
import trigs


#get numbers
operator = input("enter operator")
if operator =="cube":
    number = eval(input("enter number"))
    x = others.cube(number)
    print(x)
elif operator == "sin":
    angle = eval(input("enter angle in degrees:"))
    sin_of_angle = trigs.get_sine(angle)
    print(sin_of_angle)
elif operator =="tan":
    angle = eval(input("enter angle in degrees"))
    tan_of_angle = trigs_get_tan(angle)
    print(tan_of_angle)  
else:   
    num1 = eval(input("Enter number 1:"))
    num2 = eval(input("enter number 2:"))
    if operator =="/":
        x = operators.divide(num1,num2)
        print(x)  
    elif operator =="-":
        x = operators.subtract(num1,num2)
        print(x)
    elif operator =="*":
        x = operators.multiply(num1,num2)
        print(x)

#build a better calculator
#x = others.cube(9)
#y = operators.add(7,8)

#print(y)
#print(x)
