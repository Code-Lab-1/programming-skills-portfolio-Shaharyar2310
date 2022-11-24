#extra 4
#adding two lists (manual lists)
list1=[]
n = int(input("length of list 1 : "))
for i in range(0,n):
  thing = input()
  list1.append(thing)
print("list 1 is",list1)  


list2=[]
n = int(input("length of list 2 : "))
for i in range(0,n):
  thing1 = input()
  list2.append(thing1)
print("list 2 is",list2)



list3 = list1 + list2
print("list 3 is",list3)