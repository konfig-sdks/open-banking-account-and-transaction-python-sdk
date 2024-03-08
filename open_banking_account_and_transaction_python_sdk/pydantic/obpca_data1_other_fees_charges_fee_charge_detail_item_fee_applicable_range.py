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


class OBPCAData1OtherFeesChargesFeeChargeDetailItemFeeApplicableRange(BaseModel):
    # Maximum Amount on which fee is applicable (where it is expressed as an amount)
    maximum_amount: typing.Optional[str] = Field(None, alias='MaximumAmount')

    # Maximum rate on which fee/charge is applicable(where it is expressed as an rate)
    maximum_rate: typing.Optional[str] = Field(None, alias='MaximumRate')

    # Minimum Amount on which fee/charge is applicable (where it is expressed as an amount)
    minimum_amount: typing.Optional[str] = Field(None, alias='MinimumAmount')

    # Minimum rate on which fee/charge is applicable(where it is expressed as an rate)
    minimum_rate: typing.Optional[str] = Field(None, alias='MinimumRate')
    class Config:
        arbitrary_types_allowed = True
