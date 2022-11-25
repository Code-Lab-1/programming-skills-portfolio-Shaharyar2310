#exercise 3
Glossary={"Indentation":"Indentation refers to the spaces at the beginning of a code line.",
"Comments":"Comments are code lines that will not be executed.",
"Int":"The integer or whole number number type.",
"Float":"The floating or number with decimal number type.",
"string":"Strings are an array of characters.",
"Dictionary":"A dictionary is an unordered, and changeable, collection.",
"Lists":"A list is an ordered, and changeable, collection.",
"Variable":"Is a way of storing values into the memory of the computer by using specific names that you define.",
"Index number":"Index number is the location of specific value stored in Python lists or tuples. The first index value of list is always 0.",
"Script":"Script s a dedicated document for writing Python code that you can execute. Python script files should always have the .py file extension."}
print(Glossary)
for i in Glossary:
  print("\n")
  print(i,":")
  print("\t",Glossary[i])