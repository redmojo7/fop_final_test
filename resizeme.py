import numpy as np

data = np.zeros((4, 2, 2))
data[1, 0, 1] = 4
data[0, 1, 0] = 8
data[3, 1, 1] = 12
data = data / 2
print(data)
data = data + 10
data.resize(4, 4)
print(data)
