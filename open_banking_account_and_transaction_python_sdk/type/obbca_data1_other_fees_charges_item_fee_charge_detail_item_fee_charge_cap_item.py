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

from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeType
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_notes import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemNotes
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeType

class RequiredOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem(TypedDict):
    FeeType: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeType

    # Min Max type
    MinMaxType: str

class OptionalOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem(TypedDict, total=False):
    # Period e.g. day, week, month etc. for which the fee/charge is capped
    CappingPeriod: str

    # Cap amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    FeeCapAmount: str

    # fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount
    FeeCapOccurrence: typing.Union[int, float]

    Notes: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemNotes

    OtherFeeType: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeType

class OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem(RequiredOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem, OptionalOBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem):
    pass