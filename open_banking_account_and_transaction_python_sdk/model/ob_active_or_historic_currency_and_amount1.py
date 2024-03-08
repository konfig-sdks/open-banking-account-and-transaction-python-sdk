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


class OBActiveOrHistoricCurrencyAndAmount1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
    """


    class MetaOapg:
        required = {
            "Amount",
            "Currency",
        }
        
        class properties:
        
            @staticmethod
            def Amount() -> typing.Type['OBActiveCurrencyAndAmountSimpleType']:
                return OBActiveCurrencyAndAmountSimpleType
        
            @staticmethod
            def Currency() -> typing.Type['ActiveOrHistoricCurrencyCode1']:
                return ActiveOrHistoricCurrencyCode1
            __annotations__ = {
                "Amount": Amount,
                "Currency": Currency,
            }
    
    Amount: 'OBActiveCurrencyAndAmountSimpleType'
    Currency: 'ActiveOrHistoricCurrencyCode1'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveCurrencyAndAmountSimpleType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Amount", "Currency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> 'OBActiveCurrencyAndAmountSimpleType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode1': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Amount", "Currency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Amount: 'OBActiveCurrencyAndAmountSimpleType',
        Currency: 'ActiveOrHistoricCurrencyCode1',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBActiveOrHistoricCurrencyAndAmount1':
        return super().__new__(
            cls,
            *args,
            Amount=Amount,
            Currency=Currency,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.active_or_historic_currency_code1 import ActiveOrHistoricCurrencyCode1
from open_banking_account_and_transaction_python_sdk.model.ob_active_currency_and_amount_simple_type import OBActiveCurrencyAndAmountSimpleType
