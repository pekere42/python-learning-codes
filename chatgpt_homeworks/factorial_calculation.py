import numpy

num_list=[]

def factorial():
    given_number = input("please write a number:")
    num = int(given_number)
    num_list.append(given_number)
    while num > 1:
       num-=1
       num_list.append(num)
factorial()
print(num_list)
print(numpy.prod(num_list))

