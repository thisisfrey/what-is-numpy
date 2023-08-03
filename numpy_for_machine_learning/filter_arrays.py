import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

x = [True, True, False, False, False, False, False, False, False, False]

np2 = np1[x]
# np2 is [1 2]

# Filter even
filtered1 = []
for el in np1:
    if el % 2 == 0:
        filtered1.append(True)
    else:
        filtered1.append(False)

"""
filtered1 is
[False, True, False, True, False, True, False, True, False, True]
"""
np3 = np1[filtered1]


# Shortcut!!!
filtered2 = np1 % 2 == 0
# [False,  True, False,  True, False,  True, False,  True, False,
#         True]

np4 = np1[np1 % 2 == 0]
# np4 is [ 2  4  6  8 10]


# All values > 5
np5 = np1[np1 > 5]
# np5 is [ 6  7  8  9 10]
