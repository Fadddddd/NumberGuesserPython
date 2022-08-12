import random

computer_guess = random.randint(0, 100)


attempts_count = 0

print("Hi there, could you guess the number between 0 and 100? ")
user_answer = input("Wanna actually play? (yes/no) ")
while True:
    if user_answer == "yes":
        user_guess = int(input("Your suggestion: "))
        attempts_count += 1
        if user_guess == computer_guess:
            print("Congrats!")
            print("You found after", attempts_count, "attempts")
            break
        elif user_guess > computer_guess:
            print("too big")
        elif user_guess < computer_guess:
            print("too small")

    else:
        print("ok, bye")
        break
