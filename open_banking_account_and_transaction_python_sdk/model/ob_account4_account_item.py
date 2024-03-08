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


class OBAccount4AccountItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides the details to identify an account.
    """


    class MetaOapg:
        required = {
            "Identification",
            "SchemeName",
        }
        
        class properties:
        
            @staticmethod
            def Identification() -> typing.Type['Identification0']:
                return Identification0
            SchemeName = schemas.StrSchema
        
            @staticmethod
            def Name() -> typing.Type['Name0']:
                return Name0
        
            @staticmethod
            def SecondaryIdentification() -> typing.Type['SecondaryIdentification']:
                return SecondaryIdentification
            __annotations__ = {
                "Identification": Identification,
                "SchemeName": SchemeName,
                "Name": Name,
                "SecondaryIdentification": SecondaryIdentification,
            }
    
    Identification: 'Identification0'
    SchemeName: MetaOapg.properties.SchemeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> 'Identification0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SecondaryIdentification"]) -> 'SecondaryIdentification': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Identification", "SchemeName", "Name", "SecondaryIdentification", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> 'Identification0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union['Name0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SecondaryIdentification"]) -> typing.Union['SecondaryIdentification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Identification", "SchemeName", "Name", "SecondaryIdentification", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Identification: 'Identification0',
        SchemeName: typing.Union[MetaOapg.properties.SchemeName, str, ],
        Name: typing.Union['Name0', schemas.Unset] = schemas.unset,
        SecondaryIdentification: typing.Union['SecondaryIdentification', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBAccount4AccountItem':
        return super().__new__(
            cls,
            *args,
            Identification=Identification,
            SchemeName=SchemeName,
            Name=Name,
            SecondaryIdentification=SecondaryIdentification,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.identification0 import Identification0
from open_banking_account_and_transaction_python_sdk.model.name0 import Name0
from open_banking_account_and_transaction_python_sdk.model.secondary_identification import SecondaryIdentification
