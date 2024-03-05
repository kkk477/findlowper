from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    create_at = Column(DateTime, nullable=False)