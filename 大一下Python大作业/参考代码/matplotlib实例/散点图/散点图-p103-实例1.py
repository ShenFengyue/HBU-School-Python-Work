import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = np.random.randint(1, 10, size=10)
print(y)
plt.scatter(x,y,marker='v',s=2)

plt.show()

