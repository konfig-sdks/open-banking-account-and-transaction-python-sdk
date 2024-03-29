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

from open_banking_account_and_transaction_python_sdk.type.obbca_data1_credit_interest import OBBCAData1CreditInterest
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_other_fees_charges import OBBCAData1OtherFeesCharges
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_overdraft import OBBCAData1Overdraft
from open_banking_account_and_transaction_python_sdk.type.obbca_data1_product_details import OBBCAData1ProductDetails

class RequiredOBBCAData1(TypedDict):
    pass

class OptionalOBBCAData1(TypedDict, total=False):
    CreditInterest: OBBCAData1CreditInterest

    OtherFeesCharges: OBBCAData1OtherFeesCharges

    Overdraft: OBBCAData1Overdraft

    ProductDetails: OBBCAData1ProductDetails

class OBBCAData1(RequiredOBBCAData1, OptionalOBBCAData1):
    pass
