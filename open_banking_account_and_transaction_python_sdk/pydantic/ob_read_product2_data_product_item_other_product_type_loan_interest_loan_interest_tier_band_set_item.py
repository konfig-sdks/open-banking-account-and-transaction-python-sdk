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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_interest_calculation_method1_code import OBInterestCalculationMethod1Code
from open_banking_account_and_transaction_python_sdk.pydantic.ob_other_code_type10 import OBOtherCodeType10
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesCharges
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBand
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_notes import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemNotes

class OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItem(BaseModel):
    calculation_method: OBInterestCalculationMethod1Code = Field(alias='CalculationMethod')

    loan_interest_tier_band: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBand = Field(alias='LoanInterestTierBand')

    # The methodology of how credit interest is charged. It can be:- 1. Banded Interest rates are banded. i.e. Increasing rate on whole balance as balance increases. 2. Tiered Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance. 3. Whole The same interest rate is applied irrespective of the SME Loan balance
    tier_band_method: Literal["INBA", "INTI", "INWH"] = Field(alias='TierBandMethod')

    # Loan interest tierbandset identification. Used by  loan providers for internal use purpose.
    identification: typing.Optional[str] = Field(None, alias='Identification')

    loan_interest_fees_charges: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesCharges] = Field(None, alias='LoanInterestFeesCharges')

    notes: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemNotes] = Field(None, alias='Notes')

    other_calculation_method: typing.Optional[OBOtherCodeType10] = Field(None, alias='OtherCalculationMethod')
    class Config:
        arbitrary_types_allowed = True
