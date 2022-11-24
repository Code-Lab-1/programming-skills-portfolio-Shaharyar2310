#extra 1
##Taking a number N as input and output the sum of all numbers from 1 to N (including N).
##and telling if it is even or odd 
N = int(input())
sum = 0
for i in range(0,N+1):
    sum += i
print(sum)
if sum%2==0:
  print("it is even")
elif sum%2!=0:
  print("it is odd")