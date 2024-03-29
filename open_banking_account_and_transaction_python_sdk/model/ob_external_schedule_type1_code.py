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


class OBExternalScheduleType1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Specifies the scheduled payment date type requested
    """


    class MetaOapg:
        enum_value_to_name = {
            "Arrival": "ARRIVAL",
            "Execution": "EXECUTION",
        }
    
    @schemas.classproperty
    def ARRIVAL(cls):
        return cls("Arrival")
    
    @schemas.classproperty
    def EXECUTION(cls):
        return cls("Execution")
