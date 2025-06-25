import random

print("here are the rules of the game:\n"
      "Rock vs Scissors => Rock Wins\n"
      "Rock vs Paper => Paper Wins\n"
      "Paper vs Scissors => Scissors Wins")

while True:
    user_choice_1 = input("please enter your choice; 1 for rock,2 for scissors,3 for paper:")
    
    if user_choice_1 == "":
        print("you did not write anything")
        continue
    user_choice = int(user_choice_1)
    
    if user_choice < 1 or user_choice> 3:
        print("please enter valid number")
        continue

    if user_choice == 1:
        user_choice_name = "rock"
    elif user_choice == 2:
        user_choice_name = "scissors"
    elif user_choice == 3:
        user_choice_name = "paper"

    print(f"user choice is {user_choice_name}")
    print("now it is computer's turn")
    
    

    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "rock"
    elif comp_choice == 2:
        comp_choice_name = "scissors"
    elif comp_choice == 3:
        comp_choice_name = "paper"

    print(f"computer choose {comp_choice_name}")
    print(user_choice_name,"vs",comp_choice_name)

    if user_choice == comp_choice:
        result = "draw"
    elif user_choice == 1 and comp_choice == 2 or comp_choice == 1 and user_choice ==2:
        result = "rock"
    elif user_choice == 2 and comp_choice == 3 or comp_choice == 2 and user_choice ==3:
        result = "scissors"
    elif user_choice == 3 and comp_choice == 1 or comp_choice == 3 and user_choice ==1:
        result = "paper"

   
    

    if result == "draw":
        print("you picked the same object as comp!!!")
    elif user_choice_name == result:
        print("You won the game")
    else:
        print("Computer wins")
    ans = input("Do you want to play the game again?Y OR N:")
    if ans.lower() == "y":
        continue
    elif ans.lower() == "n":
        print("Thanks for playing")
        break
    else:
        print("you write invalid number")
        break


        
        
        