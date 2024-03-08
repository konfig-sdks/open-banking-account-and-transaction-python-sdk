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
from open_banking_account_and_transaction_python_sdk.pydantic.active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from open_banking_account_and_transaction_python_sdk.pydantic.description0 import Description0
from open_banking_account_and_transaction_python_sdk.pydantic.nickname import Nickname
from open_banking_account_and_transaction_python_sdk.pydantic.ob_account_status1_code import OBAccountStatus1Code
from open_banking_account_and_transaction_python_sdk.pydantic.ob_external_account_sub_type1_code import OBExternalAccountSubType1Code
from open_banking_account_and_transaction_python_sdk.pydantic.ob_external_account_type1_code import OBExternalAccountType1Code

class OBAccount6Basic(BaseModel):
    account_id: AccountId = Field(alias='AccountId')

    account_sub_type: OBExternalAccountSubType1Code = Field(alias='AccountSubType')

    account_type: OBExternalAccountType1Code = Field(alias='AccountType')

    currency: ActiveOrHistoricCurrencyCode0 = Field(alias='Currency')

    description: typing.Optional[Description0] = Field(None, alias='Description')

    # Maturity date of the account.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    maturity_date: typing.Optional[datetime] = Field(None, alias='MaturityDate')

    nickname: typing.Optional[Nickname] = Field(None, alias='Nickname')

    # Date on which the account and related basic services are effectively operational for the account owner.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    opening_date: typing.Optional[datetime] = Field(None, alias='OpeningDate')

    status: typing.Optional[OBAccountStatus1Code] = Field(None, alias='Status')

    # Date and time at which the resource status was updated.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    status_update_date_time: typing.Optional[datetime] = Field(None, alias='StatusUpdateDateTime')

    # Specifies the switch status for the account, in a coded form.
    switch_status: typing.Optional[str] = Field(None, alias='SwitchStatus')
    class Config:
        arbitrary_types_allowed = True
