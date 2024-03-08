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
from open_banking_account_and_transaction_python_sdk.type.address_line import AddressLine
from open_banking_account_and_transaction_python_sdk.type.ob_active_or_historic_currency_and_amount10 import OBActiveOrHistoricCurrencyAndAmount10
from open_banking_account_and_transaction_python_sdk.type.ob_active_or_historic_currency_and_amount9 import OBActiveOrHistoricCurrencyAndAmount9
from open_banking_account_and_transaction_python_sdk.type.ob_bank_transaction_code_structure1 import OBBankTransactionCodeStructure1
from open_banking_account_and_transaction_python_sdk.type.ob_credit_debit_code1 import OBCreditDebitCode1
from open_banking_account_and_transaction_python_sdk.type.ob_currency_exchange5 import OBCurrencyExchange5
from open_banking_account_and_transaction_python_sdk.type.ob_entry_status1_code import OBEntryStatus1Code
from open_banking_account_and_transaction_python_sdk.type.ob_supplementary_data1 import OBSupplementaryData1
from open_banking_account_and_transaction_python_sdk.type.ob_transaction_card_instrument1 import OBTransactionCardInstrument1
from open_banking_account_and_transaction_python_sdk.type.ob_transaction_mutability1_code import OBTransactionMutability1Code
from open_banking_account_and_transaction_python_sdk.type.proprietary_bank_transaction_code_structure1 import ProprietaryBankTransactionCodeStructure1
from open_banking_account_and_transaction_python_sdk.type.statement_reference import StatementReference
from open_banking_account_and_transaction_python_sdk.type.transaction_id import TransactionId
from open_banking_account_and_transaction_python_sdk.type.transaction_reference import TransactionReference

class RequiredOBTransaction6Basic(TypedDict):
    AccountId: AccountId

    Amount: OBActiveOrHistoricCurrencyAndAmount9

    # Date and time when a transaction entry is posted to an account on the account servicer's books. Usage: Booking date is the expected booking date, unless the status is booked, in which case it is the actual booking date.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    BookingDateTime: datetime

    CreditDebitIndicator: OBCreditDebitCode1

    Status: OBEntryStatus1Code

class OptionalOBTransaction6Basic(TypedDict, total=False):
    AddressLine: AddressLine

    BankTransactionCode: OBBankTransactionCodeStructure1

    CardInstrument: OBTransactionCardInstrument1

    ChargeAmount: OBActiveOrHistoricCurrencyAndAmount10

    CurrencyExchange: OBCurrencyExchange5

    ProprietaryBankTransactionCode: ProprietaryBankTransactionCodeStructure1

    StatementReference: typing.List[StatementReference]

    SupplementaryData: OBSupplementaryData1

    TransactionId: TransactionId

    TransactionMutability: OBTransactionMutability1Code

    TransactionReference: TransactionReference

    # Date and time at which assets become available to the account owner in case of a credit entry, or cease to be available to the account owner in case of a debit transaction entry. Usage: If transaction entry status is pending and value date is present, then the value date refers to an expected/requested value date. For transaction entries subject to availability/float and for which availability information is provided, the value date must not be used. In this case the availability component identifies the number of availability days.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    ValueDateTime: datetime

class OBTransaction6Basic(RequiredOBTransaction6Basic, OptionalOBTransaction6Basic):
    pass
