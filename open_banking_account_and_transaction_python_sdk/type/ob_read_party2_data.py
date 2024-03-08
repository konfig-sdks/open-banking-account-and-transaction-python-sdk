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

from open_banking_account_and_transaction_python_sdk.type.ob_party2 import OBParty2

class RequiredOBReadParty2Data(TypedDict):
    pass

class OptionalOBReadParty2Data(TypedDict, total=False):
    Party: OBParty2

class OBReadParty2Data(RequiredOBReadParty2Data, OptionalOBReadParty2Data):
    pass
