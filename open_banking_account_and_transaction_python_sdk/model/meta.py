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


class Meta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Meta Data relevant to the payload
    """


    class MetaOapg:
        
        class properties:
            FirstAvailableDateTime = schemas.DateTimeSchema
            LastAvailableDateTime = schemas.DateTimeSchema
            TotalPages = schemas.Int32Schema
            __annotations__ = {
                "FirstAvailableDateTime": FirstAvailableDateTime,
                "LastAvailableDateTime": LastAvailableDateTime,
                "TotalPages": TotalPages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstAvailableDateTime"]) -> MetaOapg.properties.FirstAvailableDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastAvailableDateTime"]) -> MetaOapg.properties.LastAvailableDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TotalPages"]) -> MetaOapg.properties.TotalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FirstAvailableDateTime", "LastAvailableDateTime", "TotalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstAvailableDateTime"]) -> typing.Union[MetaOapg.properties.FirstAvailableDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastAvailableDateTime"]) -> typing.Union[MetaOapg.properties.LastAvailableDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TotalPages"]) -> typing.Union[MetaOapg.properties.TotalPages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FirstAvailableDateTime", "LastAvailableDateTime", "TotalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FirstAvailableDateTime: typing.Union[MetaOapg.properties.FirstAvailableDateTime, str, datetime, schemas.Unset] = schemas.unset,
        LastAvailableDateTime: typing.Union[MetaOapg.properties.LastAvailableDateTime, str, datetime, schemas.Unset] = schemas.unset,
        TotalPages: typing.Union[MetaOapg.properties.TotalPages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Meta':
        return super().__new__(
            cls,
            *args,
            FirstAvailableDateTime=FirstAvailableDateTime,
            LastAvailableDateTime=LastAvailableDateTime,
            TotalPages=TotalPages,
            _configuration=_configuration,
            **kwargs,
        )