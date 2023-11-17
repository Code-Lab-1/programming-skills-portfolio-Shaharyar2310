#Extra 1
#pythagorean theorem
import math
a=int(input("Enter first side(not the side opposite to right angle) : "))
b=int(input("Enter second side(not the side opposite to right angle) : "))
A=a**2
print("square of first side : ",A) 
B=b**2
print("square of second side : ",B)
c=A+B
print(c)
print(math.sqrt(c))