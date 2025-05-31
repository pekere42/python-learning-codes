import numpy as np
list_1 = [[1,2,3],[2,3,4],[3,4,5]]#creating a list for arrays
list_2 = [[4,3,7],[4,7,6],[5,4,7]]#creating a list for arrays
arr_1 = np.array(list_1)#converting into a numpy array
arr_2 = np.array(list_2)#converting into a numpy array

print(np.add(arr_1,arr_2))#adding two arrays
print(np.subtract(arr_1,arr_2))#substracting two arrays
print(np.dot(arr_1,arr_2))#for special matrix multiplication
#gpt says for dot method shape is very crucial and check every time with arr.shape
print(np.dot(arr_1, arr_2.T))  # changes the result structure
