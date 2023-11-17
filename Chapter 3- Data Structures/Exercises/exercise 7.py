##exercise No. 7
places = ["Machu Picchu", "Peru","The Grand Canyon","Colosseum,Amalfi","Angkor Wat","Pyramids of Giza"]
print("original :" ,places)
A = sorted(places)#sorted acending aplhabatical order
print(A)
print("original :" ,places)
B = sorted(A, reverse=True)#sorted decending alphabatical order
print(B)
C = sorted(B, reverse=False)#sorted decending alphabatical reverse order
print(C)
print("original :" ,places)
places.sort(reverse=False)#acending alphabitical order
print(places)
places.sort(reverse=True)#decending aplhabatical order
print(places)