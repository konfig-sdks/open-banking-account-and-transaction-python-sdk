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


class OBFeeFrequency1Code1(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    How often is the overdraft fee/charge calculated for the account.
    """


    class MetaOapg:
        enum_value_to_name = {
            "FEAC": "FEAC",
            "FEAO": "FEAO",
            "FECP": "FECP",
            "FEDA": "FEDA",
            "FEHO": "FEHO",
            "FEI": "FEI",
            "FEMO": "FEMO",
            "FEOA": "FEOA",
            "FEOT": "FEOT",
            "FEPC": "FEPC",
            "FEPH": "FEPH",
            "FEPO": "FEPO",
            "FEPS": "FEPS",
            "FEPT": "FEPT",
            "FEPTA": "FEPTA",
            "FEPTP": "FEPTP",
            "FEQU": "FEQU",
            "FESM": "FESM",
            "FEST": "FEST",
            "FEWE": "FEWE",
            "FEYE": "FEYE",
        }
    
    @schemas.classproperty
    def FEAC(cls):
        return cls("FEAC")
    
    @schemas.classproperty
    def FEAO(cls):
        return cls("FEAO")
    
    @schemas.classproperty
    def FECP(cls):
        return cls("FECP")
    
    @schemas.classproperty
    def FEDA(cls):
        return cls("FEDA")
    
    @schemas.classproperty
    def FEHO(cls):
        return cls("FEHO")
    
    @schemas.classproperty
    def FEI(cls):
        return cls("FEI")
    
    @schemas.classproperty
    def FEMO(cls):
        return cls("FEMO")
    
    @schemas.classproperty
    def FEOA(cls):
        return cls("FEOA")
    
    @schemas.classproperty
    def FEOT(cls):
        return cls("FEOT")
    
    @schemas.classproperty
    def FEPC(cls):
        return cls("FEPC")
    
    @schemas.classproperty
    def FEPH(cls):
        return cls("FEPH")
    
    @schemas.classproperty
    def FEPO(cls):
        return cls("FEPO")
    
    @schemas.classproperty
    def FEPS(cls):
        return cls("FEPS")
    
    @schemas.classproperty
    def FEPT(cls):
        return cls("FEPT")
    
    @schemas.classproperty
    def FEPTA(cls):
        return cls("FEPTA")
    
    @schemas.classproperty
    def FEPTP(cls):
        return cls("FEPTP")
    
    @schemas.classproperty
    def FEQU(cls):
        return cls("FEQU")
    
    @schemas.classproperty
    def FESM(cls):
        return cls("FESM")
    
    @schemas.classproperty
    def FEST(cls):
        return cls("FEST")
    
    @schemas.classproperty
    def FEWE(cls):
        return cls("FEWE")
    
    @schemas.classproperty
    def FEYE(cls):
        return cls("FEYE")
