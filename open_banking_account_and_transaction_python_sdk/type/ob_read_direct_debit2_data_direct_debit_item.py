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
from open_banking_account_and_transaction_python_sdk.type.direct_debit_id import DirectDebitId
from open_banking_account_and_transaction_python_sdk.type.mandate_identification import MandateIdentification
from open_banking_account_and_transaction_python_sdk.type.name2 import Name2
from open_banking_account_and_transaction_python_sdk.type.ob_active_or_historic_currency_and_amount0 import OBActiveOrHistoricCurrencyAndAmount0
from open_banking_account_and_transaction_python_sdk.type.ob_external_direct_debit_status1_code import OBExternalDirectDebitStatus1Code

class RequiredOBReadDirectDebit2DataDirectDebitItem(TypedDict):
    AccountId: AccountId

    MandateIdentification: MandateIdentification

    Name: Name2

class OptionalOBReadDirectDebit2DataDirectDebitItem(TypedDict, total=False):
    DirectDebitId: DirectDebitId

    DirectDebitStatusCode: OBExternalDirectDebitStatus1Code

    # Regularity with which direct debit instructions are to be created and processed.
    Frequency: str

    PreviousPaymentAmount: OBActiveOrHistoricCurrencyAndAmount0

    # Date of most recent direct debit collection.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    PreviousPaymentDateTime: datetime

class OBReadDirectDebit2DataDirectDebitItem(RequiredOBReadDirectDebit2DataDirectDebitItem, OptionalOBReadDirectDebit2DataDirectDebitItem):
    pass