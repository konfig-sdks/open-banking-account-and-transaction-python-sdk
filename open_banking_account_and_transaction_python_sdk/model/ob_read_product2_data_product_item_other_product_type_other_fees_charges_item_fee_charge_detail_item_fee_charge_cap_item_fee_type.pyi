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


class OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeType(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def FEPF(cls):
                return cls("FEPF")
            
            @schemas.classproperty
            def FTOT(cls):
                return cls("FTOT")
            
            @schemas.classproperty
            def FYAF(cls):
                return cls("FYAF")
            
            @schemas.classproperty
            def FYAM(cls):
                return cls("FYAM")
            
            @schemas.classproperty
            def FYAQ(cls):
                return cls("FYAQ")
            
            @schemas.classproperty
            def FYCP(cls):
                return cls("FYCP")
            
            @schemas.classproperty
            def FYDB(cls):
                return cls("FYDB")
            
            @schemas.classproperty
            def FYMI(cls):
                return cls("FYMI")
            
            @schemas.classproperty
            def FYXX(cls):
                return cls("FYXX")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeType':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
