import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')
x = np.linspace(-3, 3)
y = (2**x) * np.sin(10 * x)
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2)
plt.show()
