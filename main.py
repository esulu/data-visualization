import numpy as np
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import ColumnDataSource
import pandas

# Read in csv
data_frame = pandas.read_csv('ontario-data.csv')

# Create ColumnDataSource from the data frame
source = ColumnDataSource(data_frame)

data_list = source.data['Field of study'].tolist()
cost_list = source.data['2014 / 2015'].tolist()

print(data_list)
print(cost_list)

l = []

# Makes a list of data for each field
for i in range(1, len(data_frame)): 
    l.append(data_frame.iloc[i])

dates = ["2014 / 2015","2015 / 2016","2016 / 2017","2017 / 2018","2018 / 2019"]

output_file('index.html', title='temp')

# Add plot

p = figure (
    x_range=dates,
    plot_width = 800,
    plot_height= 600,
    title = "Plot Title",
    x_axis_label = "Date",
    y_axis_label= "Cost",
    tools="pan,wheel_zoom,save,reset"
)

# Render glyph

#p = figure(width=500, height=300, x_axis_type="datetime") 

data_size = len(l)-1
cost = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(data_size):
    for j in range(1, 6):
        cost[i].append(l[i][j])

#cost = ['6481', '6658', '6695', '6826', '7016']

'''for i in range(data_size):
    p.line(
        y=cost[i],
        x=dates,
        legend=l[i][0]
    )'''

p.line(
        y='Field of study',
        x='2014 / 2015',
        #legend=l[i][0],
        legend='temp',
        source=source
    )
# Show results 
show(p)