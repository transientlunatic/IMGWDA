"""
Produces

gp-training-data.pdf
gp-example-prior-draws.pdf
"""

import thesis
import matplotlib.pyplot as plt
import matplotlib.cm as cmap
cm = cmap.inferno

plt.style.use("../thesis-style.mpl")


import numpy as np
import scipy as sp
import theano
import theano.tensor as tt
import theano.tensor.nlinalg
import sys
#sys.path.insert(0, "../../..")
import pymc3 as pm

x = np.linspace(0, 10, 20) 
x_unc = x + 0.5 * np.random.randn(len(x))
y = np.sin(x) + 0.5* np.random.randn(len(x))


### The training data plot

fig = plt.figure(figsize=thesis.figsize); ax = fig.add_subplot(111)
#ax.plot(X, y, '--', color=cm(0.4))
ax.plot(x, y, '.', ms=3, c='k');
ax.set_xlabel("$x$");
ax.set_ylabel("$f(x)$");
plt.tight_layout()
fig.savefig("../figures/gp-training-data.pdf")


### The Gaussian process posterior plot


with pm.Model() as model:
    ls = pm.HalfCauchy("metric", 2)
    # Specify the covariance function.
    cov_func = pm.gp.cov.ExpQuad(1, ls)
    # Specify the GP.  The default mean function is `Zero`.
    gp = pm.gp.Marginal(cov_func=cov_func)
    sigma = pm.Normal("sigma", .5, 2)
    y_ = gp.marginal_likelihood("y", X=x[::,None], y=y, noise=sigma)
with model:
    mp = pm.find_MAP()

x_new = np.linspace(0,10, 200)[::,None]
mu, var = gp.predict(x_new, point=mp, diag=True)
sd = np.sqrt(var)

# draw plot
fig = plt.figure(figsize=thesis.figsize); ax = fig.add_subplot(111)

# plot mean and 2 sigma intervals
plt.plot(x_new, mu, 'r', lw=2, label="mean and 2 sigma region");
for deviation in range(1,4):
    plt.fill_between(x_new.flatten(), mu - deviation*sd, mu + deviation*sd, color=thesis.colors['red'], alpha=0.5/deviation)

# plot original data and true function
plt.plot(x, y, 'ok', ms=1, alpha=1.0, label="observed data");

plt.xlabel("x");# plt.ylim([-13,13]);
plt.tight_layout()


### The Gaussian process prior plot using the appropriate length scale

ls = float(mp['metric'])
#ls= 0.25


with pm.Model() as model:
    # Specify the covariance function.
    cov_func = pm.gp.cov.ExpQuad(1, ls)
    # Specify the GP.  The default mean function is `Zero`.
    gp = pm.gp.Marginal(cov_func=cov_func)
    sigma = pm.Normal("sigma", 1, 5)
    y_ = gp.marginal_likelihood("y", X=x[::,None], y=y, noise=sigma)

    
fig = plt.figure(figsize=thesis.figsize)
ax = fig.add_subplot(111)
K = cov_func(x[::,None]).eval()
ax.plot(x, pm.MvNormal.dist(mu=np.zeros(K.shape[0]), cov=K).random(size=15).T, 
             alpha = 0.5, c=thesis.colors['blue'], lw=1, linestyle="--"
            );
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
fig.tight_layout();
fig.savefig("../figures/gp-example-prior-draws.pdf")
