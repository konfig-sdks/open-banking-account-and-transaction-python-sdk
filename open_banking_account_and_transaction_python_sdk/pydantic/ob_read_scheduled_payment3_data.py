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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_scheduled_payment3 import OBScheduledPayment3

class OBReadScheduledPayment3Data(BaseModel):
    scheduled_payment: typing.Optional[typing.List[OBScheduledPayment3]] = Field(None, alias='ScheduledPayment')
    class Config:
        arbitrary_types_allowed = True
