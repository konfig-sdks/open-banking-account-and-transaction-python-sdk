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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_active_or_historic_currency_and_amount5 import OBActiveOrHistoricCurrencyAndAmount5

class OBStatement2DetailStatementBenefitItem(BaseModel):
    amount: OBActiveOrHistoricCurrencyAndAmount5 = Field(alias='Amount')

    # Benefit type, in a coded form.
    type: str = Field(alias='Type')
    class Config:
        arbitrary_types_allowed = True
