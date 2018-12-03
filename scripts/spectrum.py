# Gravitational wave spectrum diagram
import matplotlib.pyplot as plt
plt.style.use("../thesis-style.mpl")

import astropy.units as u
import numpy as np

import grasshopper.interferometers as ifo
import grasshopper.timingarray as arrays


parameters = {
    "acoustic": {
        "color": "red",
        "range": [1e0, 1e4]
    },
    "space": {
        "color":"blue",
        "range": [1e-4, 1e0]
    }
}

figsize = (6.0, 6.0/1.618) 
f, ax = plt.subplots(1,1, figsize=figsize)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim([1e-12, 1e4])

aligo = ifo.AdvancedLIGO()
ax.text(280, 6e-23, r"\textsf{aLIGO}", rotation=60, rotation_mode='anchor', fontsize=6)
geo = ifo.GEO()
ax.text(280, 1.5e-21, r"\textsf{GEO}", rotation=60, rotation_mode='anchor', fontsize=6)
elisa = ifo.EvolvedLISA()
bdecigo = ifo.BDecigo()
decigo = ifo.Decigo()
bbo = ifo.BigBangObservatory()
print(decigo.noise_amplitude(decigo.frequencies))
lisa = ifo.LISA()
#ipta = arrays.IPTA()
ax.text(0.07, 3e-20, r"\textsf{eLISA}", rotation=60, rotation_mode='anchor', fontsize=6)
aligo.plot(ax, color="k", lw=1)
lisa.plot(ax)
bdecigo.plot(ax)
bbo.plot(ax)
decigo.plot(ax)
elisa.plot(ax, color="k", lw=1)
geo.plot(ax, color="k", lw=1)
#ipta.plot(ax, color="k", lw=1)

for band in parameters.items():
    ymax = ax.get_ylim()[1]
    #ax.text((band[1]["range"][1] - band[1]["range"][0])/2, ymax-100, r"{}".format(band[0]))
    ax.axvspan(band[1]["range"][0], band[1]["range"][1], alpha=0.1, color=band[1]["color"])
#ax.grid(which="minor", lw=0.5, linestyle="..", zorder=100)

import grasshopper.sources as sources
# sources
cbc = sources.IMR(m1=30*u.solMass, m2=32*u.solMass, r=900*1e6*u.parsec)
cbc.plot(ax)


f.tight_layout()
f.savefig("gw-spectrum.pdf", dpi=300)
