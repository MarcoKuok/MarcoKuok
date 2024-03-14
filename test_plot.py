import plotly.graph_objs as go
import plotly.io as pio

# Create some data
x = [1, 2, 3, 4, 5]
y = [10, 11, 12, 13, 14]

# Create the plot
fig = go.Figure(data=go.Scatter(x=x, y=y))

# Save as HTML
pio.write_html(fig, file='plotly_graph.html', auto_open=True)
