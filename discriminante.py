import sympy as sp 

x = sp.Symbol('x') 
y = sp.Symbol('y')


#change the function here-------------------------------------------------------------------------------------
f = x**3 + y**3 - 3 * x**2 - 3 * y**2 - 9*x
#-------------------------------------------------------------------------------------------------------------


first_derivate_x = sp.diff(f,x)
first_derivate_y = sp.diff(f,y)
second_derivate_xx = sp.diff(first_derivate_x,x)
second_derivate_xy = sp.diff(first_derivate_x,y)
second_derivate_yx = sp.diff(first_derivate_y,x)
second_derivate_yy = sp.diff(first_derivate_y,y)
third_derivate_xxx = sp.diff(second_derivate_xx,x)
third_derivate_xxy = sp.diff(second_derivate_xx,y)
third_derivate_xyx = sp.diff(second_derivate_xy,x)
third_derivate_xyy = sp.diff(second_derivate_xy,y)
third_derivate_yxx = sp.diff(second_derivate_yx,x)
third_derivate_yxy = sp.diff(second_derivate_yx,y)
third_derivate_yyx = sp.diff(second_derivate_yy,x)
third_derivate_yyy = sp.diff(second_derivate_yy,y)

def critical_points(derivate):
    return sp.solve(derivate)

print("the first derivative with respect to x is:", first_derivate_x)
print("the first derivative with respect to y is:", first_derivate_y)
print("the second derivative with respect to xx is:", second_derivate_xx)
print("the second derivative with respect to xy is:", second_derivate_xy)
print("the second derivative with respect to yx is:", second_derivate_yx)
print("the second derivative with respect to yy is:", second_derivate_yy)
print("the third derivative with respect to xxx is:", third_derivate_xxx)
print("the third derivative with respect to xxy is:", third_derivate_xxy)
print("the third derivative with respect to xyx is:", third_derivate_xyx)
print("the third derivative with respect to xyy is:", third_derivate_xyy)
print("the third derivative with respect to yxx is:", third_derivate_yxx)
print("the third derivative with respect to yxy is:", third_derivate_yxy)
print("the third derivative with respect to yyy is:", third_derivate_yyy)
print("the third derivative with respect to yyy is:", third_derivate_yyy)

critical_points_x = critical_points(first_derivate_x)
critical_points_y = critical_points(first_derivate_y)

print("the critical points for the first derivative with respect to x are:", critical_points_x)
print("the critical points for the first derivative with respect to y are:", critical_points_y)

def discriminante():
    return (second_derivate_xx * second_derivate_yy) - (second_derivate_xy * second_derivate_yx)

formula_discriminante = discriminante()
print("the discriminante formula is:", formula_discriminante)

#-------------------------------------------------------------------------------------------------------------------
def calculate_discriminante(x, y):
    #replace this formula according to the formula_discriminante
    return (6*x - 6) * (6*y - 6)
#these inputs should be fixed in every exercise according to the function.
discriminante1 = calculate_discriminante(-1,0)
discriminante2 = calculate_discriminante(-1,2)
discriminante3 = calculate_discriminante(3,0)
discriminante4 = calculate_discriminante(3,2)
#-------------------------------------------------------------------------------------------------------------------
print("Discriminante 1 is:", discriminante1)
print("Discriminante 2 is:",discriminante2)
print("Discriminante 3 is:",discriminante3)
print("Discriminante 4 is:",discriminante4)

    
