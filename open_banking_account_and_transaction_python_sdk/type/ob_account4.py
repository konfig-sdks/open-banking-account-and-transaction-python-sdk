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

from open_banking_account_and_transaction_python_sdk.type.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.type.active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from open_banking_account_and_transaction_python_sdk.type.description0 import Description0
from open_banking_account_and_transaction_python_sdk.type.nickname import Nickname
from open_banking_account_and_transaction_python_sdk.type.ob_account4_account import OBAccount4Account
from open_banking_account_and_transaction_python_sdk.type.ob_account_status1_code import OBAccountStatus1Code
from open_banking_account_and_transaction_python_sdk.type.ob_branch_and_financial_institution_identification50 import OBBranchAndFinancialInstitutionIdentification50
from open_banking_account_and_transaction_python_sdk.type.ob_external_account_sub_type1_code import OBExternalAccountSubType1Code
from open_banking_account_and_transaction_python_sdk.type.ob_external_account_type1_code import OBExternalAccountType1Code

class RequiredOBAccount4(TypedDict):
    AccountId: AccountId

    AccountSubType: OBExternalAccountSubType1Code

    AccountType: OBExternalAccountType1Code

    Currency: ActiveOrHistoricCurrencyCode0

class OptionalOBAccount4(TypedDict, total=False):
    Account: OBAccount4Account

    Description: Description0

    Nickname: Nickname

    Servicer: OBBranchAndFinancialInstitutionIdentification50

    Status: OBAccountStatus1Code

    # Date and time at which the resource status was updated.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    StatusUpdateDateTime: datetime

class OBAccount4(RequiredOBAccount4, OptionalOBAccount4):
    pass