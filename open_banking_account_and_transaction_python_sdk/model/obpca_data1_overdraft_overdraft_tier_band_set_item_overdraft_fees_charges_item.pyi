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


class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Overdraft fees and charges details
    """


    class MetaOapg:
        required = {
            "OverdraftFeeChargeDetail",
        }
        
        class properties:
        
            @staticmethod
            def OverdraftFeeChargeDetail() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail
        
            @staticmethod
            def OverdraftFeeChargeCap() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap
            __annotations__ = {
                "OverdraftFeeChargeDetail": OverdraftFeeChargeDetail,
                "OverdraftFeeChargeCap": OverdraftFeeChargeCap,
            }
    
    OverdraftFeeChargeDetail: 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeeChargeDetail"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OverdraftFeeChargeDetail", "OverdraftFeeChargeCap", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeeChargeDetail"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OverdraftFeeChargeDetail", "OverdraftFeeChargeCap", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        OverdraftFeeChargeDetail: 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail',
        OverdraftFeeChargeCap: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem':
        return super().__new__(
            cls,
            *args,
            OverdraftFeeChargeDetail=OverdraftFeeChargeDetail,
            OverdraftFeeChargeCap=OverdraftFeeChargeCap,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCap
from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetail
