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

from open_banking_account_and_transaction_python_sdk.type.obpca_data1_credit_interest import OBPCAData1CreditInterest
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_other_fees_charges import OBPCAData1OtherFeesCharges
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_overdraft import OBPCAData1Overdraft
from open_banking_account_and_transaction_python_sdk.type.obpca_data1_product_details import OBPCAData1ProductDetails

class RequiredOBPCAData1(TypedDict):
    pass

class OptionalOBPCAData1(TypedDict, total=False):
    CreditInterest: OBPCAData1CreditInterest

    OtherFeesCharges: OBPCAData1OtherFeesCharges

    Overdraft: OBPCAData1Overdraft

    ProductDetails: OBPCAData1ProductDetails

class OBPCAData1(RequiredOBPCAData1, OptionalOBPCAData1):
    pass
