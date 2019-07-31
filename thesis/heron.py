import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
from matplotlib import rc, font_manager
import matplotlib.pyplot as plt
import numpy as np
import pycbc
import pandas as pd


def match(a, b, psd=None):
    
    data_a = a.pycbc()
    data_b = b.pycbc()
    
    if psd == "aligo":
        f_low = 5
        f_delta = 1./16
        flen = int(2048/ f_delta) + 1
        psd = pycbc.psd.aLIGOZeroDetHighPower(flen, f_delta, f_low)
    
        return pycbc.filter.match(data_a, data_b, psd=psd)
    
    else:
        return pycbc.filter.match(data_a, data_b)
    
def triangle_match_plot(data, parameters, match_col, figsize=(9, 9), additional=[]):
        """
        Plot an n-dimensional corner plot to illustrate the
        parameter space coverage of this catalogue.

        Parameters
        ----------
        figsize : tuple
           The size of the figure to be produced.
        additional : list
           A list of additional points to be added to the plot.

        Returns
        -------
        figure: `matplotlib.figure.Figure`#
           The figure object containing the corner plot.
        """

        lato = {'family': 'Lato',
                'color':  'black',
                'weight': 'light',
                'size': 10,
        }
        
        ssp_ticks = {'family': 'Source Code Pro',
             'weight': 'light',
             'size': 7,
        }

        ticks_font = font_manager.FontProperties(**ssp_ticks)

        f = plt.figure(figsize=figsize, dpi=300)

               
        if not isinstance(additional, pd.DataFrame):
            # Convert additional to an array
            additional = pd.DataFrame(additional)

        # produce an n x n grid of subplots
        gs = gridspec.GridSpec(len(parameters), len(parameters),
                               wspace=0.05, hspace=0.05)


        # Make a legend for the additional points
        legend_ax = plt.subplot(gs[1,3])
        legend_ax.axis("off")
        legend_ax.grid(None)
        for i, point in enumerate(additional.iterrows()):
             legend_ax.scatter(0, i, marker="o", c=point[1]['color'], alpha=0.7)
             legend_ax.text(0.02, i, point[1]['label'], ha="left", va="center", fontdict=lato)
        legend_ax.set_xlim([-0.05, 0.3])
             
        for i, parameter in enumerate(parameters):
            for j, j_parameter in enumerate(parameters):

                if i >= j:
                    # Don't produce a plot for combinations above the
                    # diagonal.
                    continue
                else:
                    # Produce a subplot for combinations on or below
                    # the diagonal
                    ax = plt.subplot(gs[j, i])
                    ax.grid(None)

                if i == j:
                    continue
                    # This is the on-diagonal case, which we'll just skip for
                    # now. Ideally will want to insert a histogram here.
                    ax.hist(data[parameter], histtype="step")
                    ax.yaxis.tick_right()
                    ax.set_yticks(ax.get_yticks()[1:-1])
                    for label in ax.get_yticklabels():
                        label.set_fontproperties(ticks_font)
                else:
                    
                    # Add in the 'additional' points
                    #ax.scatter(additional[parameter], additional[j_parameter], marker="o", c=additional['color'], alpha=0.7)


                    # Produce a scatter plot of the waveforms for this
                    # combination
                    cscat = ax.scatter(data[parameter],
                               data[j_parameter],
                               c = 1.-data[match_col],
                               norm=colors.LogNorm(vmin=0.001, vmax=0.2),
                               cmap="viridis",
                               marker=".")
                if j == len(parameters) - 1:
                    ax.set_xlabel(parameter.replace("_", " "), fontdict=lato)
                    labels = ax.xaxis.get_ticklabels()
                    for label in ax.get_xticklabels():
                        label.set_fontproperties(ticks_font)
                else:
                    ax.set_xticks([])

                if i == 0:
                    ax.set_ylabel(j_parameter.replace("_", " "), fontdict=lato)
                    
                    for label in ax.get_yticklabels():
                        label.set_fontproperties(ticks_font)
                elif not i == j:
                    ax.set_yticks([])

        cbar = f.colorbar(cscat, ax=legend_ax, extend="max", fraction=0.5, shrink=1.2, )
        cbar.set_label("Mismatch", fontdict=lato)
        for label in legend_ax.get_yticklabels():
            label.set_fontproperties(ticks_font)
        
        #legend_ax.set_scale("log")
                    
        f.tight_layout()
        #thesis.thesisify(f, height=2)
        return f
