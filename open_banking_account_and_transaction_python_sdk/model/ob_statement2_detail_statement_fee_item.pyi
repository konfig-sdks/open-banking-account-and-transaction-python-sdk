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


class OBStatement2DetailStatementFeeItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Set of elements used to provide details of a fee for the statement resource.
    """


    class MetaOapg:
        required = {
            "Type",
            "Amount",
            "CreditDebitIndicator",
        }
        
        class properties:
        
            @staticmethod
            def Amount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount6']:
                return OBActiveOrHistoricCurrencyAndAmount6
        
            @staticmethod
            def CreditDebitIndicator() -> typing.Type['OBCreditDebitCode0']:
                return OBCreditDebitCode0
            Type = schemas.StrSchema
        
            @staticmethod
            def Description() -> typing.Type['Description1']:
                return Description1
            Frequency = schemas.StrSchema
            Rate = schemas.NumberSchema
            RateType = schemas.StrSchema
            __annotations__ = {
                "Amount": Amount,
                "CreditDebitIndicator": CreditDebitIndicator,
                "Type": Type,
                "Description": Description,
                "Frequency": Frequency,
                "Rate": Rate,
                "RateType": RateType,
            }
    
    Type: MetaOapg.properties.Type
    Amount: 'OBActiveOrHistoricCurrencyAndAmount6'
    CreditDebitIndicator: 'OBCreditDebitCode0'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveOrHistoricCurrencyAndAmount6': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreditDebitIndicator"]) -> 'OBCreditDebitCode0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> 'Description1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Frequency"]) -> MetaOapg.properties.Frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rate"]) -> MetaOapg.properties.Rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RateType"]) -> MetaOapg.properties.RateType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Amount", "CreditDebitIndicator", "Type", "Description", "Frequency", "Rate", "RateType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveOrHistoricCurrencyAndAmount6': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreditDebitIndicator"]) -> 'OBCreditDebitCode0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union['Description1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Frequency"]) -> typing.Union[MetaOapg.properties.Frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rate"]) -> typing.Union[MetaOapg.properties.Rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RateType"]) -> typing.Union[MetaOapg.properties.RateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Amount", "CreditDebitIndicator", "Type", "Description", "Frequency", "Rate", "RateType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: typing.Union[MetaOapg.properties.Type, str, ],
        Amount: 'OBActiveOrHistoricCurrencyAndAmount6',
        CreditDebitIndicator: 'OBCreditDebitCode0',
        Description: typing.Union['Description1', schemas.Unset] = schemas.unset,
        Frequency: typing.Union[MetaOapg.properties.Frequency, str, schemas.Unset] = schemas.unset,
        Rate: typing.Union[MetaOapg.properties.Rate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        RateType: typing.Union[MetaOapg.properties.RateType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBStatement2DetailStatementFeeItem':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            Amount=Amount,
            CreditDebitIndicator=CreditDebitIndicator,
            Description=Description,
            Frequency=Frequency,
            Rate=Rate,
            RateType=RateType,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.description1 import Description1
from open_banking_account_and_transaction_python_sdk.model.ob_active_or_historic_currency_and_amount6 import OBActiveOrHistoricCurrencyAndAmount6
from open_banking_account_and_transaction_python_sdk.model.ob_credit_debit_code0 import OBCreditDebitCode0
