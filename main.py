import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
import pandas

# Read in csv
data_frame = pandas.read_csv('ontario-data.csv')

'''field = data_frame['field']
date = data_frame['date']
cost = data_frame['cost']'''

l = []

# Makes a list of data for each field
for i in range(1, len(data_frame)): 
    l.append(data_frame.iloc[i])

dates = ["2014 / 2015","2015 / 2016","2016 / 2017","2017 / 2018","2018 / 2019"]

'''# List of all the fields 
l = list(data_frame['Field of study'])
l.pop(0)
l.pop(0)

print(data_frame.iloc[1])'''

'''data = data_frame.iloc[3]
cost = data["2014 / 2015"]

print(data)
print(cost)'''


output_file('index.html', title='temp')

# Add plot

p = figure (
    x_range=dates,
    plot_width = 800,
    plot_height= 600,
    title = "Plot Title",
    x_axis_label = "Date",
    y_axis_label= "Cost",
    tools="pan,wheel_zoom,save"
)

'''p = figure (
    x_range=date,
    plot_width = 800,
    plot_height= 600,
    title = "Plot Title",
    x_axis_label = "Date",
    y_axis_label= "Cost",
    tools=""
)'''

# Render glyph
#p.line(x, y, legend="Field 1", line_width=2)
#p.line(date, cost, legend = "field")


#p = figure(width=500, height=300, x_axis_type="datetime") 

data_size = len(l)-1
cost = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(data_size):
    for j in range(1, 6):
        cost[i].append(l[i][j])
    #print(l[i][0])
    #print(cost[i])
    '''p.line(
        y=cost,
        x=dates,
        legend=str(i)
    )
    cost.clear()'''

#cost = ['6481', '6658', '6695', '6826', '7016']

for i in range(data_size):
    print(l[i][0])
    print(cost[i])
    p.line(
        y=cost[i],
        x=dates,
        legend=l[i][0]
    )

'''p.line(
    y=cost,
    x=dates,
    legend="line"
)'''
'''p.line(
    y=cost,
    x=date,
    legend="total"
)
p.line(
    y=cost,
    x=date,
    legend="education"
)'''


# Show results 
show(p)