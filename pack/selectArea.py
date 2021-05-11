from .polygonPoints import PolygonInteractor as plg
from matplotlib.patches import Polygon
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib
from matplotlib.ticker import AutoMinorLocator


def hrpoly(x,y,figname,outputname):
	start_time=time.time()

	data=pd.DataFrame({'x':x,'y':y})

	fig=plt.figure()
	fig.set_figheight(7.5)
	fig.set_figwidth(7.5)
	
	sx,sy=[x.min(),x.min(),x.max(),x.max()],[y.min(),y.max(),y.max(),y.min()]
	poly=Polygon(np.column_stack([sx,sy]),alpha=0.2,color='yellow',animated=True)
	ax=fig.add_subplot(111)
	ax.add_patch(poly)
	
	p=plg(ax,poly,data,figname,outputname)
	
	sc=ax.scatter(x,y,c='k',ec=None,alpha=0.8,s=1)

	ax.set_xlabel('x')
	ax.xaxis.label.set_fontsize(12)
	ax.set_ylabel('y')
	ax.yaxis.label.set_fontsize(12)
	ax.xaxis.label.set_color('red')
	ax.yaxis.label.set_color('red')
	ax.xaxis.set_minor_locator(AutoMinorLocator(5))
	ax.yaxis.set_minor_locator(AutoMinorLocator(5))
	ax.tick_params(which='both', width=1)
	ax.tick_params(which='major', length=7)
	ax.tick_params(which='minor', length=4)

	ax.grid(True)
	
	plt.show()
	end_time=time.time()
	elapsed=end_time-start_time
	print('total time: ',elapsed,' seconds')

