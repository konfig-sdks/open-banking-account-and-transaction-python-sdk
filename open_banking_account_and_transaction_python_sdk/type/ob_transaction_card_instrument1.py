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


class RequiredOBTransactionCardInstrument1(TypedDict):
    # Name of the card scheme.
    CardSchemeName: str

class OptionalOBTransactionCardInstrument1(TypedDict, total=False):
    # The card authorisation type.
    AuthorisationType: str

    # Identification assigned by an institution to identify the card instrument used in the transaction. This identification is known by the account owner, and may be masked.
    Identification: str

    # Name of the cardholder using the card instrument.
    Name: str

class OBTransactionCardInstrument1(RequiredOBTransactionCardInstrument1, OptionalOBTransactionCardInstrument1):
    pass
