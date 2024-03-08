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


class OBBranchAndFinancialInstitutionIdentification50(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.
    """


    class MetaOapg:
        required = {
            "Identification",
            "SchemeName",
        }
        
        class properties:
        
            @staticmethod
            def Identification() -> typing.Type['Identification1']:
                return Identification1
            SchemeName = schemas.StrSchema
            __annotations__ = {
                "Identification": Identification,
                "SchemeName": SchemeName,
            }
    
    Identification: 'Identification1'
    SchemeName: MetaOapg.properties.SchemeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> 'Identification1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Identification", "SchemeName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> 'Identification1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SchemeName"]) -> MetaOapg.properties.SchemeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Identification", "SchemeName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Identification: 'Identification1',
        SchemeName: typing.Union[MetaOapg.properties.SchemeName, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBranchAndFinancialInstitutionIdentification50':
        return super().__new__(
            cls,
            *args,
            Identification=Identification,
            SchemeName=SchemeName,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.identification1 import Identification1
