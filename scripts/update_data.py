import argparse
from io import StringIO
from pathlib import Path
from datetime import date, datetime, timedelta
import logging


import pandas as pd
import requests


logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)

DATA_URL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'


def main(start, end, output_dir, overwrite=True):

    path = Path(output_dir).absolute()

    if not path.exists():
        logger.error(f'Path "{output_dir}" doesn\'t exist. Create the directory and try again.')
        raise IOError(f'No such directory: {path}')

    logger.info(f'Downloading data for {start} - {end} to {str(path)}')

    if overwrite:
        logger.info(f'Overwrite={overwrite}')

    dates = pd.date_range(start, end, freq='D')

    for date in dates:
        download_single_day(date, path, overwrite)


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


def get_args(args_list=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Download Johns Hopkins COVID-19 case data.')

    parser.add_argument('--start', help='starting date in YYYY-MM-DD format', default='2020-01-22')
    parser.add_argument('--end', help='ending date, also in YYYY-MM-DD format', default=yesterday())
    parser.add_argument('-o', '--overwrite', action='store_true', default=False, 
                        help='overwrite files in the output directory with the same name')
    parser.add_argument('output', type=str, nargs='?', default='data/original', help='path to save the data')

    return parser.parse_args(args_list)


def yesterday():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    return yesterday.date()


if __name__ == '__main__':
    args = get_args()

    main(args.start, args.end, args.output, args.overwrite)
