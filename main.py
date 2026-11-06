import numpy as np

values = np.array([-10, 50, 65, 80, 95, 110])

<<<<<<< HEAD
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
np_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
is_even = arr % 2 == 0
print(is_even)
=======
selected = values[(values >= 60) & (values <= 90)]
print(selected)

values[values < 0] = 0
print(values)

result = np.where(values >= 60, "합격", "불합격")
print(result)
>>>>>>> 176cb8ffbadcdf5e569113024b692ef3750cd7d1
