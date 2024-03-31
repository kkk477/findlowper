from datetime import datetime

from sqlalchemy.orm import Session

from models import IncomeStatements

def create_incomestatements(db: Session, ticker: str, timestamp: str, _income_statement: dict):
    db_incomestatement = IncomeStatements(
        ticker=ticker,
        total_revenue=_income_statement.get('Total Revenue'),
        operating_revenue=_income_statement.get('Operating Revenue'),
        cost_of_revenue=_income_statement.get('Cost Of Revenue'),
        gross_profit=_income_statement.get('Gross Profit'),
        operating_expense=_income_statement.get('Operating Expense'),
        selling_general_and_administrative=_income_statement.get('Selling General And Administration'),
        general_and_administrative_expense=_income_statement.get('General And Administrative Expense'),
        selling_and_marketing_expense=_income_statement.get('Selling And Marketing Expense'),
        other_general_and_administrative=_income_statement.get('Other Gand A'),
        research_and_development=_income_statement.get('Research And Development'),
        operating_income=_income_statement.get('Operating Income'),
        net_non_operating_interest_income_expense=_income_statement.get('Net Non Operating Interest Income Expense'),
        interest_income_non_operating=_income_statement.get('Interest Income Non Operating'),
        interest_expense_non_operating=_income_statement.get('Interest Expense Non Operating'),
        total_other_finance_cost=_income_statement.get('Total Other Finance Cost'),
        other_income_expense=_income_statement.get('Other Income Expense'),
        gain_on_sale_of_security=_income_statement.get('Gain on Sale Of Security'),
        other_non_operating_income_expenses=_income_statement.get('Other Non Operating Income Expenses'),
        pretax_income=_income_statement.get('Pretax Income'),
        tax_provision=_income_statement.get('Tax Provision'),
        net_income_common_stockholders=_income_statement.get('Net Income Common Stockholders'),
        net_income=_income_statement.get('Net Income'),
        net_income_including_noncontrolling_interests=_income_statement.get('Net Income Including Noncontrolling Interests'),
        net_income_continuous_operations=_income_statement.get('Net Income Continuous Operations'),
        average_dilution_earnings=_income_statement.get('Average Dilution Earnings'),
        diluted_ni_available_to_come_stockholders=_income_statement.get('Diluted NI Availto Com Stockholders'),
        basic_eps=_income_statement.get('Basic EPS'),
        diluted_eps=_income_statement.get('Diluted EPS'),
        basic_average_shares=_income_statement.get('Basic Average Shares'),
        diluted_average_shares=_income_statement.get('Diluted Average Shares'),
        total_operating_income_as_reported=_income_statement.get('Total Operating Income As Reported'),
        total_expenses=_income_statement.get('Total Expenses'),
        net_income_from_continuing_and_discontinued_operation=_income_statement.get('Net Income From Continuing And Discontinued Operation'),
        normalized_income=_income_statement.get('Normalized Income'),
        interest_income=_income_statement.get('Interest Income'),
        interest_expense=_income_statement.get('Interest Expense'),
        net_interest_income=_income_statement.get('Net Interest Income'),
        ebit=_income_statement.get('EBIT'),
        ebitda=_income_statement.get('EBITDA'),
        reconciled_cost_of_revenue=_income_statement.get('Reconciled Cost Of Revenue'),
        reconciled_depreciation=_income_statement.get('Reconciled Depreciation'),
        net_income_from_continuing_operation_net_minority_interest=_income_statement.get(
            'Net Income From Continuing Operation Net Minority Interest'),
        total_unusual_items_excluding_goodwill=_income_statement.get('Total Unusual Items Excluding Goodwill'),
        total_unusual_items=_income_statement.get('Total Unusual Items'),
        normalized_ebitda=_income_statement.get('Normalized EBITDA'),
        tax_rate_for_calcs=_income_statement.get('Tax Rate For Calcs'),
        tax_effect_of_unusual_items=_income_statement.get('Tax Effect Of Unusual Items'),
        modified_at=datetime.fromtimestamp(int(timestamp)/1000))

    db.add(db_incomestatement)
    db.commit()

def get_incomestatements(db: Session, ticker: str):
    return db.query(IncomeStatements).filter(IncomeStatements.ticker == ticker).first()

def is_incomestatements(db: Session, ticker: str, timestamp: str):
    return db.query(IncomeStatements).filter(ticker == IncomeStatements.ticker, IncomeStatements.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()