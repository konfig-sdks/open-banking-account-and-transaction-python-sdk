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

from open_banking_account_and_transaction_python_sdk.type.ob_read_balance1_data_balance import OBReadBalance1DataBalance

class RequiredOBReadBalance1Data(TypedDict):
    Balance: OBReadBalance1DataBalance

class OptionalOBReadBalance1Data(TypedDict, total=False):
    pass

class OBReadBalance1Data(RequiredOBReadBalance1Data, OptionalOBReadBalance1Data):
    pass
