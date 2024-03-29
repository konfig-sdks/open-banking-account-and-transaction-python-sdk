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


class OBAccount4Basic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Unambiguous identification of the account to which credit and debit entries are made.
    """


    class MetaOapg:
        required = {
            "AccountId",
            "Currency",
            "AccountType",
            "AccountSubType",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def AccountSubType() -> typing.Type['OBExternalAccountSubType1Code']:
                return OBExternalAccountSubType1Code
        
            @staticmethod
            def AccountType() -> typing.Type['OBExternalAccountType1Code']:
                return OBExternalAccountType1Code
        
            @staticmethod
            def Currency() -> typing.Type['ActiveOrHistoricCurrencyCode0']:
                return ActiveOrHistoricCurrencyCode0
        
            @staticmethod
            def Description() -> typing.Type['Description0']:
                return Description0
        
            @staticmethod
            def Nickname() -> typing.Type['Nickname']:
                return Nickname
        
            @staticmethod
            def Status() -> typing.Type['OBAccountStatus1Code']:
                return OBAccountStatus1Code
            StatusUpdateDateTime = schemas.DateTimeSchema
            __annotations__ = {
                "AccountId": AccountId,
                "AccountSubType": AccountSubType,
                "AccountType": AccountType,
                "Currency": Currency,
                "Description": Description,
                "Nickname": Nickname,
                "Status": Status,
                "StatusUpdateDateTime": StatusUpdateDateTime,
            }
    
    AccountId: 'AccountId'
    Currency: 'ActiveOrHistoricCurrencyCode0'
    AccountType: 'OBExternalAccountType1Code'
    AccountSubType: 'OBExternalAccountSubType1Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountSubType"]) -> 'OBExternalAccountSubType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountType"]) -> 'OBExternalAccountType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> 'Description0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Nickname"]) -> 'Nickname': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Status"]) -> 'OBAccountStatus1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatusUpdateDateTime"]) -> MetaOapg.properties.StatusUpdateDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "AccountSubType", "AccountType", "Currency", "Description", "Nickname", "Status", "StatusUpdateDateTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountSubType"]) -> 'OBExternalAccountSubType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountType"]) -> 'OBExternalAccountType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Currency"]) -> 'ActiveOrHistoricCurrencyCode0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union['Description0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Nickname"]) -> typing.Union['Nickname', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Status"]) -> typing.Union['OBAccountStatus1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatusUpdateDateTime"]) -> typing.Union[MetaOapg.properties.StatusUpdateDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "AccountSubType", "AccountType", "Currency", "Description", "Nickname", "Status", "StatusUpdateDateTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: 'AccountId',
        Currency: 'ActiveOrHistoricCurrencyCode0',
        AccountType: 'OBExternalAccountType1Code',
        AccountSubType: 'OBExternalAccountSubType1Code',
        Description: typing.Union['Description0', schemas.Unset] = schemas.unset,
        Nickname: typing.Union['Nickname', schemas.Unset] = schemas.unset,
        Status: typing.Union['OBAccountStatus1Code', schemas.Unset] = schemas.unset,
        StatusUpdateDateTime: typing.Union[MetaOapg.properties.StatusUpdateDateTime, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBAccount4Basic':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            Currency=Currency,
            AccountType=AccountType,
            AccountSubType=AccountSubType,
            Description=Description,
            Nickname=Nickname,
            Status=Status,
            StatusUpdateDateTime=StatusUpdateDateTime,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.model.active_or_historic_currency_code0 import ActiveOrHistoricCurrencyCode0
from open_banking_account_and_transaction_python_sdk.model.description0 import Description0
from open_banking_account_and_transaction_python_sdk.model.nickname import Nickname
from open_banking_account_and_transaction_python_sdk.model.ob_account_status1_code import OBAccountStatus1Code
from open_banking_account_and_transaction_python_sdk.model.ob_external_account_sub_type1_code import OBExternalAccountSubType1Code
from open_banking_account_and_transaction_python_sdk.model.ob_external_account_type1_code import OBExternalAccountType1Code
