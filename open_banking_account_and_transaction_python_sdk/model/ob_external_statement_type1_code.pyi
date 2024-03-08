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


class OBExternalStatementType1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Statement type, in a coded form.
    """
    
    @schemas.classproperty
    def ACCOUNT_CLOSURE(cls):
        return cls("AccountClosure")
    
    @schemas.classproperty
    def ACCOUNT_OPENING(cls):
        return cls("AccountOpening")
    
    @schemas.classproperty
    def ANNUAL(cls):
        return cls("Annual")
    
    @schemas.classproperty
    def INTERIM(cls):
        return cls("Interim")
    
    @schemas.classproperty
    def REGULAR_PERIODIC(cls):
        return cls("RegularPeriodic")
