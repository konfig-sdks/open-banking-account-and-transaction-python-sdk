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


class OBScheduledPayment3Basic(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "AccountId",
            "InstructedAmount",
            "ScheduledPaymentDateTime",
            "ScheduledType",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def InstructedAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount1']:
                return OBActiveOrHistoricCurrencyAndAmount1
            ScheduledPaymentDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def ScheduledType() -> typing.Type['OBExternalScheduleType1Code']:
                return OBExternalScheduleType1Code
        
            @staticmethod
            def DebtorReference() -> typing.Type['DebtorReference']:
                return DebtorReference
        
            @staticmethod
            def Reference() -> typing.Type['Reference']:
                return Reference
        
            @staticmethod
            def ScheduledPaymentId() -> typing.Type['ScheduledPaymentId']:
                return ScheduledPaymentId
            __annotations__ = {
                "AccountId": AccountId,
                "InstructedAmount": InstructedAmount,
                "ScheduledPaymentDateTime": ScheduledPaymentDateTime,
                "ScheduledType": ScheduledType,
                "DebtorReference": DebtorReference,
                "Reference": Reference,
                "ScheduledPaymentId": ScheduledPaymentId,
            }
    
    AccountId: 'AccountId'
    InstructedAmount: 'OBActiveOrHistoricCurrencyAndAmount1'
    ScheduledPaymentDateTime: MetaOapg.properties.ScheduledPaymentDateTime
    ScheduledType: 'OBExternalScheduleType1Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InstructedAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ScheduledPaymentDateTime"]) -> MetaOapg.properties.ScheduledPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ScheduledType"]) -> 'OBExternalScheduleType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DebtorReference"]) -> 'DebtorReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Reference"]) -> 'Reference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ScheduledPaymentId"]) -> 'ScheduledPaymentId': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "InstructedAmount", "ScheduledPaymentDateTime", "ScheduledType", "DebtorReference", "Reference", "ScheduledPaymentId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InstructedAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount1': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ScheduledPaymentDateTime"]) -> MetaOapg.properties.ScheduledPaymentDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ScheduledType"]) -> 'OBExternalScheduleType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DebtorReference"]) -> typing.Union['DebtorReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Reference"]) -> typing.Union['Reference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ScheduledPaymentId"]) -> typing.Union['ScheduledPaymentId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "InstructedAmount", "ScheduledPaymentDateTime", "ScheduledType", "DebtorReference", "Reference", "ScheduledPaymentId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: 'AccountId',
        InstructedAmount: 'OBActiveOrHistoricCurrencyAndAmount1',
        ScheduledPaymentDateTime: typing.Union[MetaOapg.properties.ScheduledPaymentDateTime, str, datetime, ],
        ScheduledType: 'OBExternalScheduleType1Code',
        DebtorReference: typing.Union['DebtorReference', schemas.Unset] = schemas.unset,
        Reference: typing.Union['Reference', schemas.Unset] = schemas.unset,
        ScheduledPaymentId: typing.Union['ScheduledPaymentId', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBScheduledPayment3Basic':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            InstructedAmount=InstructedAmount,
            ScheduledPaymentDateTime=ScheduledPaymentDateTime,
            ScheduledType=ScheduledType,
            DebtorReference=DebtorReference,
            Reference=Reference,
            ScheduledPaymentId=ScheduledPaymentId,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.model.debtor_reference import DebtorReference
from open_banking_account_and_transaction_python_sdk.model.ob_active_or_historic_currency_and_amount1 import OBActiveOrHistoricCurrencyAndAmount1
from open_banking_account_and_transaction_python_sdk.model.ob_external_schedule_type1_code import OBExternalScheduleType1Code
from open_banking_account_and_transaction_python_sdk.model.reference import Reference
from open_banking_account_and_transaction_python_sdk.model.scheduled_payment_id import ScheduledPaymentId
