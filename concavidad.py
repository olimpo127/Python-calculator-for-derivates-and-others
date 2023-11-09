def calculate(c, x1, x2):

    x = (c * x1) + ((1 - c) * x2)
    
    #this function should be fixed in every exercise according to the function.
    fx1 = (12 - (x1- 2)**2)
    fx2 = (12 - (x2 - 2)**2)
    number1 = (12 - (x - 2) ** 2)
    #

    number2 = (c*fx1) + ((1-c)*fx2)

    if number1 > number2:
        return "Concavo"
    else:
        return "Convexo"

print(calculate(0.5, 0, 3)) #these inputs should be fixed in every exercise according to the function.

