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
from open_banking_account_and_transaction_python_sdk.pydantic.debtor_reference import DebtorReference
from open_banking_account_and_transaction_python_sdk.pydantic.ob_active_or_historic_currency_and_amount1 import OBActiveOrHistoricCurrencyAndAmount1
from open_banking_account_and_transaction_python_sdk.pydantic.ob_external_schedule_type1_code import OBExternalScheduleType1Code
from open_banking_account_and_transaction_python_sdk.pydantic.reference import Reference
from open_banking_account_and_transaction_python_sdk.pydantic.scheduled_payment_id import ScheduledPaymentId

class OBScheduledPayment3Basic(BaseModel):
    account_id: AccountId = Field(alias='AccountId')

    instructed_amount: OBActiveOrHistoricCurrencyAndAmount1 = Field(alias='InstructedAmount')

    # The date on which the scheduled payment will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    scheduled_payment_date_time: datetime = Field(alias='ScheduledPaymentDateTime')

    scheduled_type: OBExternalScheduleType1Code = Field(alias='ScheduledType')

    debtor_reference: typing.Optional[DebtorReference] = Field(None, alias='DebtorReference')

    reference: typing.Optional[Reference] = Field(None, alias='Reference')

    scheduled_payment_id: typing.Optional[ScheduledPaymentId] = Field(None, alias='ScheduledPaymentId')
    class Config:
        arbitrary_types_allowed = True
