import datetime

from pydantic import BaseModel

class IncomeStatementCreate(BaseModel):
    total_revenue: float
    operating_revenue: float
    cost_of_revenue: float
    gross_profit: float
    selling_general_and_administrative: float
    general_and_administrative_expense: float
    other_general_and_administrative: float
    research_and_development: float
    operating_income: float
    net_non_operating_interest_income_expense: float
    interest_income_non_operating: float
    interest_expense_non_operating: float
    total_other_finance_cost: float
    other_income_expense: float
    gain_on_sale_of_security: float
    other_non_operating_income_expenses: float
    pretax_income: float
    net_income_common_stockholders: float
    net_income: float
    net_income_including_noncontrolling_interests: float
    net_income_continuous_operations: float
    average_dilution_earnings: float
    diluted_ni_available_to_come_stockholders: float
    basic_eps: float
    diluted_eps: float
    basic_average_shares: float
    diluted_average_shares: float
    total_operating_income_as_reported: float
    total_expenses: float
    net_income_from_continuing_and_discontinued_operation: float
    normalized_income: float
    interest_income: float
    interest_expense: float
    net_interest_income: float
    ebit: float
    ebitda: float
    reconciled_cost_of_revenue: float
    reconciled_depreciation: float
    net_income_from_continuing_operation_net_minority_interest: float
    total_unusual_items_excluding_goodwill: float
    total_unusual_items: float
    normalized_ebitda: float
    tax_rate_for_calcs: float
    tax_effect_of_unusual_items: float
    modified_at: datetime.datetime