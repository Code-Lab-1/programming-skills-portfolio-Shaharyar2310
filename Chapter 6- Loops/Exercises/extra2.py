#extra 2
number = 0
n = int(input('\nEnter whole number to check : '))
i = 2
while i <= (n/2):
    if (n%i) == 0:
        flag = 1
        break
    i += 1
if n == 1:
    print('1 is neither prime nor composite')
elif number == 0:
    print(n,' is a prime number.')
elif number == 1:
    print(n,' is not a prime number.')