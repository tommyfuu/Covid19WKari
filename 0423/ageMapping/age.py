import plotly.graph_objects as go
import pandas as pd
import json
import plotly.express as px

df = pd.read_csv('age.csv', usecols=['CITYNAME', 'YEAR', "AGEGRP", "TOT_POP"])

df2018 = df['YEAR'] == 11  # just the data from 2018


#TODO: manipulate data into a useful form
# calculate percentages
# get the fip thing to correspond somehow???
# graph it <3

with open('counties_locations.json') as response:
    counties = json.load(response)

fig = go.Figure(data=go.Choropleth(
    locations=df['Fips'], # Spatial coordinates
    z = df['Percentage'], # Data to be color-coded
    geojson = counties, # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "Diabetes %"
))

fig.update_layout(
    title_text = "USA by Diabetes %", 
    geo_scope = 'usa'
)

fig.show()