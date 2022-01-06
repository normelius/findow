

import pandas as pd
import requests
import numpy as np
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
from datetime import datetime


# Package imports
from findow.search import search

def historical(symbol_id: int, from_date: str, to_date: str) -> pd.DataFrame:
  """
  Retrieves historical data from a given symbol id. These ids can be obtained using
  the findow.search function.

  :param symbol_id: Specify what id the data should be retrieved for, e.g., 1173182.
  :param from_date: Specify from what date the historical data should be retrieved.
    Should be specified as '2021-01-01'.
  :param to_date: Specify to what date the historical data should be retrieved.
    Should be specified as '2021-01-01'.
  :returns: A dataframe containing historical prices.
  """

  if not isinstance(symbol_id, int):
    raise TypeError("Parameter 'symbol_id' must be an int.")
    
  # Assert dates are specified on the correct format.
  date_format = "%Y-%m-%d"
  try:
    from_date = datetime.strptime(from_date, date_format).strftime("%m/%d/%Y")
    to_date = datetime.strptime(to_date, date_format).strftime("%m/%d/%Y")

  except ValueError:
    raise ValueError("'from_date' and 'to_date' needs to be on the format 'YYYY-MM-DD'")

  url = "https://www.investing.com/instruments/HistoricalDataAjax"

  params = {
    "curr_id": symbol_id,
    "smlID": str(np.random.randint(10000, 99999999)),
    "header": "",
    "st_date": from_date,
    "end_date": to_date,
    "interval_sec": "Daily",
    "sort_col": "date",
    "sort_ord": "DESC",
    "action": "historical_data",
  }
  
  headers = {
    "User-Agent": generate_user_agent(),
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "text/html",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
  }
    
  try:
    response =  requests.post(url, headers = headers, data = params)
    response.raise_for_status()

  except requests.exceptions.HTTPError as error:
    raise ValueError(error)
    
  soup = BeautifulSoup(response.text, features = "lxml")
  table = soup.find_all("table")
  out = pd.read_html(str(table))[0]
  # Todo: Should return an empty dataframe here in case no result is found.
  
  out["Date"] = pd.to_datetime(out.Date)
  
  if "Change %" in out:
    del out["Change %"]

  if 'Vol.' in out:
    # Remove delimiters so .map(pd.eval) below works.
    out['Vol.'] = out['Vol.'].str.replace(',','')

    # Transform volume to integers from string representation.
    out['Vol.'] = out['Vol.'].replace({"K": "*1e3", "M": "*1e6", "B": "*1e9", "-": "0"}, 
        regex = True)
    out['Vol.'] = out['Vol.'].map(pd.eval).astype(int)

    out = out.rename(columns = {'Vol.':'Volume'})

  # Reverse it so we get latest price at the bottom.
  out = out.iloc[::-1]
  out.reset_index(drop = True, inplace = True)
  return out


def main():
  df = historical(1173182, from_date = "2010-01-01", to_date = "2022-01-01")
  #print(df.tail().to_markdown())



if __name__ == '__main__':
    main()

