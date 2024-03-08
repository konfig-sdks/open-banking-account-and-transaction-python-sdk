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
from open_banking_account_and_transaction_python_sdk.type.debtor_reference import DebtorReference
from open_banking_account_and_transaction_python_sdk.type.ob_active_or_historic_currency_and_amount1 import OBActiveOrHistoricCurrencyAndAmount1
from open_banking_account_and_transaction_python_sdk.type.ob_branch_and_financial_institution_identification51 import OBBranchAndFinancialInstitutionIdentification51
from open_banking_account_and_transaction_python_sdk.type.ob_cash_account51 import OBCashAccount51
from open_banking_account_and_transaction_python_sdk.type.ob_external_schedule_type1_code import OBExternalScheduleType1Code
from open_banking_account_and_transaction_python_sdk.type.reference import Reference
from open_banking_account_and_transaction_python_sdk.type.scheduled_payment_id import ScheduledPaymentId

class RequiredOBScheduledPayment3(TypedDict):
    AccountId: AccountId

    InstructedAmount: OBActiveOrHistoricCurrencyAndAmount1

    # The date on which the scheduled payment will be made.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    ScheduledPaymentDateTime: datetime

    ScheduledType: OBExternalScheduleType1Code

class OptionalOBScheduledPayment3(TypedDict, total=False):
    CreditorAccount: OBCashAccount51

    CreditorAgent: OBBranchAndFinancialInstitutionIdentification51

    DebtorReference: DebtorReference

    Reference: Reference

    ScheduledPaymentId: ScheduledPaymentId

class OBScheduledPayment3(RequiredOBScheduledPayment3, OptionalOBScheduledPayment3):
    pass
