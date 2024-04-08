from http import HTTPStatus

from fastapi import FastAPI, APIRouter, Depends, HTTPException
import pandas_datareader.data as web
import pandas as pd
import FinanceDataReader as fdr
import yfinance as yf
import json

from database import get_db
from datetime import datetime
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
        ticker_yf.history(period='99y')
        info = ticker_yf.info
        per = info.get('trailingPE')
        fwd_per = info.get('forwardPE')
        pbr = info.get('priceToBook')
        roe = info.get('returnOnEquity')
        current_ratio = info.get('currentRatio')
        quick_ratio = info.get('quickRatio')

        if per == 'Infinity' or per is None or float(per) <= 0:
            continue

        if fwd_per == 'Infinity' or fwd_per is None or float(fwd_per) <= 0:
            continue

        if pbr == 'Infinity' or pbr is None or float(pbr) <= 0:
            continue

        if roe == 'Infinity' or roe is None or float(roe) <= 0:
            continue

        if current_ratio == 'Infinity' or current_ratio is None or float(current_ratio) <= 0:
            continue

        if quick_ratio == 'Infinity' or quick_ratio is None or float(quick_ratio) <= 0:
            continue

        if not rawstatistics_crud.is_rawstatistic(db, ticker.ticker):
            rawstatistics_crud.create_rawstatistics(db, ticker.ticker, per, fwd_per, pbr, roe, current_ratio, quick_ratio)

    return 'a'

@app.get("/recommendations/{ticker}")
def get_recommendations(ticker: str, db: Session = Depends(get_db)):
    rawstatistic_per = rawstatistics_crud.get_rawstatistic_per(db)
    per_mean = pd.Series(rawstatistic_per).mean(axis=0)
    per_std = pd.Series(rawstatistic_per).std(axis=0)
    return per_std

@app.get("/do/refine")
def do_refine(db: Session = Depends(get_db)):
    rowdatas = rawstatistics_crud.get_all_rawstatistic(db)
    rawstatistic_per = rawstatistics_crud.get_rawstatistic_per(db)
    rawstatistic_fwdper = rawstatistics_crud.get_rawstatistic_fwdper(db)
    rawstatistic_pbr = rawstatistics_crud.get_rawstatistic_pbr(db)
    rawstatistic_roe = rawstatistics_crud.get_rawstatistic_roe(db)
    rawstatistic_current = rawstatistics_crud.get_rawstatistic_current(db)
    rawstatistic_quick = rawstatistics_crud.get_rawstatistic_quick(db)

    per_max = pd.Series(rawstatistic_per).max()
    per_min = pd.Series(rawstatistic_per).min()
    fwdper_max = pd.Series(rawstatistic_fwdper).max()
    fwdper_min = pd.Series(rawstatistic_fwdper).min()

    pbr_max = pd.Series(rawstatistic_pbr).max()
    pbr_min = pd.Series(rawstatistic_pbr).min()

    roe_max = pd.Series(rawstatistic_roe).max()
    roe_min = pd.Series(rawstatistic_roe).min()

    current_max = pd.Series(rawstatistic_current).max()
    current_min = pd.Series(rawstatistic_current).min()

    quick_max = pd.Series(rawstatistic_quick).max()
    quick_min = pd.Series(rawstatistic_quick).min()

    for rowdata in rowdatas:
        normalized_per = (float(rowdata.per) - per_min) / (per_max - per_min)
        normalized_fwdper = (float(rowdata.forward_per) - fwdper_min) / (fwdper_max - fwdper_min)
        normalized_pbr = (float(rowdata.pbr) - pbr_min) / (pbr_max - pbr_min)
        normalized_roe = (float(rowdata.roe) - roe_min) / (roe_max - roe_min)
        normalized_current = (float(rowdata.current_ratio) - current_min) / (current_max - current_min)
        normalized_quick = (float(rowdata.quick_ratio) - quick_min) / (quick_max - quick_min)
        refinedstatistics_crud.create_refinedstatistic(db, rowdata.ticker, normalized_per,
                                                       normalized_fwdper,
                                                       normalized_pbr, normalized_roe, rowdata.current_ratio, rowdata.quick_ratio)

    return 'ㅁ'

@app.get("/do/join")
def do_join(db: Session = Depends(get_db)):
    refinedstatistic_per = pd.DataFrame(refinedstatistics_crud.get_refinedstatistic_per(db)).quantile(0.3)
    refinedstatistic_fwdper = pd.DataFrame(refinedstatistics_crud.get_refinedstatistic_fwdper(db)).quantile(0.3)
    refinedstatistic_pbr = pd.DataFrame(refinedstatistics_crud.get_refinedstatistic_pbr(db)).quantile(0.3)
    refinedstatistic_roe = pd.DataFrame(refinedstatistics_crud.get_refinedstatistic_roe(db)).quantile(0.7)

    a=len(refinedstatistics_crud.find_recommendations(db, refinedstatistic_per.get(0), refinedstatistic_fwdper.get(0),
                                                      refinedstatistic_pbr.get(0), refinedstatistic_roe.get(0)))
    print(a)
    return refinedstatistics_crud.find_recommendations(db, refinedstatistic_per.get(0), refinedstatistic_fwdper.get(0), refinedstatistic_pbr.get(0), refinedstatistic_roe.get(0))