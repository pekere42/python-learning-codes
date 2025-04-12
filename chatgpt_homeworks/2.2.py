my_list_for_first_set = [3214,435,24124]
my_list_for_second_set = [2343,4324,24234,324]
my_first_set = set(my_list_for_first_set)
my_second_set = set(my_list_for_second_set)
print(my_first_set.union(my_second_set))
my_first_set.add(5325)
my_second_set.remove(2343)
print(my_first_set)
print(my_second_set)
