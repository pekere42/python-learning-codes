import random
def hangman_game():
    user_name = input("welcome to the hangman game!!,please tell your name: ")
    print()
    print("HINT:word can associated with footbal or clash royale")

    for i in range(3):
        print()
    word_list =["chelsea", "barcelona", "galatasaray", "juventus", "ajax","pekka", "valkyrie", "goblin", "wizard", "mega"]
    word = random.choice(word_list)
    total_chance = len(word) + 2
    guesses = ""
    while total_chance > 0:
        not_same_letter = 0
        
        for char in word:
            if char in guesses:
                print(char,end=" ")
            else:
                not_same_letter+=1
                print("-",end=" ")
        if not_same_letter == 0:
         print(f"Congrulations,you won the game {user_name}")
         game_check = input(f"do you want to play again {user_name} type yes or no: ").lower()
         if game_check == "yes":
              hangman_game()
         else:
              break
        for i in range(3):
          print()
        guess = input(f"Enter a letter to guess {user_name}: ").lower()
        guesses += guess
        if len(guess) == 1:
         if guess not in word:
             total_chance-=1
             
             print(f"you wrong,you have {total_chance} to guess {user_name}")
         if total_chance == 0:  
             game_check_2 = input(f"you loose the game,do you want to play again? yes or no: ").lower()
             if game_check_2 == "yes":
                 hangman_game()
        else:
            break
hangman_game()