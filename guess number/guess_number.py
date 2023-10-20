import random

def tebak(x):
    random_number = random.randint(1,x)
    guess_number = 0
    guess_counter = 0
    while guess_number != random_number:
        while True:
            try:
                guess_number = int(input(f"Guess from the numbers 1 - {x}: "))
                break
            except:
                print("Enter only numbers!!")
        guess_counter += 1

        diff = 0
        if guess_number < random_number:
            diff = random_number - guess_number
            if diff < 4:
                print("Guess a little higher (↑)")
            elif diff < 11:
                print("Guess higher (↑↑)")
            else:
                print("Guess much higher (↑↑↑)")
        elif guess_number > random_number:
            diff = guess_number - random_number
            if diff < 4:
                print("Guess a little lower (↓)")
            elif diff < 11:
                print("Guess lower (↓↓)")
            else:
                print("Guess much lower (↓↓↓)")

    print(f"\nCongratulations, you have successfully guessed number {random_number}")
    print(f"You guess {guess_counter} times")

is_play = True
while is_play:
    tebak(100)
    main_lagi = input("Play again? (y/n): ")
    if main_lagi == "n":
        is_play = False
    print("\n")
