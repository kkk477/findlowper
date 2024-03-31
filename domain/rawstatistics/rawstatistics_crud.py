from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from models import Rawstatistics

def create_rawstatistics(db: Session, ticker: str, per: str, fwd_per: str, pbr: str, roe: str, current_ratio: str,
                         quick_ratio: str):
    db_rawstatistics = Rawstatistics(
        ticker=ticker,
        modified_at=datetime.today(),
        per=per,
        forward_per=fwd_per,
        pbr=pbr,
        roe=roe,
        current_ratio=current_ratio,
        quick_ratio=quick_ratio)

    db.add(db_rawstatistics)
    db.commit()
    print(ticker)

def get_rawstatistic(db: Session, ticker: str):
    return db.query(Rawstatistics).order_by(Rawstatistics.modified_at.desc()).filter(Rawstatistics.ticker == ticker).all()

def is_rawstatistic(db: Session, ticker: str):
    result = db.query(Rawstatistics).filter(ticker == Rawstatistics.ticker, Rawstatistics.modified_at ==
                                   datetime.today()).count()
    if result > 0:
        print('true')
        return True
    else:
        print('false')
        return False