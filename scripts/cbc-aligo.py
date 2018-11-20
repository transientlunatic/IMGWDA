import astropy.units as u
import numpy as np

import grasshopper.interferometers as ifo
import grasshopper.sources as sources

import matplotlib.pyplot as plt
plt.style.use("../thesis-style.mpl")

aligo = ifo.AdvancedLIGO()
aligo_o1 = ifo.AdvancedLIGO(configuration="O1")
figsize = (5.0, 5.0/1.618) # Fix this to use the Golden ratio please

fig, ax = plt.subplots(1,1, figsize=figsize)


aligo = ifo.AdvancedLIGO()

cbc = sources.CBC(frequencies=np.logspace(-4, 5, 1000) * u.hertz,
                  m1=30*u.solMass, m2=32*u.solMass, r=0.8*1e9*u.parsec)
cbc.plot(ax, label="BBH 30, 32")


bns = sources.CBC(frequencies=np.logspace(-4, 5, 1000) * u.hertz,
                  m1=1.4*u.solMass, m2=1.4*u.solMass, r=40*1e6*u.parsec)

bns.plot(ax, label="BNS")

aligo.plot(ax)

ax.set_xlim([1e0, 4e3])

fig.tight_layout()
fig.savefig("aligo-cbc.pdf", dpi=300)
