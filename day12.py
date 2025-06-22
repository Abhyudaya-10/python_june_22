# a=1
# num=54
# while(a<=10):
#     print(f'{num} x {a}={num*a}')
#     a=a+1
#     print(a)



data=[10,50,3]
length=len(data)
print(length)
index=0
while(index<length):
    i=1
    while(i<=10):
        print(f"data[index] x i={data[index]*i}")
        i+=1
        print("/n")
        index+=1




        #random library
        import random
        a =random.randint(10,50)
print(a)

while(True):
    user_input = int(input("enter a number: "))
    if a==user_input:
        print("You win")
        user_play = input("Do you want to play again: ")

        if user_play == "Y":
            a = random.randint(10,50)
            print(a)
        else:
            break
    else:
        print("Number doesnot match, please try again")