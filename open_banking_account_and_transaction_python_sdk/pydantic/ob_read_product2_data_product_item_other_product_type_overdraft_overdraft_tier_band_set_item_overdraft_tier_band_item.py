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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges

class OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItem(BaseModel):
    # Minimum value of Overdraft Tier/Band
    tier_value_min: str = Field(alias='TierValueMin')

    # Specifies the maximum length of a band for a fixed overdraft agreement
    agreement_length_max: typing.Optional[int] = Field(None, alias='AgreementLengthMax')

    # Specifies the minimum length of a band for a fixed overdraft agreement
    agreement_length_min: typing.Optional[int] = Field(None, alias='AgreementLengthMin')

    # Specifies the period of a fixed length overdraft agreement
    agreement_period: typing.Optional[Literal["PACT", "PDAY", "PHYR", "PMTH", "PQTR", "PWEK", "PYER"]] = Field(None, alias='AgreementPeriod')

    # Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it�s part of a government scheme, or whether the rate may vary dependent on the applicant�s circumstances.
    bank_guaranteed_indicator: typing.Optional[bool] = Field(None, alias='BankGuaranteedIndicator')

    # EAR means Effective Annual Rate and/or Equivalent Annual Rate (frequently used interchangeably), being the actual annual interest rate of an Overdraft.
    e_a_r: typing.Optional[str] = Field(None, alias='EAR')

    # Unique and unambiguous identification of a  Tier Band for a overdraft.
    identification: typing.Optional[str] = Field(None, alias='Identification')

    notes: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes] = Field(None, alias='Notes')

    overdraft_fees_charges: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges] = Field(None, alias='OverdraftFeesCharges')

    # Refers to which interest rate is applied when interests are tiered. For example, if an overdraft balance is �2k and the interest tiers are:- 0-�500 0.1%, 500-1000 0.2%, 1000-10000 0.5%, then the applicable interest rate could either be 0.5% of the entire balance (since the account balance sits in the top interest tier) or (0.1%*500)+(0.2%*500)+(0.5%*1000). In the 1st situation, we say the interest is applied to the �Whole� of the account balance,  and in the 2nd that it is �Tiered�.
    overdraft_interest_charging_coverage: typing.Optional[Literal["INBA", "INTI", "INWH"]] = Field(None, alias='OverdraftInterestChargingCoverage')

    # Maximum value of Overdraft Tier/Band
    tier_value_max: typing.Optional[str] = Field(None, alias='TierValueMax')
    class Config:
        arbitrary_types_allowed = True
