import random
chancesleft=10
human_point=0
pc_point=0
while(chancesleft>0):
    pcinp= ["s", "w", "g"]
    pcchoice = random.choice(pcinp)
    human_inp = input("Enter s for snake, g for gun or w for water: ")
    if pcchoice==human_inp:
        print("Tie")
        print(f"Computer chose {pcchoice} and you chose {human_inp}")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")

    elif pcchoice=="s" and human_inp=="w":
        print("You lose computers snake drank your water")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")
        pc_point=pc_point+1
        
    elif pcchoice=="s" and human_inp=="g":
        print("You win you killed computers snake with gun")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")
        human_point=human_point+1
    
    elif pcchoice=="w" and human_inp=="s":
        print("You win snake drank computers water")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")
        human_point=human_point+1
    
    elif pcchoice=="w" and human_inp=="g":
        print("You lose your gun fell into computers water")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")
        human_point=human_point-1
    
    elif pcchoice=="g" and human_inp=="s":
        print("You lose your snake was killed by computers gun")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")
        human_point=human_point-1
    
    elif pcchoice=="g" and human_inp=="w":
        print("You win computers gun fell in your water")
        chancesleft=chancesleft-1
        print(f"You have {chancesleft} chances left")
        human_point=human_point+1
    
    else:
        print("Wrong input you may have capitalised the letter")
        continue
print("Game over")
if pc_point>human_point:
    print("Computer wins")
elif pc_point==human_point:
    print("Its tie")
else:
    print("You win")        
    
    
    
    