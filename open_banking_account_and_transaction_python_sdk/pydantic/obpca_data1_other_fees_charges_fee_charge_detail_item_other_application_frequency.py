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


class OBPCAData1OtherFeesChargesFeeChargeDetailItemOtherApplicationFrequency(BaseModel):
    # Description to describe the purpose of the code
    description: str = Field(alias='Description')

    # Long name associated with the code
    name: str = Field(alias='Name')

    # The four letter Mnemonic used within an XML file to identify a code
    code: typing.Optional[str] = Field(None, alias='Code')
    class Config:
        arbitrary_types_allowed = True
