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

from open_banking_account_and_transaction_python_sdk.type.email_address import EmailAddress
from open_banking_account_and_transaction_python_sdk.type.full_legal_name import FullLegalName
from open_banking_account_and_transaction_python_sdk.type.name3 import Name3
from open_banking_account_and_transaction_python_sdk.type.ob_external_party_type1_code import OBExternalPartyType1Code
from open_banking_account_and_transaction_python_sdk.type.ob_party2_address import OBParty2Address
from open_banking_account_and_transaction_python_sdk.type.ob_party_relationships1 import OBPartyRelationships1
from open_banking_account_and_transaction_python_sdk.type.party_id import PartyId
from open_banking_account_and_transaction_python_sdk.type.party_number import PartyNumber
from open_banking_account_and_transaction_python_sdk.type.phone_number0 import PhoneNumber0
from open_banking_account_and_transaction_python_sdk.type.phone_number1 import PhoneNumber1

class RequiredOBParty2(TypedDict):
    PartyId: PartyId

class OptionalOBParty2(TypedDict, total=False):
    # A party’s role with respect to the related account.
    AccountRole: str

    Address: OBParty2Address

    BeneficialOwnership: bool

    EmailAddress: EmailAddress

    FullLegalName: FullLegalName

    # Legal standing of the party.
    LegalStructure: str

    Mobile: PhoneNumber1

    Name: Name3

    PartyNumber: PartyNumber

    PartyType: OBExternalPartyType1Code

    Phone: PhoneNumber0

    Relationships: OBPartyRelationships1

class OBParty2(RequiredOBParty2, OptionalOBParty2):
    pass