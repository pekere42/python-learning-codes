def detect_data_type(user_input):
    try:
        int(user_input)
        print(f"{user input} is an Integer")
    except ValueError:
        try:
            float(user_input)
            print(f"{user_input} is a float")
        except ValueError:
            if user_input.lower() == "true" or user_input.lower() =="false":
                print(f"{user_input} is a Boolean")
            else:
                print(f"{user_input} is a String")


while True:
    user_input = input("please enter your data: or enter quit")
    if data=="quit":
        break
    else:
        detect_data_type(user_input)


