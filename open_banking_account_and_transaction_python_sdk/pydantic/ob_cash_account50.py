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

from open_banking_account_and_transaction_python_sdk.pydantic.identification0 import Identification0
from open_banking_account_and_transaction_python_sdk.pydantic.name0 import Name0
from open_banking_account_and_transaction_python_sdk.pydantic.secondary_identification import SecondaryIdentification

class OBCashAccount50(BaseModel):
    identification: Identification0 = Field(alias='Identification')

    # Name of the identification scheme, in a coded form as published in an external list.
    scheme_name: str = Field(alias='SchemeName')

    name: typing.Optional[Name0] = Field(None, alias='Name')

    secondary_identification: typing.Optional[SecondaryIdentification] = Field(None, alias='SecondaryIdentification')
    class Config:
        arbitrary_types_allowed = True
