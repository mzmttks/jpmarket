import datetime
import time

import jsm

import pandas.compat as compat


def DataReader(name, data_source=None, start=None, end=None,
               retry_count=3, pause=0.001):
    """
    [Docstring is compatible with
     https://github.com/pydata/pandas/blob/master/pandas/io/data.py]

    Imports data from Japanese market data sources.
    Currently supports Yahoo! Finance Japan.
 
    Parameters
    ----------
    name : str or list of strs
        the name of the dataset. Some data sources (yahoo, google, fred) will
        accept a list of names.
    data_source: str
        the data source ("yahoojp")
    start : {datetime, None}
        left boundary for range (defaults to 1/1/2010)
    end : {datetime, None}
        right boundary for range (defaults to today)

    Examples
    ----------

    # Data from Yahoo! Finance Japan (Toyota)
    toyota = DataReader("7203", "yahoojp")
    """

    if data_source == "yahoojp":
        return get_data_yahoojp(symbols=name, start=start, end=end,
                                adjust_price=False, chunksize=25,
                                retry_count=retry_count, pause=pause)

def _sanitize_dates(start, end):
    from pandas.core.datetools import to_datetime
    start = to_datetime(start)
    end = to_datetime(end)
    if start is None:
        start = dt.datetime(2010, 1, 1)
    if end is None:
        end = dt.datetime.today()
    return start, end

def get_data_yahoojp(symbols=None, start=None, end=None, retry_count=3,
                     pause=0.001, adjust_price=False, ret_index=False,
                     chunksize=25):
    q = jsm.Quotes() 
    if not isinstance(symbols, list):
        symbols = [symbols]

    for i, s in enumerate(symbols):
        try:
            symbols[i] = int(s)
        except:
            raise exceptions.ValueError("symbols must be an integer")

    prices = []
    for symbol in symbols:
        prices.append(
            q.get_historical_prices(symbol, start_date=start, end_date=end)
        )
    return prices
