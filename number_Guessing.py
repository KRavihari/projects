import random
import time

print("You can choose the top of range of numbers.")
top_of_range = input("Choose number :")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

start_time = time.time()

while True:
    guesses +=1 
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please print a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print ("You were below the number!")

end_time = time.time()

tot_time = round(end_time - start_time)

print ("Congratulations!! You got it in ", guesses, "guesses within ",tot_time,"seconds")
