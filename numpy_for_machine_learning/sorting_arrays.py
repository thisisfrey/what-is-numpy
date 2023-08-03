import numpy as np

# Sorting NumPy arrays
# Sorting returns a copy but does not change the original array
np1 = np.array([6, 7, 8, 9, 0, 2, 1])

# Numerical sorting
np2 = np.sort(np1)
# np2 is [0 1 2 6 7 8 9]

# Alphabetical sorting
np3 = np.array(["John", "Tina", "Aaron", "Anna", "Zed"])
np4 = np.sort(np3)
# np4 is ["Aaron" "Anna" "John" "Tina" "Zed"]

# Boolean sorting
np5 = np.array([True, False, False, True])
np6 = np.sort(np5)
# np6 is [False False  True  True]

# Sort 2D Array, sorting inside the rows
np7 = np.array([[6, 7, 1, 9], [8, 3, 5, 0]])
np8 = np.sort(np7)
"""
[[1 6 7 9]
 [0 3 5 8]]
"""
