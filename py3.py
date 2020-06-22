#guess the number in 7 guesses
n = 18
guess = 1
print("no. of guesses u have is 7")
while(guess < 7):

    w = int(input("enter the no.   :  "))
    if w < 18:
        print("enter the greater value\n")

    elif w > 18:
        print("enter smaller value\n")
    else:
        print("correct\n ")
        break
    print("no. of guesses", guess)
    guess = guess + 1
if guess > 7:
    print("game over")