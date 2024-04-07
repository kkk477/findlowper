from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql import exists
from models import Rawstatistics
from sqlalchemy import select

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
    return [float(ele) for ele in db.query(Rawstatistics).order_by(Rawstatistics.modified_at.desc()).filter(Rawstatistics.ticker == ticker).all()]

def get_all_rawstatistic(db: Session):
    return db.query(Rawstatistics).order_by(Rawstatistics.modified_at.desc()).filter(Rawstatistics.modified_at == '2024-04-04').all()

def get_rawstatistic_per(db: Session):
    stmt = select(Rawstatistics.per).select_from(Rawstatistics).filter(
        Rawstatistics.modified_at == '2024-04-04')
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_rawstatistic_fwdper(db: Session):
    stmt = select(Rawstatistics.forward_per).select_from(Rawstatistics).filter(
        Rawstatistics.modified_at == '2024-04-04')
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_rawstatistic_pbr(db: Session):
    stmt = select(Rawstatistics.pbr).select_from(Rawstatistics).filter(
        Rawstatistics.modified_at == '2024-04-04')
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_rawstatistic_roe(db: Session):
    stmt = select(Rawstatistics.roe).select_from(Rawstatistics).filter(
        Rawstatistics.modified_at == '2024-04-04')
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_rawstatistic_current(db: Session):
    stmt = select(Rawstatistics.current_ratio).select_from(Rawstatistics).filter(
        Rawstatistics.modified_at == '2024-04-04')
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_rawstatistic_quick(db: Session):
    stmt = select(Rawstatistics.quick_ratio).select_from(Rawstatistics).filter(
        Rawstatistics.modified_at == '2024-04-04')
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def is_rawstatistic(db: Session, ticker: str):
    result = db.query(Rawstatistics).filter(ticker == Rawstatistics.ticker, Rawstatistics.modified_at ==
                                   datetime.today()).count()
    if result > 0:
        print('true')
        return True
    else:
        print('false')
        return False