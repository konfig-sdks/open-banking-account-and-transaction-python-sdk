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

from open_banking_account_and_transaction_python_sdk.type.ob_amount10 import OBAmount10
from open_banking_account_and_transaction_python_sdk.type.ob_min_max_type1_code import OBMinMaxType1Code
from open_banking_account_and_transaction_python_sdk.type.ob_period1_code import OBPeriod1Code
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_notes import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType

class RequiredOBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem(TypedDict):
    FeeType: OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType

    MinMaxType: OBMinMaxType1Code

class OptionalOBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem(TypedDict, total=False):
    CappingPeriod: OBPeriod1Code

    FeeCapAmount: OBAmount10

    # Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it�s part of a government scheme, or whether the rate may vary dependent on the applicant�s circumstances.
    FeeCapOccurrence: int

    Notes: OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes

    OtherFeeType: OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType

class OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem(RequiredOBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem, OptionalOBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem):
    pass
