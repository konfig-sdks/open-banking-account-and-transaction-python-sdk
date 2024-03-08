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


class RequiredOBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency(TypedDict):
    # Description to describe the purpose of the code
    Description: str

    # Long name associated with the code
    Name: str

class OptionalOBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency(TypedDict, total=False):
    # The four letter Mnemonic used within an XML file to identify a code
    Code: str

class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency(RequiredOBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency, OptionalOBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency):
    pass
