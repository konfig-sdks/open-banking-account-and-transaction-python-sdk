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

from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_fee_applicable_range import OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_fee_charge_cap import OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeChargeCap
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_notes import OBPCAData1OtherFeesChargesFeeChargeDetailItemNotes
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_application_frequency import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_calculation_frequency import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_fee_category_type import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_fee_rate_type import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges_fee_charge_detail_item_other_fee_type import OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeType

class RequiredOBPCAData1OtherFeesChargesFeeChargeDetailItem(TypedDict):
    # How frequently the fee/charge is applied to the account
    ApplicationFrequency: str

    # Categorisation of fees and charges into standard categories.
    FeeCategory: str

    # Fee/Charge Type
    FeeType: str

class OptionalOBPCAData1OtherFeesChargesFeeChargeDetailItem(TypedDict, total=False):
    # How frequently the fee/charge is calculated
    CalculationFrequency: str

    # Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    FeeAmount: str

    FeeApplicableRange: OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange

    FeeChargeCap: OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeChargeCap

    # Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    FeeRate: str

    # Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    FeeRateType: str

    Notes: OBPCAData1OtherFeesChargesFeeChargeDetailItemNotes

    OtherApplicationFrequency: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency

    OtherCalculationFrequency: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherCalculationFrequency

    OtherFeeCategoryType: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeCategoryType

    OtherFeeRateType: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeRateType

    OtherFeeType: OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherFeeType

class OBPCAData1OtherFeesChargesFeeChargeDetailItem(RequiredOBPCAData1OtherFeesChargesFeeChargeDetailItem, OptionalOBPCAData1OtherFeesChargesFeeChargeDetailItem):
    pass
