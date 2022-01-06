
import findow as fd

def main():
  df = fd.search("shiba inu")
  print(df)
  df_historical = fd.historical(1173182, "2010-01-01", "2022-01-01")
  print(df_historical)



if __name__ == '__main__':
    main()

