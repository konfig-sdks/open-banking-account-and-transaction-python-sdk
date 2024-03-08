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
from open_banking_account_and_transaction_python_sdk.pydantic.ob_external_statement_type1_code import OBExternalStatementType1Code
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_amount import OBStatement2DetailStatementAmount
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_benefit import OBStatement2DetailStatementBenefit
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_date_time import OBStatement2DetailStatementDateTime
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_description import OBStatement2DetailStatementDescription
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_fee import OBStatement2DetailStatementFee
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_interest import OBStatement2DetailStatementInterest
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_rate import OBStatement2DetailStatementRate
from open_banking_account_and_transaction_python_sdk.pydantic.ob_statement2_detail_statement_value import OBStatement2DetailStatementValue
from open_banking_account_and_transaction_python_sdk.pydantic.statement_id import StatementId
from open_banking_account_and_transaction_python_sdk.pydantic.statement_reference import StatementReference

class OBStatement2Detail(BaseModel):
    account_id: AccountId = Field(alias='AccountId')

    # Date and time at which the resource was created.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    creation_date_time: datetime = Field(alias='CreationDateTime')

    # Date and time at which the statement period ends.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    end_date_time: datetime = Field(alias='EndDateTime')

    # Date and time at which the statement period starts.All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00
    start_date_time: datetime = Field(alias='StartDateTime')

    type: OBExternalStatementType1Code = Field(alias='Type')

    statement_amount: typing.Optional[OBStatement2DetailStatementAmount] = Field(None, alias='StatementAmount')

    statement_benefit: typing.Optional[OBStatement2DetailStatementBenefit] = Field(None, alias='StatementBenefit')

    statement_date_time: typing.Optional[OBStatement2DetailStatementDateTime] = Field(None, alias='StatementDateTime')

    statement_description: typing.Optional[OBStatement2DetailStatementDescription] = Field(None, alias='StatementDescription')

    statement_fee: typing.Optional[OBStatement2DetailStatementFee] = Field(None, alias='StatementFee')

    statement_id: typing.Optional[StatementId] = Field(None, alias='StatementId')

    statement_interest: typing.Optional[OBStatement2DetailStatementInterest] = Field(None, alias='StatementInterest')

    statement_rate: typing.Optional[OBStatement2DetailStatementRate] = Field(None, alias='StatementRate')

    statement_reference: typing.Optional[StatementReference] = Field(None, alias='StatementReference')

    statement_value: typing.Optional[OBStatement2DetailStatementValue] = Field(None, alias='StatementValue')
    class Config:
        arbitrary_types_allowed = True