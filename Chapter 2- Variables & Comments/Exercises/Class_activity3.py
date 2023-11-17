#Question no. 3
Money_I_have = int(input("Enter monny here : "))
print("Money I have = ", Money_I_have)
Return_each_year = 0.1 #only the number divided by 100 not the sign
print("Return after each year = 10%")

after_one_year = Money_I_have * Return_each_year
print("Investment after one year = ", after_one_year)
total_money_after_one_year = Money_I_have + after_one_year
print("Totalmoney aftre one year = ", total_money_after_one_year)

return_after_two_years = Return_each_year * 2
print("Money return after 2 years = ", return_after_two_years)
after_2_years = Money_I_have * return_after_two_years
print("Investment after 2 years", after_2_years)
total_money_after_2_year = Money_I_have + after_2_years
print("Total money aftre two year = ", total_money_after_2_year)

return_after_7_years = Return_each_year * 7
print("Money return after 7 years = ", return_after_7_years)
after_7_years = Money_I_have * return_after_7_years
print("Investment after 7 years = ", after_7_years)
total_money_after_7_years = Money_I_have + after_7_years
print("Total money after 7 years = ", total_money_after_7_years)
