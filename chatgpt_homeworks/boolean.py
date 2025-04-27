import random

positive_messages = [
    "Yükseklerde uçuyorsun! Bu sayı pozitif. 🚀",
    "Pozitif enerjiyle dolusun! ✨",
    "Bu sayı kesinlikle pozitif. Gibi sen de! 😎"
]

negative_messages = [
    "Bu sayı biraz moralsiz... Negatif çıktı. 😕",
    "Hmm... bu sayı moral bozucu. 🥶",
    "Negatifmiş ama dert etme, olur öyle şeyler. 🙃"
]

zero_messages = [
    "Ne eksik ne fazla, tam sıfır! 🎯",
    "Denge bu olsa gerek: 0 💫",
    "Bu sayı tam ortada durmuş: Sıfır! 🧘"
]

invalid_input_messages = [
    "Hmm, bu bir sayı değil. Sayılarla konuşalım! 🔢",
    "Lütfen rakam kullan, sihirli harflerle olmuyor. 🧙",
    "Sayısal lütfen! 🤖"
]

empty_input_messages = [
    "Hiçbir şey yazmadın 😐",
    "Bir şeyler yazman lazım... 🤫",
    "Boş girdiyle nereye kadar? 🙈"
]







def bool_definer():
    
    while True:
        input_data = input("please write your number(or write 'quit' to exit):")#user write the number
        if input_data == "":
           print(random.choice(empty_input_messages))
           continue
    
        if input_data.lower() == "quit":
          break



        try:
            number = float(input_data)
            if number > 0:
             print(random.choice(positive_messages))
            elif number < 0:
             print(random.choice(negative_messages))
            else:
              print(random.choice(zero_messages))
        except ValueError:
          
          print(random.choice(invalid_input_messages))


print("welcome,this program tells if your number is positive,negative or zero")   
bool_definer()
