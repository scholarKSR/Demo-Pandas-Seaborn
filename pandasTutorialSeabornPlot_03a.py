#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title - 

Created on Thu Aug 29 07:12:48 2019
@author: k as root
"""

import matplotlib.pyplot as plt
plt.style.use('classic')
%matplotlib inline
import numpy as np
import pandas as pd

"""
# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

# Plot the data with Matplotlib defaults
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
"""

import seaborn as sns
sns.set()

# same plotting code as above!
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');

##Plot 2
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], normed=True, alpha=0.5)
    
##Plot 3
for col in 'xy':
    sns.kdeplot(data[col], shade=True)

##
sns.distplot(data['x'])
sns.distplot(data['y']);

##
sns.kdeplot(data);

##
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='kde');

##
with sns.axes_style('white'):
    sns.jointplot("x", "y", data, kind='hex')

### Pair Plots
iris = sns.load_dataset("iris")
iris.head()
##
sns.pairplot(iris, hue='species', size=2.5);

### Faceted histograms
tips = sns.load_dataset('tips')
tips.head()
##
tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']

grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15));

###Factor plots
with sns.axes_style(style='ticks'):
    g = sns.factorplot("day", "total_bill", "sex", data=tips, kind="box")
    g.set_axis_labels("Day", "Total Bill");

##Joint distributions
with sns.axes_style('white'):
    sns.jointplot("total_bill", "tip", data=tips, kind='hex')
#
sns.jointplot("total_bill", "tip", data=tips, kind='reg');

### Bar plots
planets = sns.load_dataset('planets')
planets.head()
##
with sns.axes_style('white'):
    g = sns.factorplot("year", data=planets, aspect=2,
                       kind="count", color='steelblue')
    g.set_xticklabels(step=5)

##
with sns.axes_style('white'):
    g = sns.factorplot("year", data=planets, aspect=4.0, kind='count',
                       hue='method', order=range(2001, 2015))
    g.set_ylabels('Number of Planets Discovered')

    
    
"""
https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html
"""