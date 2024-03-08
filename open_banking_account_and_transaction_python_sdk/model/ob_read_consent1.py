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


class OBReadConsent1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "Risk",
            "Data",
        }
        
        class properties:
        
            @staticmethod
            def Data() -> typing.Type['OBReadConsent1Data']:
                return OBReadConsent1Data
            Risk = schemas.DictSchema
            __annotations__ = {
                "Data": Data,
                "Risk": Risk,
            }
    
    Risk: MetaOapg.properties.Risk
    Data: 'OBReadConsent1Data'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Data"]) -> 'OBReadConsent1Data': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Risk"]) -> MetaOapg.properties.Risk: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Data", "Risk", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Data"]) -> 'OBReadConsent1Data': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Risk"]) -> MetaOapg.properties.Risk: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Data", "Risk", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Risk: typing.Union[MetaOapg.properties.Risk, dict, frozendict.frozendict, ],
        Data: 'OBReadConsent1Data',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadConsent1':
        return super().__new__(
            cls,
            *args,
            Risk=Risk,
            Data=Data,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_read_consent1_data import OBReadConsent1Data
