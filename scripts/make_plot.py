from pathlib import Path

import pandas as pd
import plotly
import plotly.express as px

COLUMNS = ['date', 'country', 'confirmed']

COLUMN_MAP = {
    'Country/Region': 'country',
    'Country_Region': 'country',
    'Confirmed': 'confirmed',
    'Deaths': 'deaths',
    'Recovered': 'recovered',
}

COUNTRY_MAP = {
    'Mainland China': 'China',
    'US': 'United States',
}

DATA_DIR = Path('data')


def load_and_normalize(file) -> pd.DataFrame:
    df = pd \
        .read_csv(file) \
        .rename(columns=COLUMN_MAP) \
        .replace({'country': COUNTRY_MAP}) \
        .groupby('country', as_index=False) \
        .sum() \
        .assign(date=file.name.strip('*.csv')) \
        .loc[:,COLUMNS]
    
    return df


data = None

for file in sorted(DATA_DIR.glob('*.csv')):
    df = load_and_normalize(file)
    if data is None:
        data = df
    else:
        data = pd.concat([data, df])


data.reset_index(drop=True, inplace=True)
data['days_since_100'] = data[data['confirmed'] > 100].groupby('country').cumcount()


top_n = data.groupby('country')['confirmed'].max().sort_values(ascending=False).head(25)
y_max = max(data['confirmed']) * 1.1
labels = {
    'days_since_100': 'Days Since 100 Cases',
    'confirmed': 'Confirmed Cases',
    'country': 'Country/Region',
}


fig = px.line(x='days_since_100', y='confirmed', color='country', 
              data_frame=data.loc[data['country'].isin(top_n.index)], 
              log_y=True, range_y=[100, y_max], labels=labels)

plotly.offline.plot(fig, filename='figures/covid-19-cases.html')
