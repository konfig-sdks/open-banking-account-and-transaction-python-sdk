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

from open_banking_account_and_transaction_python_sdk.type.ob_interest_fixed_variable_type1_code import OBInterestFixedVariableType1Code
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesCharges
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_notes import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_other_loan_provider_interest_rate_type import OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType

class RequiredOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(TypedDict):
    FixedVariableInterestRateType: OBInterestFixedVariableType1Code

    # The unit of period (days, weeks, months etc.) of the Minimum Term
    MinTermPeriod: str

    # The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made.  For SME Loan, this APR is the representative APR which includes any account fees.
    RepAPR: str

    # Minimum loan term for which the loan interest tier applies.
    TierValueMinTerm: int

    # Minimum loan value for which the loan interest tier applies.
    TierValueMinimum: str

class OptionalOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(TypedDict, total=False):
    # Unique and unambiguous identification of a  Tier Band for a SME Loan.
    Identification: str

    LoanInterestFeesCharges: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesCharges

    # Loan provider Interest for the SME Loan product
    LoanProviderInterestRate: str

    # Interest rate types, other than APR, which financial institutions may use to describe the annual interest rate payable for the SME Loan.
    LoanProviderInterestRateType: str

    # The unit of period (days, weeks, months etc.) of the Maximum Term
    MaxTermPeriod: str

    Notes: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemNotes

    OtherLoanProviderInterestRateType: OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType

    # Maximum loan term for which the loan interest tier applies.
    TierValueMaxTerm: int

    # Maximum loan value for which the loan interest tier applies.
    TierValueMaximum: str

class OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(RequiredOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem, OptionalOBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem):
    pass
