import random
usr_score=0
comp_score=0
q=0
print("Welcome to the Game.\n")
options=["rock","paper","scissors"]
while True:
    user_input=input("Select Rock, Paper or Scissors|| or q to quit: ")
    user_input=user_input.lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    r=random.randint(0,2)
    comp_input=options[r]
    print("Computer's Choice is: ",comp_input)
    if user_input=="rock" and comp_input=="scissors":
        print("You won")
        usr_score+=1
    elif user_input=="paper" and comp_input=="rock":
        print("You won")
        usr_score+=1
    elif user_input=="scissors" and comp_input=="paper":
        print("You won")
        usr_score+=1
    elif user_input==comp_input:
        print("It's a Draw")
    else:
        print("You Lost")
        comp_score+=1
print("Final Score:")
print("Your Score: ",usr_score )
print("Computer's Score: ",comp_score )
print("Goodbye!")
exit()