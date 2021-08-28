import pandas as pd
import numpy
import mplfinance as mpf
import yfinance as yf

#take from form
# 1. fsymbol
# 2.   type of fgraph
#     - OHLC                = default  
#     - Candlestick charts, = cande
#     - Colored Bar,        = renko 
#     - Vertex Line         = line

def func(fsymbol, charttype):

    filename = "static/sto.png"

    df = pd.read_json("StockoList.json")

    df.set_index('date')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df.index = pd.DatetimeIndex(df['date'])

    dk = df.loc[df['symbol']==fsymbol]

    if charttype != "":
        mpf.plot(dk, type = charttype, savefig=filename)

    else:
        mpf.plot(dk, savefig=filename)

    #mpf.plot(df["2020-12-01":],type="candle")




    #TICKER = "AAPL"

    #df = yf.download(TICKER, 
                    # start="2020-07-01", 
                    #end="2020-12-31", 
                    #auto_adjust=True)

