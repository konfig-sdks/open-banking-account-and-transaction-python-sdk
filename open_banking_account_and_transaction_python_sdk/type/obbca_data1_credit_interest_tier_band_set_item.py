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

from open_banking_account_and_transaction_python_sdk.type.obbca_data1_credit_interest_tier_band_set_item_notes import OBBCAData1CreditInterestTierBandSetItemNotes
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_credit_interest_tier_band_set_item_tier_band import OBBCAData1CreditInterestTierBandSetItemTierBand

class RequiredOBBCAData1CreditInterestTierBandSetItem(TypedDict):
    # Describes whether accrued interest is payable only to the BCA or to another bank account
    Destination: str

    TierBand: OBBCAData1CreditInterestTierBandSetItemTierBand

    # The methodology of how credit interest is paid/applied. It can be:-  1. Banded Interest rates are banded. i.e. Increasing rate on whole balance as balance increases.  2. Tiered Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.  3. Whole The same interest rate is applied irrespective of the BCA balance
    TierBandMethod: str

class OptionalOBBCAData1CreditInterestTierBandSetItem(TypedDict, total=False):
    # Methods of calculating interest
    CalculationMethod: str

    Notes: OBBCAData1CreditInterestTierBandSetItemNotes

class OBBCAData1CreditInterestTierBandSetItem(RequiredOBBCAData1CreditInterestTierBandSetItem, OptionalOBBCAData1CreditInterestTierBandSetItem):
    pass
