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

from open_banking_account_and_transaction_python_sdk.type.identification1 import Identification1

class RequiredOBBranchAndFinancialInstitutionIdentification51(TypedDict):
    Identification: Identification1

    # Name of the identification scheme, in a coded form as published in an external list.
    SchemeName: str

class OptionalOBBranchAndFinancialInstitutionIdentification51(TypedDict, total=False):
    pass

class OBBranchAndFinancialInstitutionIdentification51(RequiredOBBranchAndFinancialInstitutionIdentification51, OptionalOBBranchAndFinancialInstitutionIdentification51):
    pass
