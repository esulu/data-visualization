import numpy as np
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category20
import pandas

# Read in csv
df = pandas.read_csv('ontario-data.csv')

# Create ColumnDataSource from the data frame
source = ColumnDataSource(df)

field = source.data['field']
cost = source.data['cost']
date = source.data['date']

field_list = df.field.unique()

dates = df.date.unique().tolist()

output_file('index.html', title='Ontario Tuition Fees')

p = figure (
    x_range=dates,
    plot_width = 800,
    plot_height= 600,
    title = "Ontario undergraduate tuition fees by field of study",
    x_axis_label = "Date",
    y_axis_label= "Cost",
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
        color = (Category20[len(field)/5])[i],
        line_width=3
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
show(p)

# Save file
#save(p)