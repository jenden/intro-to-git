from pathlib import Path

import pandas as pd
import plotly
import plotly.express as px

DATA_PATH = Path('data/processed/covid19-daily.csv')

data = pd.read_csv(DATA_PATH)

data['days_since_100'] = data[data['confirmed'] > 100] \
        .sort_values('date') \
        .groupby('country') \
        .cumcount()

top_n = data.groupby('country')['confirmed'].max().sort_values(ascending=False).head(25)

y_max = max(data['confirmed']) * 1.1
labels = {
    'days_since_100': 'Days Since 100 Cases',
    'confirmed': 'Confirmed Cases',
    'country': 'Country/Region',
    'date': 'Date'
}

fig = px.line(x='days_since_100', y='confirmed', color='country', 
              data_frame=data.loc[data['country'].isin(top_n.index)].sort_values('date'),
              log_y=True, range_y=[100, y_max], labels=labels)

plotly.offline.plot(fig, filename='figures/covid-19-cases.html')
