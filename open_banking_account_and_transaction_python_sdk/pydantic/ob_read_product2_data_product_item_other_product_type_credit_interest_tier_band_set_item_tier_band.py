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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item import OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem

OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBand = typing.List[OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem]
