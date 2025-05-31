import numpy as np#importing numpy library

my_list_1 = [5,345,435,35345,53,23,4,34,45,13]
my_array_1 = np.array(my_list_1)#list is converted into array

print(np.min(my_array_1))
print(np.max(my_array_1))
print(np.max(my_array_1)-np.min(my_array_1))







my_list_2 = [23,34,45,56,67,78,89,90,4,5]
my_array_2 =np.array(my_list_2)


print(my_array_1 + my_array_2)
print(my_array_1 * my_array_2)