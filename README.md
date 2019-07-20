# Data Visualization

This project is a means of converting the data of tuition fees of Ontario universities and colleges into an easily readable figure. The chart uses data from the 2014/2015 to the 2018/2019 school years. The Bokeh and pandas libraries are used to make the visualization of the project. 

### Installation Process

1. Clone the repository
2. Set up virtual environment 
```
pip install pipenv
pipenv shell
```
3. Install Bokeh and pandas
```
pipenv install bokeh pandas
```
4. Run the main file to display tuition data
```
python main.py
```

### Source  
Statistics Canada.  [Table  37-10-0003-01   Canadian undergraduate tuition fees by field of study](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3710000301)

Note: Only the data for Ontario is being used in this project

#### Checklist
- [x] Finish base code
- [x] Have different colours 
- [x] Show the name on hover
- [x] Hide fields that appear on the side
- [x] Add proper tools
- [x] Change the thickness of the lines
- [x] Optimize the code
- [x] Add the title for the plot and the page
- [x] Cite the data