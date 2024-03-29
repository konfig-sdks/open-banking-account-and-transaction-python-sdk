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


class OBOverdraftFeeType1Code(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Overdraft fee type
    """


    class MetaOapg:
        enum_value_to_name = {
            "FBAO": "FBAO",
            "FBAR": "FBAR",
            "FBEB": "FBEB",
            "FBIT": "FBIT",
            "FBOR": "FBOR",
            "FBOS": "FBOS",
            "FBSC": "FBSC",
            "FBTO": "FBTO",
            "FBUB": "FBUB",
            "FBUT": "FBUT",
            "FTOT": "FTOT",
            "FTUT": "FTUT",
        }
    
    @schemas.classproperty
    def FBAO(cls):
        return cls("FBAO")
    
    @schemas.classproperty
    def FBAR(cls):
        return cls("FBAR")
    
    @schemas.classproperty
    def FBEB(cls):
        return cls("FBEB")
    
    @schemas.classproperty
    def FBIT(cls):
        return cls("FBIT")
    
    @schemas.classproperty
    def FBOR(cls):
        return cls("FBOR")
    
    @schemas.classproperty
    def FBOS(cls):
        return cls("FBOS")
    
    @schemas.classproperty
    def FBSC(cls):
        return cls("FBSC")
    
    @schemas.classproperty
    def FBTO(cls):
        return cls("FBTO")
    
    @schemas.classproperty
    def FBUB(cls):
        return cls("FBUB")
    
    @schemas.classproperty
    def FBUT(cls):
        return cls("FBUT")
    
    @schemas.classproperty
    def FTOT(cls):
        return cls("FTOT")
    
    @schemas.classproperty
    def FTUT(cls):
        return cls("FTUT")
