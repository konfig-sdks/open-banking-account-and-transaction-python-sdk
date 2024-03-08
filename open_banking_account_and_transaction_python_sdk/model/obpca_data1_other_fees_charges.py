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


class OBPCAData1OtherFeesCharges(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Contains details of fees and charges which are not associated with either borrowing or features/benefits
    """


    class MetaOapg:
        required = {
            "FeeChargeDetail",
        }
        
        class properties:
        
            @staticmethod
            def FeeChargeDetail() -> typing.Type['OBPCAData1OtherFeesChargesFeeChargeDetail']:
                return OBPCAData1OtherFeesChargesFeeChargeDetail
        
            @staticmethod
            def FeeChargeCap() -> typing.Type['OBPCAData1OtherFeesChargesFeeChargeCap']:
                return OBPCAData1OtherFeesChargesFeeChargeCap
            __annotations__ = {
                "FeeChargeDetail": FeeChargeDetail,
                "FeeChargeCap": FeeChargeCap,
            }
    
    FeeChargeDetail: 'OBPCAData1OtherFeesChargesFeeChargeDetail'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeChargeDetail"]) -> 'OBPCAData1OtherFeesChargesFeeChargeDetail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeChargeCap"]) -> 'OBPCAData1OtherFeesChargesFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["FeeChargeDetail", "FeeChargeCap", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeChargeDetail"]) -> 'OBPCAData1OtherFeesChargesFeeChargeDetail': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeChargeCap"]) -> typing.Union['OBPCAData1OtherFeesChargesFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["FeeChargeDetail", "FeeChargeCap", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FeeChargeDetail: 'OBPCAData1OtherFeesChargesFeeChargeDetail',
        FeeChargeCap: typing.Union['OBPCAData1OtherFeesChargesFeeChargeCap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1OtherFeesCharges':
        return super().__new__(
            cls,
            *args,
            FeeChargeDetail=FeeChargeDetail,
            FeeChargeCap=FeeChargeCap,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.obpca_data1_other_fees_charges_fee_charge_cap import OBPCAData1OtherFeesChargesFeeChargeCap
from open_banking_account_and_transaction_python_sdk.model.obpca_data1_other_fees_charges_fee_charge_detail import OBPCAData1OtherFeesChargesFeeChargeDetail