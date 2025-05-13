#function that takes input from user and divides 100 by that number
def error_detector():
    while True:
      input_number = input("please write a number to divide,or write quit to quit:").strip()#it clears the spaces
      if input_number == "":
        print("you do not write anything to divide")
        continue
      if input_number.lower()== "quit":
         break
      try:
         converted_number =int(input_number) 
         print(100/converted_number)
      except ZeroDivisionError:
         print("you can't divide by zero")
      except ValueError:
         print("you must write available number")
error_detector()  
    
         
         
      

    


