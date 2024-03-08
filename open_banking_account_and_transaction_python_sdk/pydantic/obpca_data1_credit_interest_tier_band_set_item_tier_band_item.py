# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from open_banking_account_and_transaction_python_sdk.pydantic.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_notes import OBPCAData1CreditInterestTierBandSetItemTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.pydantic.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_other_application_frequency import OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency
from open_banking_account_and_transaction_python_sdk.pydantic.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType
from open_banking_account_and_transaction_python_sdk.pydantic.obpca_data1_credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency import OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency

class OBPCAData1CreditInterestTierBandSetItemTierBandItem(BaseModel):
    # The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made.   Read more: Annual Equivalent Rate (AER) http://www.investopedia.com/terms/a/aer.asp#ixzz4gfR7IO1A
    a_e_r: str = Field(alias='AER')

    # How often is interest applied to the PCA for this tier/band i.e. how often the financial institution pays accumulated interest to the customer's PCA.
    application_frequency: Literal["PerAcademicTerm", "Daily", "HalfYearly", "Monthly", "Other", "Quarterly", "PerStatementDate", "Weekly", "Yearly"] = Field(alias='ApplicationFrequency')

    # Type of interest rate, Fixed or Variable
    fixed_variable_interest_rate_type: Literal["Fixed", "Variable"] = Field(alias='FixedVariableInterestRateType')

    # Minimum deposit value for which the credit interest tier applies.
    tier_value_minimum: str = Field(alias='TierValueMinimum')

    # Bank Interest for the PCA product
    bank_interest_rate: typing.Optional[str] = Field(None, alias='BankInterestRate')

    # Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the PCA.
    bank_interest_rate_type: typing.Optional[Literal["LinkedBaseRate", "Gross", "Net", "Other"]] = Field(None, alias='BankInterestRateType')

    # How often is credit interest calculated for the account.
    calculation_frequency: typing.Optional[Literal["PerAcademicTerm", "Daily", "HalfYearly", "Monthly", "Other", "Quarterly", "PerStatementDate", "Weekly", "Yearly"]] = Field(None, alias='CalculationFrequency')

    # Amount on which Interest applied.
    deposit_interest_applied_coverage: typing.Optional[Literal["Tiered", "Whole"]] = Field(None, alias='DepositInterestAppliedCoverage')

    # Unique and unambiguous identification of a  Tier Band for a PCA.
    identification: typing.Optional[str] = Field(None, alias='Identification')

    notes: typing.Optional[OBPCAData1CreditInterestTierBandSetItemTierBandItemNotes] = Field(None, alias='Notes')

    other_application_frequency: typing.Optional[OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency] = Field(None, alias='OtherApplicationFrequency')

    other_bank_interest_type: typing.Optional[OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType] = Field(None, alias='OtherBankInterestType')

    other_calculation_frequency: typing.Optional[OBPCAData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency] = Field(None, alias='OtherCalculationFrequency')

    # Maximum deposit value for which the credit interest tier applies.
    tier_value_maximum: typing.Optional[str] = Field(None, alias='TierValueMaximum')
    class Config:
        arbitrary_types_allowed = True