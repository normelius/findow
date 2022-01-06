
import findow as fd

def main():
  df = fd.search("USD/SEK")
  print(df)
  df_historical = fd.historical(41, "2010-01-01", "2020-01-01")
  print(df_historical)



if __name__ == '__main__':
    main()

