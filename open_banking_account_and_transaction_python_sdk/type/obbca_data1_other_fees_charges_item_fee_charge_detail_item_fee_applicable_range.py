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


class RequiredOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange(TypedDict):
    pass

class OptionalOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange(TypedDict, total=False):
    # Maximum Amount on which fee is applicable (where it is expressed as an amount)
    MaximumAmount: str

    # Maximum rate on which fee/charge is applicable(where it is expressed as an rate)
    MaximumRate: str

    # Minimum Amount on which fee/charge is applicable (where it is expressed as an amount)
    MinimumAmount: str

    # Minimum rate on which fee/charge is applicable(where it is expressed as an rate)
    MinimumRate: str

class OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange(RequiredOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange, OptionalOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange):
    pass
