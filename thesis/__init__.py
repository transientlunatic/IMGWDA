"""
Ths file contains a number of bits and pieces which are designed to make the scripts (mostly plotting scripts) work just a little bit better for my thesis. 
"""

from matplotlib import rc, font_manager
from math import atan2,degrees
import numpy as np
from matplotlib import rc, font_manager
import matplotlib.patheffects as path_effects

colors = {"blue": "#348ABD",
          "red": "#E24A33",
          "purple": "#988ED5",
          "gray": "#777777",
          "yellow": "#FBC15E",
}

figwidth = 5 # 2.5
figheight = figwidth/1.616
figsize = (figwidth, figheight)


## FONTS

ssp_legend = {'family': 'Source Code Pro',
              'weight': 'normal',
              'size': 9,
}

lato = {'family': 'Lato',
        'color':  'black',
        'weight': 'light',
        'size': 11,
}
ssp_ticks = {'family': 'Source Code Pro',
             'weight': 'normal',
             'size': 9,
}

ticks_font = font_manager.FontProperties(**ssp_ticks)

def thesisify(f, height=1):
    rc("mathtext", fontset="custom", sf="Source Code Pro", tt="Source Code Pro", rm="Source Code Pro")
    # make the figure look the correct size
    f.set_figwidth(figwidth)
    f.set_figheight(height * figheight)
    # individual axis manipulations
    for ax in f.axes:
        #ax.get_yaxis().get_major_formatter()._useMathText=False
        #ax.get_xaxis().get_major_formatter()._useMathText=False
        for label in ax.get_xticklabels():
            label.set_fontproperties(ticks_font)
        ax.set_xlabel(ax.get_xlabel(), fontdict=lato)  
        ax.xaxis.get_offset_text().set_fontproperties(ticks_font)
        for label in ax.get_yticklabels():
            label.set_fontproperties(ticks_font)
        ax.set_ylabel(ax.get_ylabel(), fontdict=lato) 
        ax.yaxis.get_offset_text().set_fontproperties(ticks_font)
        
        if len(ax.get_ygridlines()) > 0:
            ax.grid(which="both", color='#348ABD', alpha=0.2, lw=0.3,)
        
    f.tight_layout()
    return f


def labelLine(line,x,label=None,align=True, yshift=2, **kwargs):
    
    ax = line.axes
    xdata = line.get_xdata().value
    ydata = line.get_ydata().value
    
    if (x < xdata[0]) or (x > xdata[-1]):
        print('x label location is outside data range!')
        return

    #Find corresponding y co-ordinate and angle of the line
    ip = 1
    for i in range(len(xdata)):
        if x < xdata[i]:
            ip = i
            break

    y = ydata[ip-1] + (ydata[ip]-ydata[ip-1])*(x-xdata[ip-1])/(xdata[ip]-xdata[ip-1])

    
    
    if not label:
        label = line.get_label()

    if align:
        #Compute the slope
        dx = xdata[ip] - xdata[ip-1]
        dy = ydata[ip] - ydata[ip-1]
        ang = degrees(atan2(dy,dx))

        #Transform to screen co-ordinates
        pt = np.array([x,y]).reshape((1,2))
        trans_angle = ax.transData.transform_angles(np.array((ang,)),pt)[0]
    else:
        trans_angle = 0

    y*=yshift
        
    #Set a bunch of keyword arguments
    if 'color' not in kwargs:
        kwargs['color'] = line.get_color()

    if ('horizontalalignment' not in kwargs) and ('ha' not in kwargs):
        kwargs['ha'] = 'center'

    if ('verticalalignment' not in kwargs) and ('va' not in kwargs):
        kwargs['va'] = 'center'

    #if 'backgroundcolor' not in kwargs:
    #    kwargs['backgroundcolor'] = ax.get_facecolor()

    if 'clip_on' not in kwargs:
        kwargs['clip_on'] = True

    if 'zorder' not in kwargs:
        kwargs['zorder'] = 2.5

    label = ax.text(x,y,label,rotation=trans_angle,fontdict=lato, **kwargs)
    label.set_path_effects([path_effects.Stroke(linewidth=2, foreground='white'),
                           path_effects.Normal()])

def labelLines(lines,align=True,xvals=None,**kwargs):

    ax = lines[0].axes
    labLines = []
    labels = []

    #Take only the lines which have labels other than the default ones
    for line in lines:
        label = line.get_label()
        if "_line" not in label:
            labLines.append(line)
            labels.append(label)

    if xvals is None:
        xvals = []
        for line in lines:
            xvals.append(line.get_data()[0][-1].value*0.8)

    for line,x,label in zip(labLines,xvals,labels):
        labelLine(line,x,label,align,**kwargs)
