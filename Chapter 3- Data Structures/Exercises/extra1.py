#extra 1
#list basics
#list start(strings)
names = ["Ali","Ahmed","Saif","Qasim"]
print(names)
#adding (strings)
names.insert(2,"alien")
names.insert(2,"alien")
print(names)
#removing (strings)
#two ways
#No. 1
names.remove("alien")
print(names)
#No. 2
names.pop(2)
print(names)
#checking length
print("length of list is ",len(names))