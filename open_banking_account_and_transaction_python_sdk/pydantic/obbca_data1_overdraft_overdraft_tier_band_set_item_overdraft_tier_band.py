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

from open_banking_account_and_transaction_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem

OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBand = typing.List[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem]
