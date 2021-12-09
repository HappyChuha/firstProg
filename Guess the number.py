number=24
guesses=int(9)
lololl='nope'
while(guesses>0):
    inp=int(input("Enter a number:"))
    if inp<number:
        print("Your number is less than the number")
        guesses=guesses-int(1)
        print("No. of guesses left=", guesses)
        continue
    if inp>number:
        print("Your number is bigger than the number")
        guesses = guesses - int(1)
        print("No. of guesses left=", guesses)
        continue
    if inp==number:
        lololl='yup'
        print("You win")
        break

if lololl=='nope':
    print("You lost")

