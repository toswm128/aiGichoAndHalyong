import numpy as np


arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
np_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1:3])
# print(np_arr[1, 1])


sub_arr = arr[0:][1:3]
# print(sub_arr)

sub_np_arr = np_arr[1:, 1:3]
print(sub_np_arr)
