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


class OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about the fees/charges
    """


    class MetaOapg:
        required = {
            "ApplicationFrequency",
            "FeeType",
        }
        
        class properties:
        
            @staticmethod
            def ApplicationFrequency() -> typing.Type['OBFeeFrequency1Code0']:
                return OBFeeFrequency1Code0
        
            @staticmethod
            def FeeType() -> typing.Type['OBOverdraftFeeType1Code']:
                return OBOverdraftFeeType1Code
        
            @staticmethod
            def CalculationFrequency() -> typing.Type['OBFeeFrequency1Code1']:
                return OBFeeFrequency1Code1
        
            @staticmethod
            def FeeAmount() -> typing.Type['OBAmount12']:
                return OBAmount12
        
            @staticmethod
            def FeeRate() -> typing.Type['OBRate10']:
                return OBRate10
        
            @staticmethod
            def FeeRateType() -> typing.Type['OBInterestRateType1Code0']:
                return OBInterestRateType1Code0
        
            @staticmethod
            def IncrementalBorrowingAmount() -> typing.Type['OBAmount11']:
                return OBAmount11
            NegotiableIndicator = schemas.BoolSchema
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
        
            @staticmethod
            def OtherApplicationFrequency() -> typing.Type['OBOtherCodeType11']:
                return OBOtherCodeType11
        
            @staticmethod
            def OtherCalculationFrequency() -> typing.Type['OBOtherCodeType12']:
                return OBOtherCodeType12
        
            @staticmethod
            def OtherFeeRateType() -> typing.Type['OBOtherCodeType14']:
                return OBOtherCodeType14
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBOtherCodeType13']:
                return OBOtherCodeType13
            OverdraftControlIndicator = schemas.BoolSchema
        
            @staticmethod
            def OverdraftFeeChargeCap() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap']:
                return OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
            __annotations__ = {
                "ApplicationFrequency": ApplicationFrequency,
                "FeeType": FeeType,
                "CalculationFrequency": CalculationFrequency,
                "FeeAmount": FeeAmount,
                "FeeRate": FeeRate,
                "FeeRateType": FeeRateType,
                "IncrementalBorrowingAmount": IncrementalBorrowingAmount,
                "NegotiableIndicator": NegotiableIndicator,
                "Notes": Notes,
                "OtherApplicationFrequency": OtherApplicationFrequency,
                "OtherCalculationFrequency": OtherCalculationFrequency,
                "OtherFeeRateType": OtherFeeRateType,
                "OtherFeeType": OtherFeeType,
                "OverdraftControlIndicator": OverdraftControlIndicator,
                "OverdraftFeeChargeCap": OverdraftFeeChargeCap,
            }
    
    ApplicationFrequency: 'OBFeeFrequency1Code0'
    FeeType: 'OBOverdraftFeeType1Code'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> 'OBFeeFrequency1Code0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> 'OBOverdraftFeeType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationFrequency"]) -> 'OBFeeFrequency1Code1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeAmount"]) -> 'OBAmount12': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRate"]) -> 'OBRate10': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRateType"]) -> 'OBInterestRateType1Code0': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IncrementalBorrowingAmount"]) -> 'OBAmount11': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NegotiableIndicator"]) -> MetaOapg.properties.NegotiableIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> 'OBOtherCodeType11': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> 'OBOtherCodeType12': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> 'OBOtherCodeType14': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBOtherCodeType13': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftControlIndicator"]) -> MetaOapg.properties.OverdraftControlIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ApplicationFrequency", "FeeType", "CalculationFrequency", "FeeAmount", "FeeRate", "FeeRateType", "IncrementalBorrowingAmount", "NegotiableIndicator", "Notes", "OtherApplicationFrequency", "OtherCalculationFrequency", "OtherFeeRateType", "OtherFeeType", "OverdraftControlIndicator", "OverdraftFeeChargeCap", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> 'OBFeeFrequency1Code0': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> 'OBOverdraftFeeType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationFrequency"]) -> typing.Union['OBFeeFrequency1Code1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeAmount"]) -> typing.Union['OBAmount12', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRate"]) -> typing.Union['OBRate10', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRateType"]) -> typing.Union['OBInterestRateType1Code0', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IncrementalBorrowingAmount"]) -> typing.Union['OBAmount11', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NegotiableIndicator"]) -> typing.Union[MetaOapg.properties.NegotiableIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> typing.Union['OBOtherCodeType11', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> typing.Union['OBOtherCodeType12', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> typing.Union['OBOtherCodeType14', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBOtherCodeType13', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftControlIndicator"]) -> typing.Union[MetaOapg.properties.OverdraftControlIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ApplicationFrequency", "FeeType", "CalculationFrequency", "FeeAmount", "FeeRate", "FeeRateType", "IncrementalBorrowingAmount", "NegotiableIndicator", "Notes", "OtherApplicationFrequency", "OtherCalculationFrequency", "OtherFeeRateType", "OtherFeeType", "OverdraftControlIndicator", "OverdraftFeeChargeCap", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ApplicationFrequency: 'OBFeeFrequency1Code0',
        FeeType: 'OBOverdraftFeeType1Code',
        CalculationFrequency: typing.Union['OBFeeFrequency1Code1', schemas.Unset] = schemas.unset,
        FeeAmount: typing.Union['OBAmount12', schemas.Unset] = schemas.unset,
        FeeRate: typing.Union['OBRate10', schemas.Unset] = schemas.unset,
        FeeRateType: typing.Union['OBInterestRateType1Code0', schemas.Unset] = schemas.unset,
        IncrementalBorrowingAmount: typing.Union['OBAmount11', schemas.Unset] = schemas.unset,
        NegotiableIndicator: typing.Union[MetaOapg.properties.NegotiableIndicator, bool, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes', schemas.Unset] = schemas.unset,
        OtherApplicationFrequency: typing.Union['OBOtherCodeType11', schemas.Unset] = schemas.unset,
        OtherCalculationFrequency: typing.Union['OBOtherCodeType12', schemas.Unset] = schemas.unset,
        OtherFeeRateType: typing.Union['OBOtherCodeType14', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBOtherCodeType13', schemas.Unset] = schemas.unset,
        OverdraftControlIndicator: typing.Union[MetaOapg.properties.OverdraftControlIndicator, bool, schemas.Unset] = schemas.unset,
        OverdraftFeeChargeCap: typing.Union['OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem':
        return super().__new__(
            cls,
            *args,
            ApplicationFrequency=ApplicationFrequency,
            FeeType=FeeType,
            CalculationFrequency=CalculationFrequency,
            FeeAmount=FeeAmount,
            FeeRate=FeeRate,
            FeeRateType=FeeRateType,
            IncrementalBorrowingAmount=IncrementalBorrowingAmount,
            NegotiableIndicator=NegotiableIndicator,
            Notes=Notes,
            OtherApplicationFrequency=OtherApplicationFrequency,
            OtherCalculationFrequency=OtherCalculationFrequency,
            OtherFeeRateType=OtherFeeRateType,
            OtherFeeType=OtherFeeType,
            OverdraftControlIndicator=OverdraftControlIndicator,
            OverdraftFeeChargeCap=OverdraftFeeChargeCap,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_amount11 import OBAmount11
from open_banking_account_and_transaction_python_sdk.model.ob_amount12 import OBAmount12
from open_banking_account_and_transaction_python_sdk.model.ob_fee_frequency1_code0 import OBFeeFrequency1Code0
from open_banking_account_and_transaction_python_sdk.model.ob_fee_frequency1_code1 import OBFeeFrequency1Code1
from open_banking_account_and_transaction_python_sdk.model.ob_interest_rate_type1_code0 import OBInterestRateType1Code0
from open_banking_account_and_transaction_python_sdk.model.ob_other_code_type11 import OBOtherCodeType11
from open_banking_account_and_transaction_python_sdk.model.ob_other_code_type12 import OBOtherCodeType12
from open_banking_account_and_transaction_python_sdk.model.ob_other_code_type13 import OBOtherCodeType13
from open_banking_account_and_transaction_python_sdk.model.ob_other_code_type14 import OBOtherCodeType14
from open_banking_account_and_transaction_python_sdk.model.ob_overdraft_fee_type1_code import OBOverdraftFeeType1Code
from open_banking_account_and_transaction_python_sdk.model.ob_rate10 import OBRate10
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_notes import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import OBReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
