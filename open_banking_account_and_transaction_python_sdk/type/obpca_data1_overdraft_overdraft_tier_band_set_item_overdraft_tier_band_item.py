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

from open_banking_account_and_transaction_python_sdk.type.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges

class RequiredOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(TypedDict):
    # Minimum value of Overdraft Tier/Band
    TierValueMin: str

class OptionalOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(TypedDict, total=False):
    # Indicates that a bank provides the overdraft limit up to TierValueMIn to all customers automatically
    BankGuaranteedIndicator: bool

    # EAR means Effective Annual Rate and/or Equivalent Annual Rate (frequently used interchangeably), being the actual annual interest rate of an Overdraft.
    EAR: str

    # Unique and unambiguous identification of a  Tier Band for a overdraft.
    Identification: str

    Notes: OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes

    OverdraftFeesCharges: OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges

    # Interest charged on whole amount or tiered/banded
    OverdraftInterestChargingCoverage: str

    # An annual percentage rate (APR) is the annual rate charged for borrowing or earned through an investment. APR is expressed as a percentage that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction but does not take compounding into account.
    RepresentativeAPR: str

    # Maximum value of Overdraft Tier/Band
    TierValueMax: str

class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(RequiredOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem, OptionalOBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem):
    pass
