#extra 3
print("Enter word here : ")
word = input()
vowel_a = ['a', 'A']
vowel_e = ['e', 'E']
vowel_i = ['i', 'I']
vowel_o = ['o', 'O']
vowel_u = ['u', 'U']
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for x in word:
    if x in vowel_a:
        count_a = count_a+1
    elif x in vowel_e:
        count_e = count_e+1
    elif x in vowel_i:
        count_i = count_i+1
    elif x in vowel_o:
        count_o = count_o+1
    elif x in vowel_u:
        count_u = count_u+1
print("\n'a' occurs ", count_a)
print("'e' occurs ", count_e)
print("'i' occurs ", count_i)
print("'o' occurs ", count_o)
print("'u' occurs ", count_u)