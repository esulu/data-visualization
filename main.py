from bokeh.plotting import figure, output_file, show
import pandas

# Read in csv
data_frame = pandas.read_csv('ontario-data.csv')

field = data_frame["Field of study"]
year_14 = data_frame["2014 / 2015"]

output_file('index.html', title='example data')

# Add plot
p = figure (
    plot_width = 800,
    plot_height= 600,
    title = "Plot Title",
    x_axis_label = "X Axis",
    y_axis_label= "Y Axis",
    tools=""
)

# Render glyph
p.line(x, y, legend="Test", line_width=2)

# Show results 
show(p)