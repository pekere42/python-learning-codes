import random 
my_list = list(range(2,100))
print("welcome to the challange!!")
def guessing():
    choosen_number = random.choice(my_list)
    while True:
        guessed_number = input("lütfen 1 ile 100 arasında bir numara giriniz:")
        if guessed_number.lower == "quit":
            break
        if float(guessed_number) == choosen_number:
            print("doğru tahmin,çok iyi iş çıkardın,sistemden çıkmak için 'quit' yazabilirsin!")
        elif float(guessed_number) > choosen_number:
            print("sanırım biraz fazla söyledin,düşürmeye ne dersin!")
        elif float(guessed_number) < choosen_number:
            print("hadi dostum,biraz arttır,yapabilirsin")

            

guessing()

#ı have a problem ın random and mistake fixing part mistake solutions and random number method must be fixed
