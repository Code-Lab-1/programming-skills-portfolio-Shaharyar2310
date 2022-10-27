##exercise No. 6
Invitation = ["Ali","Ahmed","David","Saif"]
print(Invitation)
print("You can invite only two people for dinner")
print("Dear", Invitation[0], "sadly I am sorry I can not invite you")
Invitation.pop(0)
print("Dear", Invitation[1], "sadly I am sorry I can not invite you")
Invitation.pop(1)
print("Dear", Invitation[0],"are still invited to the party")
print("Dear", Invitation[1],"are still invited to the party")
del Invitation[0]
del Invitation[0]
print(Invitation)