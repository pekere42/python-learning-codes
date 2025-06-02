print("Hello,Welcome to the game!!")

playing = input("Dou you want to play the game,please type yes or no :").lower()#taking user input for gstarting game
score = 0
if playing == "yes":
    user_name = input("what is your name? : ")
else:
    quit()

question_1 = input("Who is the most scoring player on nba? : ").lower()

if question_1 == "lebron james":
    print("king lıbroon says congrulations to you")
    score+=10#important question btw
else:
    print("how you do not know lebron bro,please die!!")

question_2 = input("who beat the france and became champion at 2022 world cup final? : ").lower()

if question_2 == "argentina":
    special_answer = input("you have a deep footbal knowladge,do you play halisaha frequently?,yes or no :").lower()
    if special_answer == "yes":
        print("i am giving you extra point for that!!" )
        score+=1
    score+=10#important question btw
else:
    print("bro everyone have to know this are you a lgbt fan?")
    score-=1

question_3 = input("in the turkey soccer league,what is the team that have more champıonships than other teams? : ").lower()

if question_3 == "galatasaray":
    special_answer_2 = input("what is your favourite player on gala? :")
    if special_answer_2 == "gabriel sara":
        score+=1
    score+=10
else:
    print("you are gay bro i am sure of that")
    score-=2

print(f"your total score is {score} {user_name},congrulations!!")




    








