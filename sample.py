from pack import selectArea

import numpy as np

x=5*np.random.random_sample(10000)
y=4*np.random.random_sample(10000)

selectArea.hrpoly(x,y,'sample.png','sample.csv')
