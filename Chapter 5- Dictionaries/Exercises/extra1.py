#extra 1
#basics
person_I_know={"first_name":"Ali","last_name":"zafar","age":"21","city":"Dubai"} 
print(person_I_know)
#all the keys
print(person_I_know.keys())
#change multiple things
print(person_I_know)
person_I_know.update({"age":"40","name":"Saif","location":"Pakistan"})
print(person_I_know)
#add something new
person_I_know["height"]= "183 cm"
print(person_I_know)
#reomve something
person_I_know.pop("height")
print(person_I_know)
#remove last item
person_I_know.popitem()
print(person_I_know)