import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

a = np.random.randn(1000) - 2
b = np.random.randn(1000)
c = np.random.randn(1000) + 2
d = np.random.randn(1000) + 4

data = [a, b, c, d]
lables = ['A', 'B', 'C', 'D']

fig = ff.create_distplot(data, lables, bin_size = [.2, .1, .3, .4])
pyo.plot(fig, filename='distributionPlots.html')
