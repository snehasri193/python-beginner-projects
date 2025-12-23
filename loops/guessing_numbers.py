secret = 5
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

print("You guessed it!")
