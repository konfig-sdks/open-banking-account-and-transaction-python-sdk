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

from open_banking_account_and_transaction_python_sdk.type.value import Value

class RequiredOBStatement2StatementValueItem(TypedDict):
    # Statement value type, in a coded form.
    Type: str

    Value: Value

class OptionalOBStatement2StatementValueItem(TypedDict, total=False):
    pass

class OBStatement2StatementValueItem(RequiredOBStatement2StatementValueItem, OptionalOBStatement2StatementValueItem):
    pass
