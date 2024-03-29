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


class OBBCAData1ProductDetailsSegment(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.

Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd 
With respect to BCA products, they are segmented in relation to different markets that they wish to focus on. 
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "ClientAccount": "CLIENT_ACCOUNT",
                    "Standard": "STANDARD",
                    "NonCommercialChaitiesClbSoc": "NON_COMMERCIAL_CHAITIES_CLB_SOC",
                    "NonCommercialPublicAuthGovt": "NON_COMMERCIAL_PUBLIC_AUTH_GOVT",
                    "Religious": "RELIGIOUS",
                    "SectorSpecific": "SECTOR_SPECIFIC",
                    "Startup": "STARTUP",
                    "Switcher": "SWITCHER",
                }
            
            @schemas.classproperty
            def CLIENT_ACCOUNT(cls):
                return cls("ClientAccount")
            
            @schemas.classproperty
            def STANDARD(cls):
                return cls("Standard")
            
            @schemas.classproperty
            def NON_COMMERCIAL_CHAITIES_CLB_SOC(cls):
                return cls("NonCommercialChaitiesClbSoc")
            
            @schemas.classproperty
            def NON_COMMERCIAL_PUBLIC_AUTH_GOVT(cls):
                return cls("NonCommercialPublicAuthGovt")
            
            @schemas.classproperty
            def RELIGIOUS(cls):
                return cls("Religious")
            
            @schemas.classproperty
            def SECTOR_SPECIFIC(cls):
                return cls("SectorSpecific")
            
            @schemas.classproperty
            def STARTUP(cls):
                return cls("Startup")
            
            @schemas.classproperty
            def SWITCHER(cls):
                return cls("Switcher")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1ProductDetailsSegment':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
