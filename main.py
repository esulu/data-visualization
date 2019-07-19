import numpy as np
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models import ColumnDataSource, HoverTool
import pandas

# Read in csv
df = pandas.read_csv('sample.csv')

# Create ColumnDataSource from the data frame
source = ColumnDataSource(df)

field_list = source.data['field'].tolist()
cost_list = source.data['cost'].tolist()
date_list = source.data['date'].tolist()

# Elements in each list
n = 5

final = [cost_list[i * n:(i + 1) * n] for i in range((len(cost_list) + n - 1) // n )]  
print(cost_list)
print(final)

'''print(data_list)
print(cost_list)
print(date_list)'''

'''l = []

# Makes a list of data for each field
for i in range(1, len(df)): 
    l.append(df.iloc[i])'''

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

'''
data_size = len(l)-1
cost = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(data_size):
    for j in range(1, 6):
        cost[i].append(l[i][j])

#cost = ['6481', '6658', '6695', '6826', '7016']

for i in range(data_size):
    p.line(
        y=cost[i],
        x=dates,
        legend=l[i][0]
    )'''

# Problem: Making one line, so it connects all sections
'''p.line(
        y='cost',
        x='date',
        source=source
    )'''

# Problem: Multi line required a list of lists for the xs and ys
p.multi_line(
    xs= date_list, 
    ys = cost_list,
    legend="line"
)

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@field</h3>
        <div><strong>Cost: $</strong>@cost</div>
        <div><strong>Year: </strong>@date</div>
    <div
"""

p.add_tools(hover)

# Show results 
#show(p)

# Save file
save(p)