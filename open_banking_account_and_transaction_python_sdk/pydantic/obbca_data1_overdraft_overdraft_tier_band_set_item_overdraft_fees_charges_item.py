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

from open_banking_account_and_transaction_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap
from open_banking_account_and_transaction_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail

class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem(BaseModel):
    overdraft_fee_charge_detail: OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail = Field(alias='OverdraftFeeChargeDetail')

    overdraft_fee_charge_cap: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap] = Field(None, alias='OverdraftFeeChargeCap')
    class Config:
        arbitrary_types_allowed = True
