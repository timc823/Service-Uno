from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import PuOr8
from bokeh.embed import components
import pandas

# Read in csv

df = pandas.read_csv('Data.csv')

# Create ColumnDataSource from data frame
source = ColumnDataSource(df)

output_file('index.html')

# server list
server_list = source.data['Server'].tolist()

#add plot
p = figure(
    y_range=server_list,
    plot_width=800,
    plot_height=600,
    title='ServiceUno',
    x_axis_label='Server Experience',
    tools="pan, box_select, zoom_in, zoom_out, save, reset"
)

# Render glyph
p.hbar(
    y='Server',
    right='Server Experience',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
      'Server',
      palette=PuOr8,
      factors = server_list
    ),
    fill_alpha=0.9,
    source=source,
    legend='Server'
)

# Add Legend
p.legend.orientation='vertical'
p.legend.location='top_right'
p.legend.label_text_font_size='10px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
 <div>
   <h3>@Server</h3>
   <div><strong>Seated: </strong>@Seated</div>
   <div><strong>Greated: </strong>@Greated</div>
   <div><strong>Ordered: </strong>@Ordered</div>
   <div><strong>Drinks: </strong>@Drinks</div>
   <div><strong>Appetizer: </strong>@Appetizer</div>
   <div><strong>Food: </strong>@Food</div>
   <div><strong>Cleaned: </strong>@Cleaned</div>
   <div><strong>Satisfied: </strong>@Satisfied</div>
   <div><strong>Friendly: </strong>@Friendly</div>
   <div><strong>Bill: </strong>@Bill</div>
   <div><strong>Tips: </strong>@Tips</div>
   <div><strong>Total: </strong>@Total</div>
   <div><img src="@Image" alt="" width="200" /></div>
   </div>
"""
p.add_tools(hover)

# Show results
show(p)

#Save File
save(p)

# Print out div and script
#script, div = components(p)
#print(div)
#print (script)