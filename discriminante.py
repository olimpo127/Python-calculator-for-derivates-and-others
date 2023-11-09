import sympy as sp 

x = sp.Symbol('x') 

#change the function here
y = x**3
#----------------------------------------------

#this will return the first derivative of the function
first_derivate = sp.diff(y,x)
second_derivate = sp.diff(first_derivate,x)
third_derivate = sp.diff(second_derivate,x)

print("the first derivative is:", first_derivate)
print("the second derivative is:", second_derivate)
print("the third derivative is:", third_derivate)
