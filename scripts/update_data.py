"""
Download daily Covid-19 data by country from Johns Hopkins and compile into a single dataframe for further analysis.
"""

import argparse
from io import StringIO
from pathlib import Path
from datetime import date, datetime, timedelta
import logging


import pandas as pd
import requests


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

DATA_URL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'

COLUMNS = ['date', 'country', 'confirmed', 'deaths']  # name of columns to keep
COLUMN_MAP = {  # rename columns that change over time
    'Country/Region': 'country',
    'Country_Region': 'country',
    'Confirmed': 'confirmed',
    'Deaths': 'deaths',
    'Recovered': 'recovered',
}
COUNTRY_MAP = {  # Rename regions and/or countries
    'Mainland China': 'China',
    'US': 'United States',
}


def main(start, end, raw_dir, output_dir, overwrite=True):

    raw_path = Path(raw_dir).absolute()
    output_path = Path(output_dir).absolute().joinpath('covid19-daily.csv')

    if not raw_path.exists():
        logger.error(f'Path "{output_dir}" doesn\'t exist. Create the directory and try again.')
        raise IOError(f'No such directory: {raw_path}')

    logger.info(f'Downloading data for {start} - {end} to {str(raw_path)}')

    if overwrite:
        logger.info(f'Overwrite={overwrite}')

    dates = pd.date_range(start, end, freq='D')

    for date in dates:
        download_single_day(date, raw_path, overwrite)

    data = combine_files(raw_path)
    data.to_csv(output_path, index=False)

    logger.info(f'Combined dataset written to {output_path}')



def download_single_day(date, path, overwrite):
    formatted_date = date.to_pydatetime().strftime('%m-%d-%Y')

    destination_file = path.joinpath(f'{formatted_date}.csv')

    if destination_file.exists() and not overwrite:
        logger.info(f'{formatted_date} -- already exists')
        return

    url = DATA_URL + f'{formatted_date}.csv'

    logger.info(f'{formatted_date} -- downloading file: {url}')
    response = requests.get(url)

    assert meets_expectations(response)

    with open(destination_file, 'w') as fh:
        fh.write(response.text)

    logger.info(f'{formatted_date} -- saved to {destination_file}')


def meets_expectations(response):
    """check that the downloaded data looks like a CSV and has the expected columns"""
    try:
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text), nrows=5)
    except Exception as e:
        logger.exception(f'This file doesn\'t look right. Raised error: {str(e)}')
        return False

    return True


def combine_files(raw_path):
    data = None

    for file in sorted(raw_path.glob('*.csv')):
        df = read_single_day(file)
        if data is None:
            data = df
        else:
            data = pd.concat([data, df])

    logger.info(f'Loaded {len(data)} records over period from {data["date"].min()} to {data["date"].max()}')
    logger.info(f'Sample rows\n{data.sample(n=10)}')

    return data.reset_index(drop=True)


def read_single_day(file) -> pd.DataFrame:
    df = pd \
        .read_csv(file) \
        .rename(columns=COLUMN_MAP) \
        .replace({'country': COUNTRY_MAP}) \
        .groupby('country', as_index=False) \
        .sum() \
        .assign(date=pd.to_datetime(file.name.strip('*.csv'), format='%m-%d-%Y')) \
        .loc[:, COLUMNS]

    logger.info(f'Read {file.name}')

    return df


def get_args(args_list=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Download Johns Hopkins COVID-19 case data and compile to single file.')

    parser.add_argument('--start', help='starting date in YYYY-MM-DD format', default='2020-01-22')
    parser.add_argument('--end', help='ending date, also in YYYY-MM-DD format', default=yesterday())
    parser.add_argument('-o', '--overwrite', action='store_true', default=False, 
                        help='overwrite files in the output directory with the same name')
    parser.add_argument('--raw-data-path', type=str, nargs='?', default='data/raw', help='path to save the individual daily updates')
    parser.add_argument('output', type=str, nargs='?', default='data/processed', help='path to save the final, combined data set')

    return parser.parse_args(args_list)


def yesterday():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    return yesterday.date()


if __name__ == '__main__':
    args = get_args()

    main(args.start, args.end, args.raw_data_path, args.output, args.overwrite)
