# Import packages 
from dash import Dash, dcc, html, Input , Output
import dash_bootstrap_components as dbc

# Initialise the App
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "My Dash App"
server = app.server

# Create app components
markdown = dcc.Markdown(id= 'my-markdown', children='My First app', style={'textAlign': 'center', 'font-size': 24, 'marginTop': 20, 'color': 'blue'})
button = html.Button(children="click me", id="my-button", n_clicks=0, style={'display': 'block', 'margin': '20px auto'})
checklist = dcc.Checklist(
    options=[
        {'label': 'Option 1', 'value': 'opt1'},
        {'label': 'Option 2', 'value': 'opt2'},
        {'label': 'Option 3', 'value': 'opt3'}
    ],
    value=['opt1', 'opt2'],
    id='my-checklist',
    style={'width': '50%', 'margin': '20px auto'}
)
radio = dcc.RadioItems(
    options=[
        {'label': 'Choice A', 'value': 'A'},
        {'label': 'Choice B', 'value': 'B'},
        {'label': 'Choice C', 'value': 'C'}
    ],
    value='A',
    id='my-radioitems',
    style={'width': '50%', 'margin': '20px auto'}
)   

dropdown = dcc.Dropdown(
    options=[
        {'label': 'Select 1', 'value': 'sel1'},
        {'label': 'Select 2', 'value': 'sel2'},
        {'label': 'Select 3', 'value': 'sel3'}
    ],
    value='sel1',
    id='my-dropdown',
    style={'width': '50%', 'margin': '20px auto'}
)   

slider = dcc.Slider(
    min=0,
    max=10,
    step=1,
    value=5,
    id='my-slider',
    marks={i: str(i) for i in range(11)},
    #style={'width': '50%', 'margin': '20px auto'}
)

# Define the app layout
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col([markdown], width=8)]),
        dbc.Row(
            [
                dbc.Col([dropdown], width = 3), 
                dbc.Col([slider], width = 9),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([checklist], width = 6),
                dbc.Col([radio], width = 6),
            ]
        ),
        dbc.Row([dbc.Col([button], width = 11)]),
    ]
)

#callbacks
@app.callback(
    Output('my-markdown', 'children'),
    Input('my-button', 'n_clicks'),
    Input('my-checklist', 'value'),
    Input('my-radioitems', 'value'),
    Input('my-dropdown', 'value'),
    Input('my-slider', 'value')
)
def update_markdown(n_clicks, checklist_values, radio_value, dropdown_value, slider_value):
    return f"""
    Button clicked: {n_clicks} times  
    Checklist selected: {', '.join(checklist_values)}  
    Radio selected: {radio_value}  
    Dropdown selected: {dropdown_value}  
    Slider value: {slider_value}  
    """

@app.callback(
    Output(component_id='my-markdown', component_property='style'),
    Input(component_id='my-slider', component_property='value')
)
def update_markdown(value_slider):
    markdown_style = {'textAlign': 'center', 'font-size': 12+2*value_slider, 'marginTop': 20, 'color': 'blue'}
    return markdown_style

# Run the app
if __name__ == "__main__":
    app.run(debug=False)
