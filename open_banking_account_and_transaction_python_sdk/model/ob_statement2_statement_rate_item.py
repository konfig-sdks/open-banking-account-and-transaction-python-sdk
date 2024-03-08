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


class OBStatement2StatementRateItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Set of elements used to provide details of a generic rate related to the statement resource.
    """


    class MetaOapg:
        required = {
            "Type",
            "Rate",
        }
        
        class properties:
        
            @staticmethod
            def Rate() -> typing.Type['Rate']:
                return Rate
            Type = schemas.StrSchema
            __annotations__ = {
                "Rate": Rate,
                "Type": Type,
            }
    
    Type: MetaOapg.properties.Type
    Rate: 'Rate'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rate"]) -> 'Rate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Rate", "Type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rate"]) -> 'Rate': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Rate", "Type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Rate: 'Rate',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBStatement2StatementRateItem':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Rate=Rate,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.rate import Rate
