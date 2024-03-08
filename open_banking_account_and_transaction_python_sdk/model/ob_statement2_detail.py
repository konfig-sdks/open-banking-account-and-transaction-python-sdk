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


class OBStatement2Detail(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides further details on a statement resource.
    """


    class MetaOapg:
        required = {
            "Type",
            "AccountId",
            "CreationDateTime",
            "StartDateTime",
            "EndDateTime",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
            CreationDateTime = schemas.DateTimeSchema
            EndDateTime = schemas.DateTimeSchema
            StartDateTime = schemas.DateTimeSchema
        
            @staticmethod
            def Type() -> typing.Type['OBExternalStatementType1Code']:
                return OBExternalStatementType1Code
        
            @staticmethod
            def StatementAmount() -> typing.Type['OBStatement2DetailStatementAmount']:
                return OBStatement2DetailStatementAmount
        
            @staticmethod
            def StatementBenefit() -> typing.Type['OBStatement2DetailStatementBenefit']:
                return OBStatement2DetailStatementBenefit
        
            @staticmethod
            def StatementDateTime() -> typing.Type['OBStatement2DetailStatementDateTime']:
                return OBStatement2DetailStatementDateTime
        
            @staticmethod
            def StatementDescription() -> typing.Type['OBStatement2DetailStatementDescription']:
                return OBStatement2DetailStatementDescription
        
            @staticmethod
            def StatementFee() -> typing.Type['OBStatement2DetailStatementFee']:
                return OBStatement2DetailStatementFee
        
            @staticmethod
            def StatementId() -> typing.Type['StatementId']:
                return StatementId
        
            @staticmethod
            def StatementInterest() -> typing.Type['OBStatement2DetailStatementInterest']:
                return OBStatement2DetailStatementInterest
        
            @staticmethod
            def StatementRate() -> typing.Type['OBStatement2DetailStatementRate']:
                return OBStatement2DetailStatementRate
        
            @staticmethod
            def StatementReference() -> typing.Type['StatementReference']:
                return StatementReference
        
            @staticmethod
            def StatementValue() -> typing.Type['OBStatement2DetailStatementValue']:
                return OBStatement2DetailStatementValue
            __annotations__ = {
                "AccountId": AccountId,
                "CreationDateTime": CreationDateTime,
                "EndDateTime": EndDateTime,
                "StartDateTime": StartDateTime,
                "Type": Type,
                "StatementAmount": StatementAmount,
                "StatementBenefit": StatementBenefit,
                "StatementDateTime": StatementDateTime,
                "StatementDescription": StatementDescription,
                "StatementFee": StatementFee,
                "StatementId": StatementId,
                "StatementInterest": StatementInterest,
                "StatementRate": StatementRate,
                "StatementReference": StatementReference,
                "StatementValue": StatementValue,
            }
    
    Type: 'OBExternalStatementType1Code'
    AccountId: 'AccountId'
    CreationDateTime: MetaOapg.properties.CreationDateTime
    StartDateTime: MetaOapg.properties.StartDateTime
    EndDateTime: MetaOapg.properties.EndDateTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreationDateTime"]) -> MetaOapg.properties.CreationDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EndDateTime"]) -> MetaOapg.properties.EndDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StartDateTime"]) -> MetaOapg.properties.StartDateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'OBExternalStatementType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementAmount"]) -> 'OBStatement2DetailStatementAmount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementBenefit"]) -> 'OBStatement2DetailStatementBenefit': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementDateTime"]) -> 'OBStatement2DetailStatementDateTime': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementDescription"]) -> 'OBStatement2DetailStatementDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementFee"]) -> 'OBStatement2DetailStatementFee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementId"]) -> 'StatementId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementInterest"]) -> 'OBStatement2DetailStatementInterest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementRate"]) -> 'OBStatement2DetailStatementRate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementReference"]) -> 'StatementReference': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatementValue"]) -> 'OBStatement2DetailStatementValue': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "CreationDateTime", "EndDateTime", "StartDateTime", "Type", "StatementAmount", "StatementBenefit", "StatementDateTime", "StatementDescription", "StatementFee", "StatementId", "StatementInterest", "StatementRate", "StatementReference", "StatementValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreationDateTime"]) -> MetaOapg.properties.CreationDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EndDateTime"]) -> MetaOapg.properties.EndDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StartDateTime"]) -> MetaOapg.properties.StartDateTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> 'OBExternalStatementType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementAmount"]) -> typing.Union['OBStatement2DetailStatementAmount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementBenefit"]) -> typing.Union['OBStatement2DetailStatementBenefit', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementDateTime"]) -> typing.Union['OBStatement2DetailStatementDateTime', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementDescription"]) -> typing.Union['OBStatement2DetailStatementDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementFee"]) -> typing.Union['OBStatement2DetailStatementFee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementId"]) -> typing.Union['StatementId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementInterest"]) -> typing.Union['OBStatement2DetailStatementInterest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementRate"]) -> typing.Union['OBStatement2DetailStatementRate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementReference"]) -> typing.Union['StatementReference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatementValue"]) -> typing.Union['OBStatement2DetailStatementValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "CreationDateTime", "EndDateTime", "StartDateTime", "Type", "StatementAmount", "StatementBenefit", "StatementDateTime", "StatementDescription", "StatementFee", "StatementId", "StatementInterest", "StatementRate", "StatementReference", "StatementValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Type: 'OBExternalStatementType1Code',
        AccountId: 'AccountId',
        CreationDateTime: typing.Union[MetaOapg.properties.CreationDateTime, str, datetime, ],
        StartDateTime: typing.Union[MetaOapg.properties.StartDateTime, str, datetime, ],
        EndDateTime: typing.Union[MetaOapg.properties.EndDateTime, str, datetime, ],
        StatementAmount: typing.Union['OBStatement2DetailStatementAmount', schemas.Unset] = schemas.unset,
        StatementBenefit: typing.Union['OBStatement2DetailStatementBenefit', schemas.Unset] = schemas.unset,
        StatementDateTime: typing.Union['OBStatement2DetailStatementDateTime', schemas.Unset] = schemas.unset,
        StatementDescription: typing.Union['OBStatement2DetailStatementDescription', schemas.Unset] = schemas.unset,
        StatementFee: typing.Union['OBStatement2DetailStatementFee', schemas.Unset] = schemas.unset,
        StatementId: typing.Union['StatementId', schemas.Unset] = schemas.unset,
        StatementInterest: typing.Union['OBStatement2DetailStatementInterest', schemas.Unset] = schemas.unset,
        StatementRate: typing.Union['OBStatement2DetailStatementRate', schemas.Unset] = schemas.unset,
        StatementReference: typing.Union['StatementReference', schemas.Unset] = schemas.unset,
        StatementValue: typing.Union['OBStatement2DetailStatementValue', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBStatement2Detail':
        return super().__new__(
            cls,
            *args,
            Type=Type,
            AccountId=AccountId,
            CreationDateTime=CreationDateTime,
            StartDateTime=StartDateTime,
            EndDateTime=EndDateTime,
            StatementAmount=StatementAmount,
            StatementBenefit=StatementBenefit,
            StatementDateTime=StatementDateTime,
            StatementDescription=StatementDescription,
            StatementFee=StatementFee,
            StatementId=StatementId,
            StatementInterest=StatementInterest,
            StatementRate=StatementRate,
            StatementReference=StatementReference,
            StatementValue=StatementValue,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.model.ob_external_statement_type1_code import OBExternalStatementType1Code
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_amount import OBStatement2DetailStatementAmount
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_benefit import OBStatement2DetailStatementBenefit
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_date_time import OBStatement2DetailStatementDateTime
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_description import OBStatement2DetailStatementDescription
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_fee import OBStatement2DetailStatementFee
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_interest import OBStatement2DetailStatementInterest
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_rate import OBStatement2DetailStatementRate
from open_banking_account_and_transaction_python_sdk.model.ob_statement2_detail_statement_value import OBStatement2DetailStatementValue
from open_banking_account_and_transaction_python_sdk.model.statement_id import StatementId
from open_banking_account_and_transaction_python_sdk.model.statement_reference import StatementReference
