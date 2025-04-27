def fibonacci():
    fib_number = int(input("please write a number for fibonacci list:"))
    fib_list = [0,1]  
    for i in range(2,fib_number):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list)

fibonacci()

