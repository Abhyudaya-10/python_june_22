import random

a = random.randint(1, 51)

user_score = 0
computer_score = 0
final_score = 10
print(a)
while (True):
    user_input = int(input("enter a number:"))
    if a == user_input:
        print("You Win")
        user_score += 5
        computer_score -= 1
        print("Your score:", user_score)
        
        user_play = input("DO YOU WANT TO PLAY AGAIN:(Y/N)")
        if user_play == "Y":
            a = random.randint(1, 51)
            print(a)
        else:
            print("Your score:", user_score, ",", "Computer score:", computer_score)
            break
    else:
        print("You Lose:")
        computer_score += 3
        user_score -= 1
        print("Your score:", user_score, ",", "Computer score:", computer_score)
        if computer_score >= final_score:
            print("Computer Win:", computer_score)
        elif user_score >= final_score:
            print("User Score:", user_score)
    break
