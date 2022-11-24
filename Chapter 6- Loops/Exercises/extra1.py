#extra 1
numbers=[]
n = int(input("enter numbers : "))
for i in range(0,n):
  n = int(input("Enter number : "))
  numbers.append(n)
sum = 0
for i in numbers :
    sum =sum + i
print(sum)