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

from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_overdraft_notes import OBReadProduct2DataProductItemOtherProductTypeOverdraftNotes
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSet

class RequiredOBReadProduct2DataProductItemOtherProductTypeOverdraft(TypedDict):
    OverdraftTierBandSet: OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSet

class OptionalOBReadProduct2DataProductItemOtherProductTypeOverdraft(TypedDict, total=False):
    Notes: OBReadProduct2DataProductItemOtherProductTypeOverdraftNotes

class OBReadProduct2DataProductItemOtherProductTypeOverdraft(RequiredOBReadProduct2DataProductItemOtherProductTypeOverdraft, OptionalOBReadProduct2DataProductItemOtherProductTypeOverdraft):
    pass
