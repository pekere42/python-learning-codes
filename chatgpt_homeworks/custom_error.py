class NegativeNumberError(Exception):
    def __init__(self,number):
        self.number = number
        super().__init__(f"Negative number entered: {number}")

        


def custom_error():
   while True:
       input_number = input("please write a number,or type quit to quit:").strip()
       if input_number == "":
           print("please write a number")
           continue
       if input_number == "quit":
           break
       try:
           converted_number = int(input_number)
           if converted_number > 0:
            print(f"this number is bigger than zero: {converted_number}")
           if converted_number == 0:
               print("this number is zero")
           if converted_number < 0:
               raise NegativeNumberError(converted_number)
       except NegativeNumberError as e:
           print(e)
           
           
custom_error()       
    