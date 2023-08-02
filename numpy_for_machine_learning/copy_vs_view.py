import numpy as np

np1 = np.array([0,1,2,3,4,5])

# CREATE A VIEW
np2 = np1.view()

print(f'original np1: {np1}')
print(f'original np2: {np2}')
# [0  1  2  3  4  5]

np1[0] = 41
print(f'changed np1: {np1}')
print(f'original np2: {np2}')
# [41  1  2  3  4  5]
# => the np2 is changed too!

# CREATE A COPY
np3 = np1.copy()

np1[0] = 999
print(f'changed np1 {np1}')
print(f'original np3 {np3}')
# np1 is [999  1  2  3  4  5]
# np3 is [41  1  2  3  4  5]

# a copy is not connected to the original array
# a view is connected to the original