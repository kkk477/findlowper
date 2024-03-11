from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from database import Base


class Tickers(Base):
    __tablename__ = 'tickers'

    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    industry_code = Column(String(100), nullable=False)
    industry = Column(String(100), nullable=False)
    modified_at = Column(DateTime, nullable=True)

class IncomeStatements(Base):
    __tablename__ = 'income_statements'

    id = Column(Integer, primary_key=True)
    ticker = Column(String(10), unique=True, nullable=False)
    total_revenue = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    operating_revenue = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    cost_of_revenue = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    gross_profit = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    selling_general_and_administrative = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    general_and_administrative_expense = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    other_general_and_administrative = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    research_and_development = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    operating_income = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_non_operating_interest_income_expense = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    interest_income_non_operating = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    interest_expense_non_operating = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    total_other_finance_cost = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    other_income_expense = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    gain_on_sale_of_security = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    other_non_operating_income_expenses = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    pretax_income = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_income_common_stockholders = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_income = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_income_including_noncontrolling_interests = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_income_continuous_operations = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    average_dilution_earnings = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    diluted_ni_available_to_come_stockholders = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    basic_eps = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    diluted_eps = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    basic_average_shares = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    diluted_average_shares = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    total_operating_income_as_reported = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    total_expenses = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_income_from_continuing_and_discontinued_operation = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    normalized_income = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    interest_income = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    interest_expense = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_interest_income = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    ebit = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    ebitda = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    reconciled_cost_of_revenue = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    reconciled_depreciation = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    net_income_from_continuing_operation_net_minority_interest = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    total_unusual_items_excluding_goodwill = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    total_unusual_items = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    normalized_ebitda = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    tax_rate_for_calcs = Column(Numeric(precision=20, scale=10), default=0, nullable=False)
    tax_effect_of_unusual_items = Column(Numeric(precision=20, scale=10), default=0, nullable=False)

    modified_at = Column(DateTime, nullable=True)