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


class OBReadStandingOrder6(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Data",
        }
        
        class properties:
        
            @staticmethod
            def Data() -> typing.Type['OBReadStandingOrder6Data']:
                return OBReadStandingOrder6Data
        
            @staticmethod
            def Links() -> typing.Type['Links']:
                return Links
        
            @staticmethod
            def Meta() -> typing.Type['Meta']:
                return Meta
            __annotations__ = {
                "Data": Data,
                "Links": Links,
                "Meta": Meta,
            }
    
    Data: 'OBReadStandingOrder6Data'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Data"]) -> 'OBReadStandingOrder6Data': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Links"]) -> 'Links': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Data", "Links", "Meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Data"]) -> 'OBReadStandingOrder6Data': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Links"]) -> typing.Union['Links', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Data", "Links", "Meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Data: 'OBReadStandingOrder6Data',
        Links: typing.Union['Links', schemas.Unset] = schemas.unset,
        Meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadStandingOrder6':
        return super().__new__(
            cls,
            *args,
            Data=Data,
            Links=Links,
            Meta=Meta,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.links import Links
from open_banking_account_and_transaction_python_sdk.model.meta import Meta
from open_banking_account_and_transaction_python_sdk.model.ob_read_standing_order6_data import OBReadStandingOrder6Data
