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

from open_banking_account_and_transaction_python_sdk.pydantic.description3 import Description3
from open_banking_account_and_transaction_python_sdk.pydantic.name4 import Name4
from open_banking_account_and_transaction_python_sdk.pydantic.ob_code_mnemonic import OBCodeMnemonic

class OBOtherCodeType18(BaseModel):
    description: Description3 = Field(alias='Description')

    name: Name4 = Field(alias='Name')

    code: typing.Optional[OBCodeMnemonic] = Field(None, alias='Code')
    class Config:
        arbitrary_types_allowed = True
