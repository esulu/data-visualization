import numpy as np

from bokeh.plotting import figure, output_file, show
import pandas

def datetime(x):
    return np.array(x, dtype=np.datetime64)

# Read in csv
data_frame = pandas.read_csv('sample.csv')

##field = data_frame["field"]
date = data_frame['date']
cost = data_frame['cost']

output_file('index.html', title='example data')

# Add plot
p = figure (
    x_range=date,
    plot_width = 800,
    plot_height= 600,
    title = "Plot Title",
    x_axis_label = "Date",
    y_axis_label= "Cost",
    tools=""
)

# Render glyph
#p.line(x, y, legend="Field 1", line_width=2)
#p.line(date, cost, legend = "field")
p.line(
    y=cost,
    x=date
)

# Show results 
show(p)