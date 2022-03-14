
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
from os import listdir, remove


class Data_Api():

    """ csv_list()
        - walks local dir and compiles list of csv files
        Input:
        Output:
            list if csv file names
    """

    def csv_list(self):
        files = [f.split('.')[0] for f in listdir('.') if '.csv' in f]

        if(len(files) > 0):
            file_list = [{'label': x, 'value': x}
                         for x in sorted(files)]
            return file_list

        return [{'label': 'Download Data', 'value': 'Download Data'}]

    """ pull_ticker_data(symbol, start, end)
        - Pulls ticker data from yahoo finance
        Input:
            ticker symbol, start date, end date (date format as string, ex. "2022-01-20")
        Output:
            dataframe   
    """

    def pull_ticker_data(self, symbol, t_range):

        yf.pdr_override()
        df = pdr.get_data_yahoo(symbol, period=t_range).reset_index()
        df['Date'] = pd.to_datetime(df['Date']).dt.date
        return df, symbol

    """write_csv(df, symbol)
        - writes dataframe to csv in local dir.
        Input: 
            dataframe containing ticker data, ticker symbol 
        Output:
            ticker symbol
    """

    def write_csv(self, df, symbol):

        if df.empty:
            return False

        start = df['Date'].max()
        end = df['Date'].min()
        file_name = f'{symbol} - {start} - thru - {end}.csv'
        df.to_csv(f'{file_name}', index=False)
        return True

    """load_csv(symbol)
        - loads csv ticker data into dataframe
        Input:
            ticker symbol
        Output:
            dataframe
    """

    def load_csv(self, file_name):

        df = pd.read_csv(f"{file_name}.csv")
        return df

    """remove_csv(symbol)
        - removes csv file from directory
        Input:
            file name
        Output:
            boolean, true for success, false for file not found
    """

    def remove_csv(self, symbol):

        try:
            remove(f'{symbol}.csv')
            return True

        except:
            return False
