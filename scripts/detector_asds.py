import astropy.units as u
import numpy as np

import grasshopper.interferometers as ifo
import grasshopper.sources as sources

import matplotlib.pyplot as plt
plt.style.use("../thesis-style.mpl")

aligo = ifo.AdvancedLIGO()
aligo_o1 = ifo.AdvancedLIGO(configuration="O1")
figsize = (5.0, 2.5) # Fix this to use the Golden ratio please

fig, ax = plt.subplots(1,1, figsize=figsize)
aligo.plot(ax)
aligo_o1.plot(ax)
ax.set_xlim([1e1, 2e3]);
ax.set_ylim([1e-23, 1e-19]);
fig.tight_layout()
fig.savefig("../figures/aligo-asd.pdf", dpi=300)



#########################


# aligo = ifo.AdvancedLIGO()


# figsize = (5.0, 2.5) # Fix this to use the Golden ratio please

# fig, ax = plt.subplots(1,1, figsize=figsize)
# aligo.plot(ax)

# for mass in [30, 32, 50, 100]:
#     for mass2 in [30, 100, 2000]:
#         cbc = sources.CBC(frequencies=np.logspace(-4, 5, 1000) * u.hertz,
#                        m1=mass*u.solMass, m2=mass2*u.solMass, r=0.8*1e9*u.parsec)
#         cbc.plot(ax, label="{}, {}".format(mass, mass2))

# ax.set_xlim([1e1, 2e3]);
# ax.set_ylim([1e-23, 1e-19]);
# fig.tight_layout()
# fig.savefig("../figures/aligo-cbc.pdf", dpi=300)


###########################


elisa = ifo.EvolvedLISA()
figsize = (5.0, 2.5) # Fix this to use the Golden ratio please

fig, ax = plt.subplots(1,1, figsize=figsize)
elisa.plot(ax)
#ax.set_xlim([1e-1, 2e3]);
#ax.set_ylim([1e-23, 1e-19]);
fig.tight_layout()
fig.savefig("../figures/elisa-asd.pdf", dpi=300)


iligo = ifo.InitialLIGO()
virgo = ifo.VIRGO()
geo = ifo.GEO()
tama = ifo.TAMA()

fig, ax = plt.subplots(1,1, figsize=figsize)
iligo.plot(ax)
virgo.plot(ax)
geo.plot(ax)
tama.plot(ax)

ax.set_xlim([1e1, 1e3]);
ax.set_ylim([1e-23, 1e-19]);
fig.tight_layout()
fig.savefig("../figures/first-gen-asd.pdf")


import grasshopper.sources as sources

ccsn = sources.CoreCollapseSupernova()
fig, ax = plt.subplots(1,1, figsize=figsize)
aligo.plot(ax)
ccsn.plot(ax)
ax.set_xlim([1e1, 1e3]);
#ax.set_ylim([1e-23, 1e-19]);
fig.tight_layout()
fig.savefig("../figures/source-ccsn.pdf")

ccsn = sources.Type1ASupernova(r=30*1000*u.parsec)
fig, ax = plt.subplots(1,1, figsize=figsize)
aligo.plot(ax)
ccsn.plot(ax)
ax.set_xlim([1e-1, 1e3]);
ax.set_ylim([1e-23, 1e-19]);
fig.tight_layout()
fig.savefig("../figures/source-t1asn.pdf")

# Izz = .02#1e-4*10**38#0.28*10**34 / 0.366*1e-4 * (np.sqrt(8*np.pi)/15)
# pulsar = sources.Pulsar("J0534+2200", Izz=Izz*u.kilogram*u.meter**2)
# aligo = ifo.AdvancedLIGO(obs_time = 365*3600*u.second)

# fig, ax = plt.subplots(1,1, figsize=figsize)
# aligo.plot(ax, configuration="O1")
# pulsar.plot(ax)
# ax.set_xlim(10, 1000)
# ax.set_ylim(1e-26, 1e-23)
# plt.tight_layout()
# fig.savefig("/home/daniel/papers/thesis/figures/crab-strain-o1.pdf")
