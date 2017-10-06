import numpy as np
n = np.random(15)
n[n.argmax()] = 100
print(n)