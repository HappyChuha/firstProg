number=24
guesses=10
while(guesses>0):
    inp=int(input("Enter a number:"))
    if inp<number:
        print("Your number is less than the number")
        guesses=guesses-1
        print("No. of guesses left=", guesses)
        continue
    if inp>number:
        print("Your number is bigger than the number")
        guesses = guesses - 1
        print("No. of guesses left=", guesses)
        continue
    if inp==number:
        print("You win")
        break
if guesses==0:
    print("You lost")

