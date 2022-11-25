#extra 3
##Taking a number N as input and output the sum of all numbers from 1 to N (including N).
##and telling if it is even or odd 
N = int(input("Length of program : "))
sum = 0
for i in range(0,N+1):
    sum += i
print("Sum of all the numbers : ",sum)
if sum%2==0:
  print("it is even")
elif sum%2!=0:
  print("it is odd")