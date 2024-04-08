from datetime import datetime
from sqlalchemy.orm import Session
from models import Refinedstatistics
from sqlalchemy import select

def create_refinedstatistic(db: Session, ticker: str, per: str, fwd_per: str, pbr: str, roe: str, current_ratio: str,
                            quick_ratio: str):
    db_refinedstatistic = Refinedstatistics(
        ticker=ticker,
        modified_at=datetime.today(),
        refined_per=per,
        refined_forward_per=fwd_per,
        refined_pbr=pbr,
        refined_roe=roe,
        current_ratio=current_ratio,
        quick_ratio=quick_ratio)

    db.add(db_refinedstatistic)
    db.commit()

def get_refinedstatistic(db: Session, ticker: str):
    return db.query(Refinedstatistics).order_by(Refinedstatistics.modified_at.desc()).filter(Refinedstatistics.ticker == ticker).all()

def is_refinedstatistic(db: Session, ticker: str, timestamp: str):
    return db.query(Refinedstatistics).filter(ticker == Refinedstatistics.ticker, Refinedstatistics.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()

def find_recommendations(db: Session, refined_per, refined_forward_per, refined_pbr, refined_roe):
    stmt = (select(Refinedstatistics)
            .select_from(Refinedstatistics)
            .filter(Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d")
                    , Refinedstatistics.refined_per <= refined_per
                    , Refinedstatistics.refined_forward_per <= refined_forward_per
                    , Refinedstatistics.refined_pbr <= refined_pbr
                    , Refinedstatistics.refined_roe >= refined_roe
                    , Refinedstatistics.current_ratio >= 2.0
                    , Refinedstatistics.quick_ratio >= 1.0))
    return db.execute(stmt).scalars().all()

def get_refinedstatistic_per(db: Session):
    stmt = select(Refinedstatistics.refined_per).select_from(Refinedstatistics).filter(
        Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d"))
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_refinedstatistic_fwdper(db: Session):
    stmt = select(Refinedstatistics.refined_forward_per).select_from(Refinedstatistics).filter(
        Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d"))
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_refinedstatistic_pbr(db: Session):
    stmt = select(Refinedstatistics.refined_pbr).select_from(Refinedstatistics).filter(
        Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d"))
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_refinedstatistic_roe(db: Session):
    stmt = select(Refinedstatistics.refined_roe).select_from(Refinedstatistics).filter(
        Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d"))
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_refinedstatistic_current(db: Session):
    stmt = select(Refinedstatistics.current_ratio).select_from(Refinedstatistics).filter(
        Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d"))
    return [float(ele) for ele in db.execute(stmt).scalars().all()]

def get_refinedstatistic_quick(db: Session):
    stmt = select(Refinedstatistics.quick_ratio).select_from(Refinedstatistics).filter(
        Refinedstatistics.modified_at == datetime.today().strftime("%Y-%m-%d"))
    return [float(ele) for ele in db.execute(stmt).scalars().all()]