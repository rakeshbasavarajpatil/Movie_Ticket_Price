#The program asks user to input their age and prints out the amount that they need to pay.
#This can be extended for multiple users

print("Please enter your age")
age = int(input())
#Categories(infant,child,adult,senior)
#infant (Age<2)
if (age < 2):
	print("The movie ticket is free for infants")
elif (age >=2 and age <=8):
	print("The movie ticket price for child is $2")
elif (age >= 65):
	print("The movie ticket price for seniors is $5")
else:
	print("The movie ticket price for adults is $10")