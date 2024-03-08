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

from open_banking_account_and_transaction_python_sdk.type.description3 import Description3
from open_banking_account_and_transaction_python_sdk.type.name4 import Name4
from open_banking_account_and_transaction_python_sdk.type.ob_code_mnemonic import OBCodeMnemonic

class RequiredOBOtherCodeType17(TypedDict):
    Description: Description3

    Name: Name4

class OptionalOBOtherCodeType17(TypedDict, total=False):
    Code: OBCodeMnemonic

class OBOtherCodeType17(RequiredOBOtherCodeType17, OptionalOBOtherCodeType17):
    pass
