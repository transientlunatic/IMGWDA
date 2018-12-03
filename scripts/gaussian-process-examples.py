"""
This file builds the figures which demonstrate the training of a Gaussian process.
"""

figwidth = 6 # 2.5
figheight = 6/1.616

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

np.random.seed(200)
n = 150
X = np.sort(40*np.random.rand(n))[:,None]

# define gp, true parameter values
with pm.Model() as model:
    l_per_true = 2
    cov_per = pm.gp.cov.Cosine(1, l_per_true)

    l_drift_true = 4
    cov_drift = pm.gp.cov.Matern52(1, l_drift_true)

    s2_p_true = 0.3
    s2_d_true = 1.5
    s2_w_true = 0.3

    periodic_cov = s2_p_true * cov_per
    drift_cov    = s2_d_true * cov_drift

    signal_cov   = periodic_cov + drift_cov
    noise_cov    = s2_w_true**2 * tt.eye(n)


K = theano.function([], signal_cov(X, X) + noise_cov)()
y = np.random.multivariate_normal(np.zeros(n), K)

fig = plt.figure(figsize=(figwidth,figheight)); ax = fig.add_subplot(111)
#ax.plot(X, y, '--', color=cm(0.4))
ax.plot(X, y, '.');
ax.set_xlabel("x");
ax.set_ylabel("f(x)");
plt.tight_layout()
fig.savefig("../figures/gp-training-data.pdf")


with pm.Model() as model:
    # prior for periodic lengthscale, or frequency
    l_per = pm.Uniform('l_per', lower=1e-5, upper=10)

    # prior for the drift lengthscale hyperparameter
    l_drift  = pm.Uniform('l_drift', lower=1e-5, upper=10)

    # uninformative prior on the periodic amplitude
    log_s2_p = pm.Uniform('log_s2_p', lower=-10, upper=5)
    s2_p = pm.Deterministic('s2_p', tt.exp(log_s2_p))

    # uninformative prior on the drift amplitude
    log_s2_d = pm.Uniform('log_s2_d', lower=-10, upper=5)
    s2_d = pm.Deterministic('s2_d', tt.exp(log_s2_d))

    # uninformative prior on the white noise variance
    log_s2_w = pm.Uniform('log_s2_w', lower=-10, upper=5)
    s2_w = pm.Deterministic('s2_w', tt.exp(log_s2_w))

    # the periodic "signal" covariance
    signal_cov = s2_p * pm.gp.cov.Cosine(1, l_per)

    # the "noise" covariance
    drift_cov  = s2_d * pm.gp.cov.Matern52(1, l_drift)

    y_obs = pm.gp.GP('y_obs', cov_func=signal_cov + drift_cov, sigma=s2_w, observed={'X':X, 'Y':y})

with model:
    trace = pm.sample(10000, tune=1000, step=pm.Metropolis(), njobs=4)#2000, step=pm.NUTS())#integrator="two-stage"))#, init=None)

pm.traceplot(trace[1000:], varnames=['l_per', 'l_drift', 's2_d', 's2_p', 's2_w'],
            lines={"l_per": l_per_true,
                   "l_drift": l_drift_true,
                   "s2_d":    s2_d_true,
                   "s2_p":    s2_p_true,
                   "s2_w":    s2_w_true});
#plt.show()

Z = np.linspace(0, 40, 100).reshape(-1, 1)
with model:
    gp_samples = pm.gp.sample_gp(trace[1000:], y_obs, Z, samples=50, random_seed=42, progressbar=False)


fig, ax = plt.subplots(figsize=(figwidth,figheight))

[ax.plot(Z, x, color=cm(0.3), alpha=0.3) for x in gp_samples]
# overlay the observed data
ax.plot(X, y, '.');
ax.set_xlabel("x");
ax.set_ylabel("f(x)");
ax.set_title("Posterior predictive distribution");
plt.tight_layout()
plt.savefig("gp-posterior.pdf")


