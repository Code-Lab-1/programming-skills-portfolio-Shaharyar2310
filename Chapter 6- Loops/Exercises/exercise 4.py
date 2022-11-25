#exercis 4
finihed_sandwich_orders=[]
sandwich_orders=["Chicken Sandwich.","Egg Sandwich.","Seafood Sandwich.",
"Roast Beef Sandwich.","Grilled Cheese.","Nutella Sandwich.",
"Grilled Chicken Sandwich.","pastrami sandwich."]
print(sandwich_orders)
while True:
  if sandwich_orders == []:
    break
  else:
    print("I made your", sandwich_orders[0])
    finihed_sandwich_orders.insert(0,sandwich_orders[0])
    sandwich_orders.pop(0)

print("left orders : ",sandwich_orders)
print("finished orders : ",finihed_sandwich_orders)