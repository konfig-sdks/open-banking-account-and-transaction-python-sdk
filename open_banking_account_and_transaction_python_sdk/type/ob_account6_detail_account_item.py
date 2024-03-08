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

from open_banking_account_and_transaction_python_sdk.type.identification0 import Identification0
from open_banking_account_and_transaction_python_sdk.type.name0 import Name0
from open_banking_account_and_transaction_python_sdk.type.secondary_identification import SecondaryIdentification

class RequiredOBAccount6DetailAccountItem(TypedDict):
    Identification: Identification0

    # Name of the identification scheme, in a coded form as published in an external list.
    SchemeName: str

class OptionalOBAccount6DetailAccountItem(TypedDict, total=False):
    Name: Name0

    SecondaryIdentification: SecondaryIdentification

class OBAccount6DetailAccountItem(RequiredOBAccount6DetailAccountItem, OptionalOBAccount6DetailAccountItem):
    pass