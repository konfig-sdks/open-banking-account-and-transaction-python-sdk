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

from open_banking_account_and_transaction_python_sdk.pydantic.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.pydantic.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges

class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(BaseModel):
    # Minimum value of Overdraft Tier/Band
    tier_value_min: str = Field(alias='TierValueMin')

    # Indicates that a bank provides the overdraft limit up to TierValueMIn to all customers automatically
    bank_guaranteed_indicator: typing.Optional[bool] = Field(None, alias='BankGuaranteedIndicator')

    # EAR means Effective Annual Rate and/or Equivalent Annual Rate (frequently used interchangeably), being the actual annual interest rate of an Overdraft.
    e_a_r: typing.Optional[str] = Field(None, alias='EAR')

    # Unique and unambiguous identification of a  Tier Band for a overdraft.
    identification: typing.Optional[str] = Field(None, alias='Identification')

    notes: typing.Optional[OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes] = Field(None, alias='Notes')

    overdraft_fees_charges: typing.Optional[OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges] = Field(None, alias='OverdraftFeesCharges')

    # Interest charged on whole amount or tiered/banded
    overdraft_interest_charging_coverage: typing.Optional[Literal["Tiered", "Whole"]] = Field(None, alias='OverdraftInterestChargingCoverage')

    # An annual percentage rate (APR) is the annual rate charged for borrowing or earned through an investment. APR is expressed as a percentage that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction but does not take compounding into account.
    representative_a_p_r: typing.Optional[str] = Field(None, alias='RepresentativeAPR')

    # Maximum value of Overdraft Tier/Band
    tier_value_max: typing.Optional[str] = Field(None, alias='TierValueMax')
    class Config:
        arbitrary_types_allowed = True