import random
#randrange does not include 11. gets only till 10.
#r=random.randrange(-5,11)

#randint includes upper bound number.
#r=random.randint(-5,11)

top_of_range = input("please enter a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please enter a number greater than zero")
        quit()
else:
    print("please enter a number next time")
    quit()
random_number = random.randint(0,top_of_range)
guess_score = 0
while True:
    guess_score += 1
    user_input = input("please guess a number: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("please enter a number next time")
        continue
    if user_input > random_number:
        print("your were above the number")
    elif user_input < random_number:
        print("you were below the number")
    else:
        print("you got it correct!")
        break
print("You got it in", guess_score, "guesses")
