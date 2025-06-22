# import random

# a =random.randint(10,50)
# print(a)
# total_attempt = 5

# while(True):

#     user_input = int(input("enter a number: "))

#     if a==user_input:
#         print("You win")
#         user_play = input("Do you want to play again: ").upper()

#         if user_play == ("Y" or "YES"):
#             a = random.randint(10,50)

#             print(a)
#         else:
#             break
#     else:
#         print("Number doesnot match, please try again.. Remaining attempt", user_attempt)


#     if user_attempt == total_attempt:
#         print("Total attempt exceeded", "Random number is", a)
#         break


# user correct => 5 points
# computer => 3 points
# user wrong  -1
# user correct computer value should be -1


# 10 point

import random

a = random.randint(10, 50)
print(a)
user_point = 0
computer_point = 0
while True:
    user_input = int(input("enter a number:"))
    if a == user_input:
        print("You win")
        if a == user_input:
            user_point += 5
            computer_point -= 1
            user_play = input("Do you want to play again")

            
        if user_point >= 10:
            print(" You Win! Your score:", user_point)
            break
                                        
        else:
            print("your score:", user_point)

            break
    else:
        print("Number doesn't match")
        computer_point += 3
        user_point -= 1
    if computer_point >= 10:
        print(" You Lose", computer_point)
    elif user_point >= 10:
        print(" Yow Win", user_point)
