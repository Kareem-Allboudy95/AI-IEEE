import numpy as np

############################################################
# Problem 1

arr=np.array([[9, 0, 0],
              [0, 9, 0],
              [0, 0, 9]])

############################################################
# Problem 2

arr = np.arange(2, 33, 2)
arr = arr.reshape((4, 4))
mean = np.mean(arr) # mean
std = np.std(arr)  # standard deviation

# Select the elements within 1/2 standard deviations of the mean
mask = np.abs(arr - mean) < std/2
result = arr[mask]
print(result)

############################################################
# Problem 3

zeros_arr = np.zeros((9, 9), dtype=int)

############################################################
# Problem 4

arr = np.zeros((4,4))
values = np.arange(1,5)
# use broadcasting to assign values to each column of arr
arr[:, :] = values[:, np.newaxis]
print(arr)