from http import HTTPStatus

from fastapi import FastAPI, APIRouter, Depends, HTTPException
import pandas_datareader.data as web
import pandas as pd
import FinanceDataReader as fdr
import yfinance as yf
import json

from database import get_db
from sqlalchemy.orm import Session
from domain.tickers import tickers_crud
from domain.incomestatements import incomestatements_crud
from domain.balancesheets import balancesheets_crud
from domain.cashflows import cashflows_crud
from models import Tickers

app = FastAPI()

@app.get("/tickers")
def get_tickers(db: Session = Depends(get_db)):
    try:
        yf.pdr_override()

        nasdaq = fdr.StockListing('NASDAQ')
        df = pd.concat([nasdaq])

        for i in range(0, 15):
            ticker = df['Symbol'][i]
        name = df['Name'][i]
        industryCode = df['IndustryCode'][i]
        industry = df['Industry'][i]

        getResult = tickers_crud.get_tickers(db, ticker)
        if getResult is None:
            tickers_crud.create_tickers(db, ticker, name, industryCode, industry)

        return {
            'result': 'OK'
        }

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="error")

@app.get("/tickers/{ticker}")
def get_data(ticker: str, db: Session = Depends(get_db)):
    yf.pdr_override()
    ticker_yf = yf.Ticker(ticker)
    print(ticker_yf.quarterly_income_stmt)
    print("===================================")
    print(ticker_yf.quarterly_balance_sheet)
    print("===================================")
    print(ticker_yf.quarterly_cashflow)
    return ticker_yf.quarterly_income_stmt

@app.get("/income/{ticker}")
def get_income(ticker: str, db: Session = Depends(get_db)):
    yf.pdr_override()
    ticker_yf = yf.Ticker(ticker)

    raw = json.loads(ticker_yf.quarterly_income_stmt.to_json())
    keys = list(raw.keys())

    for key in keys:
        quarterly_income_stmt = raw.get(key)
        incomestatements_crud.create_incomestatements(db, ticker=ticker, timestamp=key,
                                                      _income_statement=quarterly_income_stmt)

    return json.loads(ticker_yf.quarterly_income_stmt.to_json())

@app.get("/balance/{ticker}")
def get_balance(ticker: str, db: Session = Depends(get_db)):
    yf.pdr_override()
    ticker_yf = yf.Ticker(ticker)

    raw = json.loads(ticker_yf.quarterly_balance_sheet.to_json())
    keys = list(raw.keys())

    for key in keys:
        quarterly_balance_sheet = raw.get(key)
        balancesheets_crud.create_balance_sheets(db, ticker=ticker, timestamp=key,
                                                 _balance_sheet=quarterly_balance_sheet)

    return json.loads(ticker_yf.quarterly_balance_sheet.to_json())

@app.get("/cashflow/{ticker}")
def get_cashflow(ticker: str, db: Session = Depends(get_db)):
    yf.pdr_override()
    ticker_yf = yf.Ticker(ticker)

    raw = json.loads(ticker_yf.quarterly_cashflow.to_json())
    keys = list(raw.keys())

    for key in keys:
        quarterly_cashflow = raw.get(key)
        cashflows_crud.create_cashflow(db, ticker=ticker, timestamp=key, _cashflow=quarterly_cashflow)

    return json.loads(ticker_yf.quarterly_cashflow.to_json())