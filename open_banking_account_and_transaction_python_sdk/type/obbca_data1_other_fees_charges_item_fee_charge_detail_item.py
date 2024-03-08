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

from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_notes import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_application_frequency import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_category_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType

class RequiredOBBCAData1OtherFeesChargesItemFeeChargeDetailItem(TypedDict):
    # How frequently the fee/charge is applied to the account
    ApplicationFrequency: str

    # Categorisation of fees and charges into standard categories.
    FeeCategory: str

    # Fee/Charge Type
    FeeType: str

class OptionalOBBCAData1OtherFeesChargesItemFeeChargeDetailItem(TypedDict, total=False):
    # How frequently the fee/charge is calculated
    CalculationFrequency: str

    # Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    FeeAmount: str

    FeeApplicableRange: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange

    FeeChargeCap: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap

    # Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    FeeRate: str

    # Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    FeeRateType: str

    # Fee/charge which is usually negotiable rather than a fixed amount
    NegotiableIndicator: bool

    Notes: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes

    OtherApplicationFrequency: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency

    OtherCalculationFrequency: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency

    OtherFeeCategoryType: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType

    OtherFeeRateType: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType

    OtherFeeType: OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType

class OBBCAData1OtherFeesChargesItemFeeChargeDetailItem(RequiredOBBCAData1OtherFeesChargesItemFeeChargeDetailItem, OptionalOBBCAData1OtherFeesChargesItemFeeChargeDetailItem):
    pass
