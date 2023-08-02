import numpy as np

np1 = np.array([0,1,2,3,4,5,6,7,8,9])

# Square root of each element
np2 = np.sqrt(np1)
"""
[0.         1.         1.41421356 1.73205081 2.         2.23606798
 2.44948974 2.64575131 2.82842712 3.        ]

"""

# Absolute value
np3 = np.array([-3, -5, 4, 6])
np4 = np.absolute(np3)
"""
[3 5 4 6]
"""

# Exponents
np5 = np.exp(np1)
"""
[1.00000000e+00 2.71828183e+00 7.38905610e+00 2.00855369e+01
 5.45981500e+01 1.48413159e+02 4.03428793e+02 1.09663316e+03
 2.98095799e+03 8.10308393e+03]
"""

# Min / Max
min = np.max(np1) # is 0
max = np.max(np1) # is 9

# Sign
signs = np.sign(np3)
# signs is [-1, -1,  1,  1]
# returns -1, 0 or 1

# sin / cos / log
a = np.sin(np3)
# [-0.14112001,  0.95892427, -0.7568025 , -0.2794155 ]
b = np.log(np3)
# [ nan nan 1.38629436 1.79175947]


