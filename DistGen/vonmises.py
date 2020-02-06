from scipy.stats import vonmises
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
kappa = 3.99
mean, var, skew, kurt = vonmises.stats(kappa, moments='mvsk')

x = np.linspace(vonmises.ppf(0.01, kappa),
                vonmises.ppf(0.99, kappa), 100)
#ax.plot(x, vonmises.pdf(x, kappa),
#        'r-', lw=5, alpha=0.6, label='vonmises pdf')
rv = vonmises(kappa)
#ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

vals = vonmises.ppf([0.001, 0.5, 0.999], kappa)
np.allclose([0.001, 0.5, 0.999], vonmises.cdf(vals, kappa))

r = vonmises.rvs(kappa, size=1000)
print(r)
print(vonmises.mean(kappa))

#ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
#ax.legend(loc='best', frameon=False)
#plt.show()
