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


class OBBranchAndFinancialInstitutionIdentification61(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Financial institution servicing an account for the creditor.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def Identification() -> typing.Type['Identification2']:
                return Identification2
        
            @staticmethod
            def Name() -> typing.Type['Name1']:
                return Name1
        
            @staticmethod
            def PostalAddress() -> typing.Type['OBPostalAddress6']:
                return OBPostalAddress6
            SchemeName = schemas.StrSchema
            __annotations__ = {
                "Identification": Identification,
                "Name": Name,
                "PostalAddress": PostalAddress,
                "SchemeName": SchemeName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> 'Identification2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PostalAddress"]) -> 'OBPostalAddress6': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Identification", "Name", "PostalAddress", "SchemeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> typing.Union['Identification2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union['Name1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PostalAddress"]) -> typing.Union['OBPostalAddress6', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SchemeName"]) -> typing.Union[MetaOapg.properties.SchemeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Identification", "Name", "PostalAddress", "SchemeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Identification: typing.Union['Identification2', schemas.Unset] = schemas.unset,
        Name: typing.Union['Name1', schemas.Unset] = schemas.unset,
        PostalAddress: typing.Union['OBPostalAddress6', schemas.Unset] = schemas.unset,
        SchemeName: typing.Union[MetaOapg.properties.SchemeName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBranchAndFinancialInstitutionIdentification61':
        return super().__new__(
            cls,
            *args,
            Identification=Identification,
            Name=Name,
            PostalAddress=PostalAddress,
            SchemeName=SchemeName,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.identification2 import Identification2
from open_banking_account_and_transaction_python_sdk.model.name1 import Name1
from open_banking_account_and_transaction_python_sdk.model.ob_postal_address6 import OBPostalAddress6
