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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_consent1_data import OBReadConsent1Data

class OBReadConsent1(BaseModel):
    data: OBReadConsent1Data = Field(alias='Data')

    # The Risk section is sent by the initiating party to the ASPSP. It is used to specify additional details for risk scoring for Account Info.
    risk: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='Risk')
    class Config:
        arbitrary_types_allowed = True
