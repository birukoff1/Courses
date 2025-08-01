import numpy as np
from scipy import stats
from scipy.optimize import minimize_scalar

import matplotlib.pyplot as plt

N = 876832
sigma = 5.34
cdf = 0.95
cdf_value = 48.5

def objective(root):
    global sigma, cdf, cdf_value
    gauss = stats.norm(root, sigma)
    return abs(cdf-gauss.sf(cdf_value))


root = minimize_scalar(objective, bounds=(cdf_value, cdf_value+6*sigma), method='bounded')
mean = root.x.round(2)

print()
      
x = np.linspace(mean-3*sigma, mean+3*sigma, 1000)
y = stats.norm(mean, sigma)
print(y.cdf(cdf_value))

y = y.cdf(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.grid(True)
plt.xlim((x[0], x[-1]))
plt.vlines(cdf_value, 0, max(y), colors=['red'], linestyles='dashed')
plt.show()