import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)
t2 = t ** 2
t3 = t ** 3

fig, ((ax1, ax2, ax3)) = plt.subplots(1, 3, figsize=(8, 4))

ax1.plot(t, t, 'g^')
ax2.plot(t, t2, 'bs')
ax3.plot(t, t3, 'ko')
plt.show()
