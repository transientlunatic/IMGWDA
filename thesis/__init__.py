"""
Ths file contains a number of bits and pieces which are designed to make the scripts (mostly plotting scripts) work just a little bit better for my thesis. 
"""

from matplotlib import rc, font_manager

colors = {"blue": "#348ABD",
          "red": "#E24A33"}

figwidth = 6 # 2.5
figheight = 6/1.616
figsize = (figwidth, figheight)


## FONTS

ssp_legend = {'family': 'Source Code Pro',
              'weight': 'normal',
              'size': 8,
}

lato = {'family': 'Lato',
        'color':  'black',
        'weight': 'light',
        'size': 10,
}
ssp_ticks = {'family': 'Source Code Pro',
             'weight': 'normal',
             'size': 6,
}

ticks_font = font_manager.FontProperties(**ssp_ticks)

def thesisify(f, height=1):
    # make the figure look the correct size
    f.set_figwidth(figwidth)
    f.set_figheight(height * figheight)
    # individual axis manipulations
    for ax in f.axes:
        for label in ax.get_xticklabels():
            label.set_fontproperties(ticks_font)
        ax.set_xlabel(ax.get_xlabel(), fontdict=lato)  
        ax.xaxis.get_offset_text().set_fontproperties(ticks_font)
        for label in ax.get_yticklabels():
            label.set_fontproperties(ticks_font)
        ax.set_ylabel(ax.get_ylabel(), fontdict=lato) 
        ax.yaxis.get_offset_text().set_fontproperties(ticks_font)
        
        if len(ax.get_ygridlines()) > 0:
            ax.grid(which="both", color='#348ABD', alpha=0.4, lw=0.3,)
        
    f.tight_layout()
    return f
