import numpy as np
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category10
import pandas

# Read in csv
df = pandas.read_csv('sample.csv')

# Create ColumnDataSource from the data frame
source = ColumnDataSource(df)

field = source.data['field']
cost = source.data['cost']
date = source.data['date']

field_list = df.field.unique()

#dates = date.tolist()
dates = ["2014 / 2015","2015 / 2016","2016 / 2017","2017 / 2018","2018 / 2019"]

'''dates_list = dates.tolist()
date_set = set(dates)
dates = list(date_set)'''

output_file('index.html', title='temp')

p = figure (
    x_range=dates,
    plot_width = 800,
    plot_height= 600,
    title = "Plot Title",
    x_axis_label = "Date",
    y_axis_label= "Cost",
    #tools="pan,wheel_zoom,save,reset"
)

# Add plot
for i in range(len(field_list)):
    source2 = ColumnDataSource(
         data={'date':df.loc[df.field == field_list[i]].date,
            'field':df.loc[df.field == field_list[i]].field,
            'cost':df.loc[df.field == field_list[i]].cost}
    )

    # Render glyph
    p.line(
        x='date',
        y='cost',
        source=source2,
        #legend = field_list[i],
        color = (Category10[3])[i]
    )







#p = figure(width=500, height=300, x_axis_type="datetime") 

# Problem: Making one line, so it connects all sections
'''p.line(
        y='cost',
        x='date',
        source=source
    )'''

# Problem: Multi line required a list of lists for the xs and ys
'''p.multi_line(
    xs= final_date, 
    ys = final_cost,
)'''

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