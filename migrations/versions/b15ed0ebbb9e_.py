"""empty message

Revision ID: b15ed0ebbb9e
Revises: f2558e8b0237
Create Date: 2024-03-12 19:00:57.637604

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b15ed0ebbb9e'
down_revision: Union[str, None] = 'f2558e8b0237'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income_statements', 'total_revenue',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'operating_revenue',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'cost_of_revenue',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'gross_profit',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'selling_general_and_administrative',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'general_and_administrative_expense',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'other_general_and_administrative',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'research_and_development',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'operating_income',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_non_operating_interest_income_expense',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_income_non_operating',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_expense_non_operating',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_other_finance_cost',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'other_income_expense',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'gain_on_sale_of_security',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'other_non_operating_income_expenses',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'pretax_income',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_common_stockholders',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_including_noncontrolling_interests',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_continuous_operations',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'average_dilution_earnings',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'diluted_ni_available_to_come_stockholders',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'basic_eps',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'diluted_eps',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'basic_average_shares',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'diluted_average_shares',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_operating_income_as_reported',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_expenses',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_from_continuing_and_discontinued_operation',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'normalized_income',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_income',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_expense',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_interest_income',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'ebit',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'ebitda',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'reconciled_cost_of_revenue',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'reconciled_depreciation',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_from_continuing_operation_net_minority_interest',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_unusual_items_excluding_goodwill',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_unusual_items',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'normalized_ebitda',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'tax_rate_for_calcs',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'tax_effect_of_unusual_items',
               existing_type=mysql.DECIMAL(precision=20, scale=10),
               type_=sa.Numeric(precision=30, scale=10),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('income_statements', 'tax_effect_of_unusual_items',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'tax_rate_for_calcs',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'normalized_ebitda',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_unusual_items',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_unusual_items_excluding_goodwill',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_from_continuing_operation_net_minority_interest',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'reconciled_depreciation',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'reconciled_cost_of_revenue',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'ebitda',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'ebit',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_interest_income',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_expense',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_income',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'normalized_income',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_from_continuing_and_discontinued_operation',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_expenses',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_operating_income_as_reported',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'diluted_average_shares',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'basic_average_shares',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'diluted_eps',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'basic_eps',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'diluted_ni_available_to_come_stockholders',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'average_dilution_earnings',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_continuous_operations',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_including_noncontrolling_interests',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_income_common_stockholders',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'pretax_income',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'other_non_operating_income_expenses',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'gain_on_sale_of_security',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'other_income_expense',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_other_finance_cost',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_expense_non_operating',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'interest_income_non_operating',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'net_non_operating_interest_income_expense',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'operating_income',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'research_and_development',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'other_general_and_administrative',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'general_and_administrative_expense',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'selling_general_and_administrative',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'gross_profit',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'cost_of_revenue',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'operating_revenue',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    op.alter_column('income_statements', 'total_revenue',
               existing_type=sa.Numeric(precision=30, scale=10),
               type_=mysql.DECIMAL(precision=20, scale=10),
               existing_nullable=False)
    # ### end Alembic commands ###
