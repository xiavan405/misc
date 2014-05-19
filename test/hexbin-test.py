#!/usr/bin/env python

#test out using using hexbin heatmaps as an alternative to scatter since i want to see if density is useful

from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP

n = 1e5
x = y = NP.linspace(-5,5,100)
X, Y = NP.meshgrid(x,y)
Z1 = ML.bivariate_normal(X,Y,2,2,0,0)
Z2 = ML.bivariate_normal(X,Y,4,1,1,1)
ZD = Z2 - Z1
x = X.ravel()
y = Y.ravel()
z = ZD.ravel()
gridsize = 30
PLT.subplot(111)

PLT.hexbin(x,y,C=z,gridsize=gridsize,cmap=CM.jet,bins=None)
PLT.axis([x.min(),x.max(),y.min(),y.max()])

cb = PLT.colorbar()
cb.set_label('mean value')
PLT.show()
