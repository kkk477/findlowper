from datetime import datetime
from sqlalchemy.orm import Session
from models import BalanceSheets

def create_balance_sheets(db: Session, ticker: str, timestamp: str, _balance_sheet: dict):
    db_balance_sheet = BalanceSheets(
        ticker=ticker,

        treasury_shares_number = _balance_sheet.get('Treasury Shares Number'),
        ordinary_shares_number = _balance_sheet.get('Ordinary Shares Number'),
        share_issued = _balance_sheet.get('Share Issued'),
        total_debt = _balance_sheet.get('Total Debt'),
        tangible_book_value = _balance_sheet.get('Tangible Book Value'),
        invested_capital = _balance_sheet.get('Invested Capital'),
        working_capital = _balance_sheet.get('Working Capital'),
        net_tangible_assets = _balance_sheet.get('Net Tangible Assets'),
        capital_lease_obligations = _balance_sheet.get('Capital Lease Obligations'),
        common_stock_equity = _balance_sheet.get('Common Stock Equity'),
        total_capitalization = _balance_sheet.get('Total Capitalization'),
        total_equity_gross_minority_interest = _balance_sheet.get('Total Equity Gross Minority Interest'),
        stockholders_equity = _balance_sheet.get('Stockholders Equity'),
        gains_losses_not_affecting_retained_earnings = _balance_sheet.get('Gains Losses Not Affecting Retained Earnings'),
        other_equity_adjustments = _balance_sheet.get('Other Equity Adjustments'),
        retained_earnings = _balance_sheet.get('Retained Earnings'),
        additional_paid_in_capital = _balance_sheet.get('Additional Paid In Capital'),
        capital_stock = _balance_sheet.get('Capital Stock'),
        common_stock = _balance_sheet.get('Common Stock'),
        total_liabilities_net_minority_interest = _balance_sheet.get('Total Liabilities Net Minority Interest'),
        total_non_current_liabilities_net_minority_interest = _balance_sheet.get('Total Non Current Liabilities Net Minority Interest'),
        other_non_current_liabilities = _balance_sheet.get('Other Non Current Liabilities'),
        tradeand_other_payables_non_current = _balance_sheet.get('Tradeand Other Payables Non Current'),
        long_term_debt_and_capital_lease_obligation = _balance_sheet.get('Long Term Debt And Capital Lease Obligation'),
        long_term_capital_lease_obligation = _balance_sheet.get('Long Term Capital Lease Obligation'),
        long_term_debt = _balance_sheet.get('Long Term Debt'),
        current_liabilities = _balance_sheet.get('Current Liabilities'),
        other_current_liabilities = _balance_sheet.get('Other Current Liabilities'),
        current_debt_and_capital_lease_obligation = _balance_sheet.get('Current Debt And Capital Lease Obligation'),
        current_capital_lease_obligation = _balance_sheet.get('Current Capital Lease Obligation'),
        pensionand_other_post_retirement_benefit_plans_current = _balance_sheet.get('Pensionand Other Post Retirement Benefit Plans Current'),
        payables_and_accrued_expenses = _balance_sheet.get('Payables And Accrued Expenses'),
        current_accrued_expenses = _balance_sheet.get('Current Accrued Expenses'),
        payables = _balance_sheet.get('Payables'),
        dueto_related_parties_current = _balance_sheet.get('Dueto Related Parties Current'),
        total_tax_payable = _balance_sheet.get('Total Tax Payable'),
        accounts_payable = _balance_sheet.get('Accounts Payable'),
        total_assets = _balance_sheet.get('Total Assets'),
        total_non_current_assets = _balance_sheet.get('Total Non Current Assets'),
        other_non_current_assets = _balance_sheet.get('Other Non Current Assets'),
        investments_and_advances = _balance_sheet.get('Investments And Advances'),
        investmentin_financial_assets = _balance_sheet.get('Investmentin Financial Assets'),
        available_for_sale_securities = _balance_sheet.get('Available For Sale Securities'),
        goodwill_and_other_intangible_assets = _balance_sheet.get('Goodwill And Other Intangible Assets'),
        other_intangible_assets = _balance_sheet.get('Other Intangible Assets'),
        goodwill = _balance_sheet.get('Goodwill'),
        net_ppe = _balance_sheet.get('Net PPE'),
        accumulated_depreciation = _balance_sheet.get('Accumulated Depreciation'),
        gross_ppe = _balance_sheet.get('Gross PPE'),
        leases = _balance_sheet.get('Leases'),
        construction_in_progress = _balance_sheet.get('Construction In Progress'),
        other_properties = _balance_sheet.get('Other Properties'),
        buildings_and_improvements = _balance_sheet.get('Buildings And Improvements'),
        land_and_improvements = _balance_sheet.get('Land And Improvements'),
        properties = _balance_sheet.get('Properties'),
        current_assets = _balance_sheet.get('Current Assets'),
        other_current_assets = _balance_sheet.get('Other Current Assets'),
        receivables = _balance_sheet.get('Receivables'),
        accounts_receivable = _balance_sheet.get('Accounts Receivable'),
        cash_cash_equivalents_and_short_term_investments = _balance_sheet.get('Cash Cash Equivalents And Short Term Investments'),
        other_short_term_investments = _balance_sheet.get('Other Short Term Investments'),
        cash_and_cash_equivalents = _balance_sheet.get('Cash And Cash Equivalents'),
        cash_equivalents = _balance_sheet.get('Cash Equivalents'),
        cash_financial = _balance_sheet.get('Cash Financial'),

        modified_at=datetime.fromtimestamp(int(timestamp) / 1000))

    db.add(db_balance_sheet)
    db.commit()

def get_balance_sheets(db: Session, ticker: str):
    return db.query(BalanceSheets).filter(BalanceSheets.ticker == ticker).first()

def is_balance_sheets(db: Session, ticker: str, timestamp: str):
    return db.query(BalanceSheets).filter(ticker == BalanceSheets.ticker, BalanceSheets.modified_at == datetime.fromtimestamp(int(
        timestamp) / 1000)).first()