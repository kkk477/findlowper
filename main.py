from http import HTTPStatus

from fastapi import FastAPI, APIRouter, Depends, HTTPException
import pandas_datareader.data as web
import pandas as pd
import FinanceDataReader as fdr
import yfinance as yf
import json

from database import get_db
from starlette import status
from sqlalchemy.orm import Session
from domain.tickers import tickers_crud
from domain.incomestatements import incomestatements_crud
from domain.balancesheets import balancesheets_crud
from domain.cashflows import cashflows_crud
from domain.rawstatistics import rawstatistics_crud
from domain.refinedstatistics import refinedstatistics_crud
from domain.recommandationtickers import recommandationtickers_crud
from models import Tickers

app = FastAPI()

@app.get("/tickers")
def get_tickers(db: Session = Depends(get_db)):
    try:
        yf.pdr_override()

        nasdaq = fdr.StockListing('NASDAQ')
        df = pd.concat([nasdaq])
        num_of_rows = len(df['Symbol'])

        for i in range(0, num_of_rows):
            ticker = df['Symbol'][i]
            name = df['Name'][i]
            industryCode = df['IndustryCode'][i]
            industry = df['Industry'][i]
            getResult = tickers_crud.get_ticker(db, ticker)
            if not getResult:
                tickers_crud.create_tickers(db=db, ticker=ticker, name=name, industryCode=industryCode, industry=industry)

        return {
            'result': 'OK'
        }

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)

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

    ticker_yf.history(period='max')
    raw = json.loads(ticker_yf.quarterly_cashflow.to_json())
    keys = list(raw.keys())

    for key in keys:
        quarterly_cashflow = raw.get(key)
        db_cashflow = cashflows_crud.is_cashflow(db, ticker=ticker, timestamp=key)
        if not db_cashflow:
            cashflows_crud.create_cashflow(db, ticker=ticker, timestamp=key, _cashflow=quarterly_cashflow)

    return cashflows_crud.get_cashflow(db, ticker=ticker)

@app.get("/recommendations")
def get_recommendations(db: Session = Depends(get_db)):
    yf.pdr_override()
    tickers = tickers_crud.get_tickers(db)

    for ticker in tickers:
        ticker_yf = yf.Ticker(ticker.ticker)
        ticker_yf.history(period='max')
        info = ticker_yf.info
        per = info.get('currentPrice')/info.get('trailingEps')
        fwd_per = info.get('forwardPE')
        pbr = info.get('priceToBook')
        roe = info.get('returnOnEquity')
        current_ratio = info.get('currentRatio')
        quick_ratio = info.get('quickRatio')

        if per == 'Infinity':
            per = 9999999

        if fwd_per == 'Infinity':
            fwd_per = 9999999

        if pbr == 'Infinity':
            pbr = 9999999

        if roe == 'Infinity':
            roe = -99999

        if current_ratio == 'Infinity':
            current_ratio = -99999

        if quick_ratio == 'Infinity':
            quick_ratio = -99999

        if not rawstatistics_crud.is_rawstatistic(db, ticker.ticker):
            rawstatistics_crud.create_rawstatistics(db, ticker.ticker, per, fwd_per, pbr, roe, current_ratio, quick_ratio)

    return 'a'

@app.get("/recommendations/{ticker}")
def get_recommendations(ticker: str, db: Session = Depends(get_db)):
    yf.pdr_override()
    ticker_yf = yf.Ticker(ticker)
    info = ticker_yf.info
    #per = info.get('currentPrice')/info.get('forwardEps')
    return info