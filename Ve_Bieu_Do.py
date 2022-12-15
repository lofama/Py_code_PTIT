import matplotlib.pyplot as pp
import numpy as np

months=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
incomes = np.array([15.6, 14, 13.4, 123.2, 12, 6, 7,4, 8, 90, 11,13])
pp.bar(months, incomes)
pp.show()