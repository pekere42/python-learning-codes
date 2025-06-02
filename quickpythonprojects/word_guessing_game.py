import random#importing random library

name = input("What is your name?:")
chance = 12
words = ["lebron","jordan","edwards","towns","tyrese","turner","alexander","durant","curry","green","sengun","fred"]
total_guess =  12
word = random.choice(words)#picking random word
guesses= "" #guesses are letter, string shold be more logical than list
    

print(f"Welcome to the game {name},you have 12 chance to guess!")

while total_guess > 0:#keep asking until the guess chance are bigger than 0
    remaining = 0#at every round we asked our guesses string to ask letter,if string involves every letter remaining would be 0 and the game is over ,very clever!!
    for i in word:#asking for all word member
        if i in guesses:#we asked our list every round because of this we create it out of while loop because we want it alive every loop
            print(i)
        else:
            print("-")
            remaining += 1#for example word enes and we added our string e and n this called one and subsequent round we say s string involve every letter and remaining stay at 0 and game will over
    if remaining == 0:
        print("You Win")
        print("The Word is: " ,word)
        break
    guess = input("guess a character:")
    guesses += guess#adding guess every loop
    if guess not in word:
        total_guess -= 1#in case of wrong guess chance is decreasing one by one
        print("you wrong")
        print("you have" ,total_guess,"chance")#recalling total chance
    if total_guess == 0:#if chance = 0 this means game is overrt5
        print("you loose")
    
    
    
    




