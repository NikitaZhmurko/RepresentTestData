import pandas as pd
import dash
from dash import dcc, html, dash_table
import plotly.express as px
from dash.dependencies import Input, Output


def parse_teststand_data(file_path):

    with open(file_path, "r") as file:
        file_lines = file.readlines()

    #process metadata
    metadata = {}

    for line in file_lines:
        if line.startswith("-----------") or line.startswith("~-~-~-~-~-~"):
            break

        metadata_parts = line.strip().split(",")
        key = metadata_parts[0].strip()

        if len(metadata_parts) > 1:
            value = metadata_parts[1].strip()
        else: 
            value = ""
        
        if key:
            metadata[key] = value

    #process data
    data_start_line_number = 0
    for i, line in enumerate(file_lines):
        if line.startswith("~-~-~-~-~-~"):
            data_start_line_number = i + 1
            break
    try:
        data = pd.read_csv(file_path, skiprows=data_start_line_number)
    except pd.errors.EmptyDataError:
        data = pd.DataFrame()

    return metadata, data



file_path = "./test_greenlight.csv"
metadata, data = parse_teststand_data(file_path)
print(metadata, data)

app = dash.Dash(__name__)

# Layout 
app.layout = html.Div([
    html.H1("Teststand Daten"),

    html.H2("Metadaten"),
    html.Ul([html.Li(f"{key}: {value}") for key, value in metadata.items()]),


    html.H2("Visualisierung"),
    html.Label("Wähle X-Achse:"),
    dcc.Dropdown(id='x-axis', options=[{'label': col, 'value': col} for col in data.columns], value=data.columns[0]),
    html.Label("Wähle Y-Achse:"),
    dcc.Dropdown(id='y-axis', options=[{'label': col, 'value': col} for col in data.columns], value=data.columns[1]),
    dcc.Graph(id='line-chart')
])

@app.callback(
    Output('line-chart', 'figure'),
    Input('x-axis', 'value'),
    Input('y-axis', 'value')
)
def update_graph(x_axis, y_axis):
    graph = px.line(data, x=x_axis, y=y_axis)
    return graph

if __name__ == '__main__':
    app.run(debug=True)