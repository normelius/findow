# FinDow

FinDow is a package for financial data retrieval from [investing.com](investing). By utilizing their search functionality, it is fully possible to obtain historical data from all stocks, indices, ETFs, cryptocurrencies, bonds, certificates and commodities.

## Installation

Clone the package

```bash
git clone https://github.com/normelius/findow.git
```
and then install with
```bash
python3 setup.py install
```

## Usage
The whole package evolves around using symbol ids for different quotes. The easiest way to retrieve these is by running.

```python
>>> import findow as fd

>>> df = fd.search("shiba inu")
>>> print(df)
```

```
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|    | description               | symbol   |      id | exchange      | type                  | flag      |
+====+===========================+==========+=========+===============+=======================+===========+
|  0 | SHIBA INU US Dollar       | SHIB/USD | 1173182 | Huobi         | FX - Huobi            | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  1 | SHIBA INU Euro            | SHIB/EUR | 1173274 | Synthetic     | FX - Synthetic        | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  2 | SHIBA INU Indian Rupee    | SHIB/INR | 1175019 | Bitbns        | FX - Bitbns           | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  3 | SHIBA INU Brazil Real     | SHIB/BRL | 1175058 | Binance       | FX - Binance          | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  4 | SHIBA INU Turkish Lira    | SHIB/TRY | 1178980 | Binance       | FX - Binance          | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  5 | SHIBA INU Canadian Dollar | SHIB/CAD | 1183036 | Synthetic     | FX - Synthetic        | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  6 | SHIBA INU                 | SHIB/USD | 1177506 | Investing.com | Index - Investing.com | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
|  7 | SHIBA INU US Dollar       | SHIB/USD | 1173198 | Binance       | FX - Binance          | shiba_inu |
+----+---------------------------+----------+---------+---------------+-----------------------+-----------+
```

When the symbol has been obtained, historical data can be fetched with
```python
>>> import findow as fd

>>> df = fd.historical(1173182, from_date = "2020-01-01", to_date = "2022-01-01")
>>> print(df)
````

```
+-----+---------------------+-----------+-----------+-----------+-----------+----------------+
|     | Date                |     Price |      Open |      High |       Low |         Volume |
+=====+=====================+===========+===========+===========+===========+================+
| 230 | 2021-12-28 00:00:00 | 3.488e-05 | 3.905e-05 | 3.905e-05 | 3.422e-05 | 11630270000000 |
+-----+---------------------+-----------+-----------+-----------+-----------+----------------+
| 231 | 2021-12-29 00:00:00 | 3.366e-05 | 3.496e-05 | 3.626e-05 | 3.312e-05 |  7524480000000 |
+-----+---------------------+-----------+-----------+-----------+-----------+----------------+
| 232 | 2021-12-30 00:00:00 | 3.377e-05 | 3.366e-05 | 3.434e-05 | 3.299e-05 |  5913650000000 |
+-----+---------------------+-----------+-----------+-----------+-----------+----------------+
| 233 | 2021-12-31 00:00:00 | 3.338e-05 | 3.373e-05 | 3.462e-05 | 3.266e-05 |  5588730000000 |
+-----+---------------------+-----------+-----------+-----------+-----------+----------------+
| 234 | 2022-01-01 00:00:00 | 3.415e-05 | 3.343e-05 | 3.417e-05 | 3.336e-05 |  3309140000000 |
+-----+---------------------+-----------+-----------+-----------+-----------+----------------+



```
## License
[MIT](https://choosealicense.com/licenses/mit/)
