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
from open_banking_account_and_transaction_python_sdk.pydantic.beneficiary_id import BeneficiaryId
from open_banking_account_and_transaction_python_sdk.pydantic.ob_beneficiary_type1_code import OBBeneficiaryType1Code
from open_banking_account_and_transaction_python_sdk.pydantic.ob_supplementary_data1 import OBSupplementaryData1
from open_banking_account_and_transaction_python_sdk.pydantic.reference import Reference

class OBBeneficiary5Basic(BaseModel):
    account_id: typing.Optional[AccountId] = Field(None, alias='AccountId')

    beneficiary_id: typing.Optional[BeneficiaryId] = Field(None, alias='BeneficiaryId')

    beneficiary_type: typing.Optional[OBBeneficiaryType1Code] = Field(None, alias='BeneficiaryType')

    reference: typing.Optional[Reference] = Field(None, alias='Reference')

    supplementary_data: typing.Optional[OBSupplementaryData1] = Field(None, alias='SupplementaryData')
    class Config:
        arbitrary_types_allowed = True
