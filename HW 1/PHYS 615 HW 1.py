import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, (2*np.pi), 1000)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, y)
plt.show