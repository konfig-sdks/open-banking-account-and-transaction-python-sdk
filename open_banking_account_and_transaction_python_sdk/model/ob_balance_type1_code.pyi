# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from open_banking_account_and_transaction_python_sdk import schemas  # noqa: F401


class OBBalanceType1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Balance type, in a coded form.
    """
    
    @schemas.classproperty
    def CLOSING_AVAILABLE(cls):
        return cls("ClosingAvailable")
    
    @schemas.classproperty
    def CLOSING_BOOKED(cls):
        return cls("ClosingBooked")
    
    @schemas.classproperty
    def CLOSING_CLEARED(cls):
        return cls("ClosingCleared")
    
    @schemas.classproperty
    def EXPECTED(cls):
        return cls("Expected")
    
    @schemas.classproperty
    def FORWARD_AVAILABLE(cls):
        return cls("ForwardAvailable")
    
    @schemas.classproperty
    def INFORMATION(cls):
        return cls("Information")
    
    @schemas.classproperty
    def INTERIM_AVAILABLE(cls):
        return cls("InterimAvailable")
    
    @schemas.classproperty
    def INTERIM_BOOKED(cls):
        return cls("InterimBooked")
    
    @schemas.classproperty
    def INTERIM_CLEARED(cls):
        return cls("InterimCleared")
    
    @schemas.classproperty
    def OPENING_AVAILABLE(cls):
        return cls("OpeningAvailable")
    
    @schemas.classproperty
    def OPENING_BOOKED(cls):
        return cls("OpeningBooked")
    
    @schemas.classproperty
    def OPENING_CLEARED(cls):
        return cls("OpeningCleared")
    
    @schemas.classproperty
    def PREVIOUSLY_CLOSED_BOOKED(cls):
        return cls("PreviouslyClosedBooked")
