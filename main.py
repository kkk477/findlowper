from fastapi import FastAPI
from pandas_datareader import data as panda
import yfinance as yf

app = FastAPI()

@app.get("/hello")
def hello():
    yf.pdr_override()
    data = yf.Ticker("TSLA")
    print(data.info)
    return data.info

