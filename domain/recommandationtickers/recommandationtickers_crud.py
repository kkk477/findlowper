from datetime import datetime
from sqlalchemy.orm import Session
from models import Recommandationtickers

def create_rawstatistics(db: Session, ticker: str, timestamp: str, per: str, fwd_per: str, pbr: str, roe: str,
                         current_ratio: str, quick_ratio: str):
    db_recommandationtickers = Recommandationtickers(
        ticker=ticker,
        modified_at=datetime.fromtimestamp(int(timestamp) / 1000),
        recommandation_per=per,
        recommandation_forward_per=fwd_per,
        recommandation_pbr=pbr,
        recommandation_roe=roe,
        current_ratio=current_ratio,
        quick_ratio=quick_ratio)

    db.add(db_recommandationtickers)
    db.commit()

def get_rawstatistic(db: Session, ticker: str):
    return db.query(Recommandationtickers).order_by(Recommandationtickers.modified_at.desc()).filter(Recommandationtickers.ticker == ticker).all()

def is_rawstatistic(db: Session, ticker: str, timestamp: str):
    return db.query(Recommandationtickers).filter(ticker == Recommandationtickers.ticker , Recommandationtickers.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()