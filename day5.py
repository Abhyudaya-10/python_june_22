a=10
b=9
if(a==b):
    print("a is equal to b")
elif(a>=b):
    print("a is greater")
else:
    print("a is not equal to  b and b is greater")



# #nested if
# loan_age=20
# age=input("enter your age:")
# salary=input("enter you ")


# Ask the user to enter their age.
# - If age >= 18, print "Adult".
#     - If age > 60, also print "Senior Citizen".
# - If age < 18, print "Minor".


adult_age=18
seniorcitizens_age=60
age=int(input("enter your age:"))
if(age>=18):
    print("adult")
if(age>=60):
    print("senior citizen")
else:
    print("You are minor")

# Set a predefined username and password.
# Ask the user to enter username and password.
# - If username matches:
#     - Check if password matches.
#         - If yes, print "Login successful"
#         - Else, print "Incorrect password"
# - Else, print "Username not found"


username="Jenish"
password="swagktamoh"
Username=input("Enter the username")
Password=input("Enter the password")
if(Username==username):
    if(Password==password):
        if(True):
            print("Login Successful")
        else:
            print("Incorrect Password")
else:
    print("Username not found")




# Ask the user to enter 3 numbers.
# - If all are equal, print "All numbers are equal"
# - Else:
#     - Find and print the largest number


a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if(a==b==c):
    print("All numbers are equal")
elif(a>b and b>c):
    print("a is greatest")
elif(b>a and b>c):
    print("b is greatest")
else:
    print("c is greatest")


# Ask the user to enter the temperature in Celsius.
# - If temperature > 30:
#     - If temperature > 40: print "Extreme Heat!"
#     - Else: print "Hot"
# - Else if temperature >= 20:
#     - Print "Normal Weather"
# - Else:
#     - If temperature < 10: print "Very Cold"
#     - Else: print "Cold"

Normal_temp=20
temp=int(input("enter the temperature of your surrounding in celcius:"))
if(temp>30):
    if(temp>40):
        print("Extreme Hot")
    else:
        print("Hot")
elif(temp>=20):
    print("Normal Weather")
elif(temp<10):
    print("Cold")
    

# Ask the user to enter a number.
# - If the number is even:
#     - If it is between 10 and 50, print "Even number in range"
#     - Else, print "Even number but out of range"
# - Else, print "Odd number"


num=int(input("enter a number"))
if(num%2==0):
    if(num>=10 and num<=50):
        print("even number in range")
    else:
         print("even number but out of range")
else:
    print("odd number")


# Ask the user to enter a number.
# - If it's a positive number:
#     - If it's a multiple of 3 and 5, print "FizzBuzz"
#     - Else if multiple of 3, print "Fizz"
#     - Else if multiple of 5, print "Buzz"
#     - Else, print "Positive number"
# - Else if number is 0:
#     - Print "Zero"
# - Else:
#     - Print "Negative number"
