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


class OBError1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Message",
            "ErrorCode",
        }
        
        class properties:
            ErrorCode = schemas.StrSchema
            
            
            class Message(
                schemas.StrSchema
            ):
                pass
            
            
            class Path(
                schemas.StrSchema
            ):
                pass
            Url = schemas.StrSchema
            __annotations__ = {
                "ErrorCode": ErrorCode,
                "Message": Message,
                "Path": Path,
                "Url": Url,
            }
    
    Message: MetaOapg.properties.Message
    ErrorCode: MetaOapg.properties.ErrorCode
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ErrorCode"]) -> MetaOapg.properties.ErrorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Message"]) -> MetaOapg.properties.Message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Path"]) -> MetaOapg.properties.Path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Url"]) -> MetaOapg.properties.Url: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ErrorCode", "Message", "Path", "Url", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ErrorCode"]) -> MetaOapg.properties.ErrorCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Message"]) -> MetaOapg.properties.Message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Path"]) -> typing.Union[MetaOapg.properties.Path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Url"]) -> typing.Union[MetaOapg.properties.Url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ErrorCode", "Message", "Path", "Url", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Message: typing.Union[MetaOapg.properties.Message, str, ],
        ErrorCode: typing.Union[MetaOapg.properties.ErrorCode, str, ],
        Path: typing.Union[MetaOapg.properties.Path, str, schemas.Unset] = schemas.unset,
        Url: typing.Union[MetaOapg.properties.Url, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBError1':
        return super().__new__(
            cls,
            *args,
            Message=Message,
            ErrorCode=ErrorCode,
            Path=Path,
            Url=Url,
            _configuration=_configuration,
            **kwargs,
        )
