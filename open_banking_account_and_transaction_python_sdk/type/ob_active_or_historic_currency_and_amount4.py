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

from open_banking_account_and_transaction_python_sdk.type.active_or_historic_currency_code1 import ActiveOrHistoricCurrencyCode1
from open_banking_account_and_transaction_python_sdk.type.ob_active_currency_and_amount_simple_type import OBActiveCurrencyAndAmountSimpleType

class RequiredOBActiveOrHistoricCurrencyAndAmount4(TypedDict):
    Amount: OBActiveCurrencyAndAmountSimpleType

    Currency: ActiveOrHistoricCurrencyCode1

class OptionalOBActiveOrHistoricCurrencyAndAmount4(TypedDict, total=False):
    pass

class OBActiveOrHistoricCurrencyAndAmount4(RequiredOBActiveOrHistoricCurrencyAndAmount4, OptionalOBActiveOrHistoricCurrencyAndAmount4):
    pass
