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


class OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Applicable fee/charges for repayment such as prepayment, full early repayment or non repayment.
    """


    class MetaOapg:
        required = {
            "RepaymentFeeChargeDetail",
        }
        
        class properties:
        
            @staticmethod
            def RepaymentFeeChargeDetail() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail
        
            @staticmethod
            def RepaymentFeeChargeCap() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap
            __annotations__ = {
                "RepaymentFeeChargeDetail": RepaymentFeeChargeDetail,
                "RepaymentFeeChargeCap": RepaymentFeeChargeCap,
            }
    
    RepaymentFeeChargeDetail: 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepaymentFeeChargeDetail"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepaymentFeeChargeCap"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["RepaymentFeeChargeDetail", "RepaymentFeeChargeCap", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepaymentFeeChargeDetail"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepaymentFeeChargeCap"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["RepaymentFeeChargeDetail", "RepaymentFeeChargeCap", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        RepaymentFeeChargeDetail: 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail',
        RepaymentFeeChargeCap: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges':
        return super().__new__(
            cls,
            *args,
            RepaymentFeeChargeDetail=RepaymentFeeChargeDetail,
            RepaymentFeeChargeCap=RepaymentFeeChargeCap,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_detail import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail
