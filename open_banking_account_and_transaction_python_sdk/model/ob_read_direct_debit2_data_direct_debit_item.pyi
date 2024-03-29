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


class OBReadDirectDebit2DataDirectDebitItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Account to or from which a cash entry is made.
    """


    class MetaOapg:
        required = {
            "AccountId",
            "MandateIdentification",
            "Name",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
        
            @staticmethod
            def MandateIdentification() -> typing.Type['MandateIdentification']:
                return MandateIdentification
        
            @staticmethod
            def Name() -> typing.Type['Name2']:
                return Name2
        
            @staticmethod
            def DirectDebitId() -> typing.Type['DirectDebitId']:
                return DirectDebitId
        
            @staticmethod
            def DirectDebitStatusCode() -> typing.Type['OBExternalDirectDebitStatus1Code']:
                return OBExternalDirectDebitStatus1Code
            Frequency = schemas.StrSchema
        
            @staticmethod
            def PreviousPaymentAmount() -> typing.Type['OBActiveOrHistoricCurrencyAndAmount0']:
                return OBActiveOrHistoricCurrencyAndAmount0
            PreviousPaymentDateTime = schemas.DateTimeSchema
            __annotations__ = {
                "AccountId": AccountId,
                "MandateIdentification": MandateIdentification,
                "Name": Name,
                "DirectDebitId": DirectDebitId,
                "DirectDebitStatusCode": DirectDebitStatusCode,
                "Frequency": Frequency,
                "PreviousPaymentAmount": PreviousPaymentAmount,
                "PreviousPaymentDateTime": PreviousPaymentDateTime,
            }
    
    AccountId: 'AccountId'
    MandateIdentification: 'MandateIdentification'
    Name: 'Name2'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MandateIdentification"]) -> 'MandateIdentification': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name2': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DirectDebitId"]) -> 'DirectDebitId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DirectDebitStatusCode"]) -> 'OBExternalDirectDebitStatus1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Frequency"]) -> MetaOapg.properties.Frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PreviousPaymentAmount"]) -> 'OBActiveOrHistoricCurrencyAndAmount0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PreviousPaymentDateTime"]) -> MetaOapg.properties.PreviousPaymentDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "MandateIdentification", "Name", "DirectDebitId", "DirectDebitStatusCode", "Frequency", "PreviousPaymentAmount", "PreviousPaymentDateTime", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MandateIdentification"]) -> 'MandateIdentification': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> 'Name2': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DirectDebitId"]) -> typing.Union['DirectDebitId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DirectDebitStatusCode"]) -> typing.Union['OBExternalDirectDebitStatus1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Frequency"]) -> typing.Union[MetaOapg.properties.Frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PreviousPaymentAmount"]) -> typing.Union['OBActiveOrHistoricCurrencyAndAmount0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PreviousPaymentDateTime"]) -> typing.Union[MetaOapg.properties.PreviousPaymentDateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "MandateIdentification", "Name", "DirectDebitId", "DirectDebitStatusCode", "Frequency", "PreviousPaymentAmount", "PreviousPaymentDateTime", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: 'AccountId',
        MandateIdentification: 'MandateIdentification',
        Name: 'Name2',
        DirectDebitId: typing.Union['DirectDebitId', schemas.Unset] = schemas.unset,
        DirectDebitStatusCode: typing.Union['OBExternalDirectDebitStatus1Code', schemas.Unset] = schemas.unset,
        Frequency: typing.Union[MetaOapg.properties.Frequency, str, schemas.Unset] = schemas.unset,
        PreviousPaymentAmount: typing.Union['OBActiveOrHistoricCurrencyAndAmount0', schemas.Unset] = schemas.unset,
        PreviousPaymentDateTime: typing.Union[MetaOapg.properties.PreviousPaymentDateTime, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadDirectDebit2DataDirectDebitItem':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            MandateIdentification=MandateIdentification,
            Name=Name,
            DirectDebitId=DirectDebitId,
            DirectDebitStatusCode=DirectDebitStatusCode,
            Frequency=Frequency,
            PreviousPaymentAmount=PreviousPaymentAmount,
            PreviousPaymentDateTime=PreviousPaymentDateTime,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.model.direct_debit_id import DirectDebitId
from open_banking_account_and_transaction_python_sdk.model.mandate_identification import MandateIdentification
from open_banking_account_and_transaction_python_sdk.model.name2 import Name2
from open_banking_account_and_transaction_python_sdk.model.ob_active_or_historic_currency_and_amount0 import OBActiveOrHistoricCurrencyAndAmount0
from open_banking_account_and_transaction_python_sdk.model.ob_external_direct_debit_status1_code import OBExternalDirectDebitStatus1Code
