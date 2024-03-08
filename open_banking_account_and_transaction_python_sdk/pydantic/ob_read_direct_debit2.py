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

from open_banking_account_and_transaction_python_sdk.pydantic.links import Links
from open_banking_account_and_transaction_python_sdk.pydantic.meta import Meta
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_direct_debit2_data import OBReadDirectDebit2Data

class OBReadDirectDebit2(BaseModel):
    data: OBReadDirectDebit2Data = Field(alias='Data')

    links: typing.Optional[Links] = Field(None, alias='Links')

    meta: typing.Optional[Meta] = Field(None, alias='Meta')
    class Config:
        arbitrary_types_allowed = True
