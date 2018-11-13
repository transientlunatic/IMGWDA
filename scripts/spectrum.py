# Gravitational wave spectrum diagram
import matplotlib.pyplot as plt
plt.style.use("../thesis-style.mpl")

import astropy.units as u
import numpy as np

import grasshopper.interferometers as ifo



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

figsize = (5.0, 2.5) # Fix this to use the Golden ratio please
f, ax = plt.subplots(1,1, figsize=figsize)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim([1e-12, 1e4])

aligo = ifo.AdvancedLIGO()
ax.text(280, 6e-23, r"\textsf{aLIGO}", rotation=60, rotation_mode='anchor', fontsize=6)
geo = ifo.GEO()
ax.text(280, 1.5e-21, r"\textsf{GEO}", rotation=60, rotation_mode='anchor', fontsize=6)
elisa = ifo.EvolvedLISA()
lisa = ifo.LISA()
ax.text(0.07, 3e-20, r"\textsf{eLISA}", rotation=60, rotation_mode='anchor', fontsize=6)
aligo.plot(ax, color="k", lw=1)
lisa.plot(ax)
elisa.plot(ax, color="k", lw=1)
geo.plot(ax, color="k", lw=1)

for band in parameters.items():
    ax.axvspan(band[1]["range"][0], band[1]["range"][1], alpha=0.1, color=band[1]["color"])
#ax.grid(which="minor", lw=0.5, linestyle="..", zorder=100)
        
f.tight_layout()
f.savefig("../figures/gw-spectrum.pdf", dpi=300)
