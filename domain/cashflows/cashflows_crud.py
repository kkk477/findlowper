from datetime import datetime
from sqlalchemy.orm import Session
from models import Cashflows

def create_cashflow(db: Session, ticker: str, timestamp: str, _cashflow: dict):
    db_cashflow = Cashflows(
        ticker=ticker,

        free_cash_flow = _cashflow.get('Free Cash Flow'),
        repurchase_of_capital_stock = _cashflow.get('Repurchase Of Capital Stock'),
        repayment_of_debt = _cashflow.get('Repayment Of Debt'),
        issuance_of_debt = _cashflow.get('Issuance Of Debt'),
        capital_expenditure = _cashflow.get('Capital Expenditure'),
        interest_paid_supplemental_data = _cashflow.get('Interest Paid Supplemental Data'),
        income_tax_paid_supplemental_data = _cashflow.get('Interest Paid Supplemental Data'),
        end_cash_position = _cashflow.get('End Cash Position'),
        beginning_cash_position = _cashflow.get('Beginning Cash Position'),
        effect_of_exchange_rate_changes = _cashflow.get('Effect Of Exchange Rate Changes'),
        changes_in_cash = _cashflow.get('Changes In Cash'),
        financing_cash_flow = _cashflow.get('Financing Cash Flow'),
        cash_flow_from_continuing_financing_activities = _cashflow.get('Cash Flow From Continuing Financing Activities'),
        net_other_financing_charges = _cashflow.get('Net Other Financing Charges'),
        net_common_stock_issuance = _cashflow.get('Net Common Stock Issuance'),
        common_stock_payments = _cashflow.get('Common Stock Payments'),
        net_issuance_payments_of_debt = _cashflow.get('Net Issuance Payments Of Debt'),
        net_long_term_debt_issuance = _cashflow.get('Net Long Term Debt Issuance'),
        long_term_debt_payments = _cashflow.get('Long Term Debt Payments'),
        long_term_debt_issuance = _cashflow.get('Long Term Debt Issuance'),
        investing_cash_flow = _cashflow.get('Investing Cash Flow'),
        cash_flow_from_continuing_investing_activities = _cashflow.get('Cash Flow From Continuing Investing Activities'),
        net_other_investing_changes = _cashflow.get('Net Other Investing Changes'),
        net_investment_purchase_and_sale = _cashflow.get('Net Investment Purchase And Sale'),
        sale_of_investment = _cashflow.get('Sale Of Investment'),
        purchase_of_investment = _cashflow.get('Purchase Of Investment'),
        net_business_purchase_and_sale = _cashflow.get('Net Business Purchase And Sale'),
        purchase_of_business = _cashflow.get('Purchase Of Business'),
        net_ppe_purchase_and_sale = _cashflow.get('Net PPE Purchase And Sale'),
        sale_of_ppe = _cashflow.get('Sale Of PPE'),
        purchase_of_ppe = _cashflow.get('Purchase Of PPE'),
        operating_cash_flow = _cashflow.get('Operating Cash Flow'),
        cash_flow_from_continuing_operating_activities = _cashflow.get('Cash Flow From Continuing Operating Activities'),
        change_in_working_capital = _cashflow.get('Change In Working Capital'),
        change_in_other_current_liabilities = _cashflow.get('Change In Other Current Liabilities'),
        change_in_other_current_assets = _cashflow.get('Change In Other Current Assets'),
        change_in_payables_and_accrued_expense = _cashflow.get('Change In Payables And Accrued Expense'),
        change_in_accrued_expense = _cashflow.get('Change In Accrued Expense'),
        change_in_payable = _cashflow.get('Change In Payable'),
        change_in_account_payable = _cashflow.get('Change In Account Payable'),
        change_in_prepaid_assets = _cashflow.get('Change In Prepaid Assets'),
        change_in_receivables = _cashflow.get('Change In Receivables'),
        changes_in_account_receivables = _cashflow.get('Changes In Account Receivables'),
        other_non_cash_items = _cashflow.get('Other Non Cash Items'),
        stock_based_compensation = _cashflow.get('Stock Based Compensation'),
        asset_impairment_charge = _cashflow.get('Asset Impairment Charge'),
        deferred_tax = _cashflow.get('Deferred Tax'),
        deferred_income_tax = _cashflow.get('Deferred Income Tax'),
        depreciation_amortization_depletion = _cashflow.get('Depreciation Amortization Depletion'),
        depreciation_and_amortization = _cashflow.get('Depreciation And Amortization'),
        net_income_from_continuing_operations = _cashflow.get('Net Income From Continuing Operations'),

        modified_at=datetime.fromtimestamp(int(timestamp) / 1000))

    db.add(db_cashflow)
    db.commit()