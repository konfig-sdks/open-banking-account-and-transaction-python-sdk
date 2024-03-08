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


class OBPCAData1OtherFeesChargesFeeChargeCapItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about any caps (maximum charges) that apply to a particular fee/charge
    """


    class MetaOapg:
        required = {
            "FeeType",
            "MinMaxType",
        }
        
        class properties:
        
            @staticmethod
            def FeeType() -> typing.Type['OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType']:
                return OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType
            
            
            class MinMaxType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MINIMUM(cls):
                    return cls("Minimum")
                
                @schemas.classproperty
                def MAXIMUM(cls):
                    return cls("Maximum")
            
            
            class CappingPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACADEMIC_TERM(cls):
                    return cls("AcademicTerm")
                
                @schemas.classproperty
                def DAY(cls):
                    return cls("Day")
                
                @schemas.classproperty
                def HALF_YEAR(cls):
                    return cls("Half Year")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("Month")
                
                @schemas.classproperty
                def QUARTER(cls):
                    return cls("Quarter")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("Week")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("Year")
            
            
            class FeeCapAmount(
                schemas.StrSchema
            ):
                pass
            FeeCapOccurrence = schemas.Float32Schema
        
            @staticmethod
            def Notes() -> typing.Type['OBPCAData1OtherFeesChargesFeeChargeCapItemNotes']:
                return OBPCAData1OtherFeesChargesFeeChargeCapItemNotes
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType']:
                return OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType
            __annotations__ = {
                "FeeType": FeeType,
                "MinMaxType": MinMaxType,
                "CappingPeriod": CappingPeriod,
                "FeeCapAmount": FeeCapAmount,
                "FeeCapOccurrence": FeeCapOccurrence,
                "Notes": Notes,
                "OtherFeeType": OtherFeeType,
            }
    
    FeeType: 'OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType'
    MinMaxType: MetaOapg.properties.MinMaxType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> 'OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MinMaxType"]) -> MetaOapg.properties.MinMaxType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CappingPeriod"]) -> MetaOapg.properties.CappingPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCapAmount"]) -> MetaOapg.properties.FeeCapAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCapOccurrence"]) -> MetaOapg.properties.FeeCapOccurrence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBPCAData1OtherFeesChargesFeeChargeCapItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FeeType", "MinMaxType", "CappingPeriod", "FeeCapAmount", "FeeCapOccurrence", "Notes", "OtherFeeType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> 'OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MinMaxType"]) -> MetaOapg.properties.MinMaxType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CappingPeriod"]) -> typing.Union[MetaOapg.properties.CappingPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCapAmount"]) -> typing.Union[MetaOapg.properties.FeeCapAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCapOccurrence"]) -> typing.Union[MetaOapg.properties.FeeCapOccurrence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBPCAData1OtherFeesChargesFeeChargeCapItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FeeType", "MinMaxType", "CappingPeriod", "FeeCapAmount", "FeeCapOccurrence", "Notes", "OtherFeeType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FeeType: 'OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType',
        MinMaxType: typing.Union[MetaOapg.properties.MinMaxType, str, ],
        CappingPeriod: typing.Union[MetaOapg.properties.CappingPeriod, str, schemas.Unset] = schemas.unset,
        FeeCapAmount: typing.Union[MetaOapg.properties.FeeCapAmount, str, schemas.Unset] = schemas.unset,
        FeeCapOccurrence: typing.Union[MetaOapg.properties.FeeCapOccurrence, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBPCAData1OtherFeesChargesFeeChargeCapItemNotes', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1OtherFeesChargesFeeChargeCapItem':
        return super().__new__(
            cls,
            *args,
            FeeType=FeeType,
            MinMaxType=MinMaxType,
            CappingPeriod=CappingPeriod,
            FeeCapAmount=FeeCapAmount,
            FeeCapOccurrence=FeeCapOccurrence,
            Notes=Notes,
            OtherFeeType=OtherFeeType,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.obpca_data1_other_fees_charges_fee_charge_cap_item_fee_type import OBPCAData1OtherFeesChargesFeeChargeCapItemFeeType
from open_banking_account_and_transaction_python_sdk.model.obpca_data1_other_fees_charges_fee_charge_cap_item_notes import OBPCAData1OtherFeesChargesFeeChargeCapItemNotes
from open_banking_account_and_transaction_python_sdk.model.obpca_data1_other_fees_charges_fee_charge_cap_item_other_fee_type import OBPCAData1OtherFeesChargesFeeChargeCapItemOtherFeeType