#ex 4 
def make_shirt(size,message):
    print("your size is",size, "and text on your shirt is" ,message)
A = "L"
B = "I love python"
C = "M"
make_shirt(A,B)
make_shirt(A,C)
Tsize = str(input("enter your size here : "))
msg = str(input("enter message here : "))
make_shirt(Tsize,msg)