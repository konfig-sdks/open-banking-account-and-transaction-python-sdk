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


class RequiredOBError1(TypedDict):
    # Low level textual error code, e.g., UK.OBIE.Field.Missing
    ErrorCode: str

    # A description of the error that occurred. e.g., 'A mandatory field isn't supplied' or 'RequestedExecutionDateTime must be in future' OBIE doesn't standardise this field
    Message: str

class OptionalOBError1(TypedDict, total=False):
    # Recommended but optional reference to the JSON Path of the field with error, e.g., Data.Initiation.InstructedAmount.Currency
    Path: str

    # URL to help remediate the problem, or provide more information, or to API Reference, or help etc
    Url: str

class OBError1(RequiredOBError1, OptionalOBError1):
    pass
