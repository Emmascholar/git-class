'''
A Python program to solve the 
quadratic function  ax2 + bx + c=0 using
formula
'''
a=int(input("enter the value of a "))
b= int(input("enter the value of b"))
c=int(input("enter the value of c"))

x1= (-b + ((b*b)-(4*a*c)) ** 0.5)/2 *a
x2= (-b + ((b*b)-(4*a*c)) ** 0.5)/2 *a


print("x1= ", x1)
print("x2= ", x2)
