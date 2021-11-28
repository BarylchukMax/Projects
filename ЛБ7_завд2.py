from collections import Counter
import matplotlib.pyplot as plt
c = Counter("Як дитиною, бувало, упаду собі на лихо")
plt.bar(*zip(*c.most_common()), width=0.7, color='gray', edgecolor='black')
plt.show()