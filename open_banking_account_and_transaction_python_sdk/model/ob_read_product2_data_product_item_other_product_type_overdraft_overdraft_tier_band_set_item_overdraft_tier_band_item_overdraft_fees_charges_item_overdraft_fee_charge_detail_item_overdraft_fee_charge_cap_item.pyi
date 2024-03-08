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


class OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about any caps (maximum charges) that apply to a particular fee/charge. Capping can either be based on an amount (in gbp), an amount (in items) or a rate.
    """


    class MetaOapg:
        required = {
            "FeeType",
            "MinMaxType",
        }
        
        class properties:
        
            @staticmethod
            def FeeType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType
        
            @staticmethod
            def MinMaxType() -> typing.Type['OBMinMaxType1Code']:
                return OBMinMaxType1Code
        
            @staticmethod
            def CappingPeriod() -> typing.Type['OBPeriod1Code']:
                return OBPeriod1Code
        
            @staticmethod
            def FeeCapAmount() -> typing.Type['OBAmount10']:
                return OBAmount10
            FeeCapOccurrence = schemas.IntSchema
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType
            __annotations__ = {
                "FeeType": FeeType,
                "MinMaxType": MinMaxType,
                "CappingPeriod": CappingPeriod,
                "FeeCapAmount": FeeCapAmount,
                "FeeCapOccurrence": FeeCapOccurrence,
                "Notes": Notes,
                "OtherFeeType": OtherFeeType,
            }
    
    FeeType: 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType'
    MinMaxType: 'OBMinMaxType1Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MinMaxType"]) -> 'OBMinMaxType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CappingPeriod"]) -> 'OBPeriod1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCapAmount"]) -> 'OBAmount10': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCapOccurrence"]) -> MetaOapg.properties.FeeCapOccurrence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FeeType", "MinMaxType", "CappingPeriod", "FeeCapAmount", "FeeCapOccurrence", "Notes", "OtherFeeType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MinMaxType"]) -> 'OBMinMaxType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CappingPeriod"]) -> typing.Union['OBPeriod1Code', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCapAmount"]) -> typing.Union['OBAmount10', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCapOccurrence"]) -> typing.Union[MetaOapg.properties.FeeCapOccurrence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FeeType", "MinMaxType", "CappingPeriod", "FeeCapAmount", "FeeCapOccurrence", "Notes", "OtherFeeType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FeeType: 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType',
        MinMaxType: 'OBMinMaxType1Code',
        CappingPeriod: typing.Union['OBPeriod1Code', schemas.Unset] = schemas.unset,
        FeeCapAmount: typing.Union['OBAmount10', schemas.Unset] = schemas.unset,
        FeeCapOccurrence: typing.Union[MetaOapg.properties.FeeCapOccurrence, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem':
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

from open_banking_account_and_transaction_python_sdk.model.ob_amount10 import OBAmount10
from open_banking_account_and_transaction_python_sdk.model.ob_min_max_type1_code import OBMinMaxType1Code
from open_banking_account_and_transaction_python_sdk.model.ob_period1_code import OBPeriod1Code
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeType
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_notes import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemNotes
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType