import numpy as np

my_array = np.arange(0, 21)
my_new_array = my_array ** 3
my_newer_array = my_new_array > 10
print(my_newer_array)
my_new_array[my_newer_array] = 0
print(my_new_array)
print(np.sum(my_new_array))
print(np.max(my_new_array))
