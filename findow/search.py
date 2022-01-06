

import requests
import pandas as pd
from user_agent import generate_user_agent


def search(quote: str) -> pd.DataFrame:
  """
  Retrieves information from a search query which contains description about
  possible quotes as well as their symbols and ids, which are useful for querying
  further data, e.g., historical.

  :param quote: A string specifying what to search for, e.g., 'bitcoin'.
  :returns: A pandas dataframe containing all possible retrieved quotes with
    their symbols and ids.
  """
  if not isinstance(quote, str):
    raise TypeError("Parameter 'quote' must be a string.")

  url = "https://api.investing.com/api/search/v2/search?"
  params = {'q': quote}
  headers = {'User-agent': generate_user_agent()}
  
  # Use requets exception handling.
  try:
    response = requests.get(url, params = params, headers = headers)
    response.raise_for_status()

  except requests.exceptions.HTTPError as error:
    print(error)

  data = response.json()
  quotes = data['quotes']

  if not quotes:
    raise ValueError("No quotes found for search term '{}'.".format(quote))
  
  df = pd.DataFrame(quotes)
  del df["url"]

  # More logical ordering of columns.
  df = df[["description", "symbol", "id", "exchange", "type", "flag"]]

  return df


def main():
  df = search("shiba inu")
  #print(df.to_markdown(tablefmt = "grid"))

if __name__ == '__main__':
    main()

