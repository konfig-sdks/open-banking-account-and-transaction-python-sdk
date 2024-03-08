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

from open_banking_account_and_transaction_python_sdk.pydantic.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.pydantic.direct_debit_id import DirectDebitId
from open_banking_account_and_transaction_python_sdk.pydantic.mandate_identification import MandateIdentification
from open_banking_account_and_transaction_python_sdk.pydantic.name2 import Name2
from open_banking_account_and_transaction_python_sdk.pydantic.ob_active_or_historic_currency_and_amount0 import OBActiveOrHistoricCurrencyAndAmount0
from open_banking_account_and_transaction_python_sdk.pydantic.ob_external_direct_debit_status1_code import OBExternalDirectDebitStatus1Code

class OBReadDirectDebit2DataDirectDebitItem(BaseModel):
    account_id: AccountId = Field(alias='AccountId')

    mandate_identification: MandateIdentification = Field(alias='MandateIdentification')

    name: Name2 = Field(alias='Name')

    direct_debit_id: typing.Optional[DirectDebitId] = Field(None, alias='DirectDebitId')

    direct_debit_status_code: typing.Optional[OBExternalDirectDebitStatus1Code] = Field(None, alias='DirectDebitStatusCode')

    # Regularity with which direct debit instructions are to be created and processed.
    frequency: typing.Optional[str] = Field(None, alias='Frequency')

    previous_payment_amount: typing.Optional[OBActiveOrHistoricCurrencyAndAmount0] = Field(None, alias='PreviousPaymentAmount')

    # Date of most recent direct debit collection.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    previous_payment_date_time: typing.Optional[datetime] = Field(None, alias='PreviousPaymentDateTime')
    class Config:
        arbitrary_types_allowed = True
