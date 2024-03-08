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

from open_banking_account_and_transaction_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeType
from open_banking_account_and_transaction_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_notes import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemNotes
from open_banking_account_and_transaction_python_sdk.pydantic.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeType

class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem(BaseModel):
    fee_type: OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeType = Field(alias='FeeType')

    # Min Max type
    min_max_type: Literal["Minimum", "Maximum"] = Field(alias='MinMaxType')

    # Period e.g. day, week, month etc. for which the fee/charge is capped
    capping_period: typing.Optional[Literal["Day", "Half Year", "Month", "Quarter", "Week", "Year"]] = Field(None, alias='CappingPeriod')

    # Cap amount charged for a fee/charge
    fee_cap_amount: typing.Optional[str] = Field(None, alias='FeeCapAmount')

    # Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it’s part of a government scheme, or whether the rate may vary dependent on the applicant’s circumstances.
    fee_cap_occurrence: typing.Optional[typing.Union[int, float]] = Field(None, alias='FeeCapOccurrence')

    notes: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemNotes] = Field(None, alias='Notes')

    other_fee_type: typing.Optional[OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeType] = Field(None, alias='OtherFeeType')
    class Config:
        arbitrary_types_allowed = True
