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

from open_banking_account_and_transaction_python_sdk.type.description1 import Description1
from open_banking_account_and_transaction_python_sdk.type.ob_active_or_historic_currency_and_amount6 import OBActiveOrHistoricCurrencyAndAmount6
from open_banking_account_and_transaction_python_sdk.type.ob_credit_debit_code0 import OBCreditDebitCode0

class RequiredOBStatement2BasicStatementFeeItem(TypedDict):
    Amount: OBActiveOrHistoricCurrencyAndAmount6

    CreditDebitIndicator: OBCreditDebitCode0

    # Fee type, in a coded form.
    Type: str

class OptionalOBStatement2BasicStatementFeeItem(TypedDict, total=False):
    Description: Description1

    # How frequently the fee is applied to the Account.
    Frequency: str

    # Rate charged for Statement Fee (where it is charged in terms of a rate rather than an amount)
    Rate: typing.Union[int, float]

    # Description that may be available for the statement fee rate type.
    RateType: str

class OBStatement2BasicStatementFeeItem(RequiredOBStatement2BasicStatementFeeItem, OptionalOBStatement2BasicStatementFeeItem):
    pass
