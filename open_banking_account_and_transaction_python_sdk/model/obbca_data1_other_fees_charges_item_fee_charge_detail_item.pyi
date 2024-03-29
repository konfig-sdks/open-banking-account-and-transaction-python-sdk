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


class OBBCAData1OtherFeesChargesItemFeeChargeDetailItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Other fees/charges details
    """


    class MetaOapg:
        required = {
            "ApplicationFrequency",
            "FeeType",
            "FeeCategory",
        }
        
        class properties:
            
            
            class ApplicationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ON_CLOSING(cls):
                    return cls("OnClosing")
                
                @schemas.classproperty
                def ON_OPENING(cls):
                    return cls("OnOpening")
                
                @schemas.classproperty
                def CHARGING_PERIOD(cls):
                    return cls("ChargingPeriod")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("Daily")
                
                @schemas.classproperty
                def PER_ITEM(cls):
                    return cls("PerItem")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("Monthly")
                
                @schemas.classproperty
                def ON_ANNIVERSARY(cls):
                    return cls("OnAnniversary")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def PER_HUNDRED_POUNDS(cls):
                    return cls("PerHundredPounds")
                
                @schemas.classproperty
                def PER_HOUR(cls):
                    return cls("PerHour")
                
                @schemas.classproperty
                def PER_OCCURRENCE(cls):
                    return cls("PerOccurrence")
                
                @schemas.classproperty
                def PER_SHEET(cls):
                    return cls("PerSheet")
                
                @schemas.classproperty
                def PER_TRANSACTION(cls):
                    return cls("PerTransaction")
                
                @schemas.classproperty
                def PER_TRANSACTION_AMOUNT(cls):
                    return cls("PerTransactionAmount")
                
                @schemas.classproperty
                def PER_TRANSACTION_PERCENTAGE(cls):
                    return cls("PerTransactionPercentage")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("Quarterly")
                
                @schemas.classproperty
                def SIX_MONTHLY(cls):
                    return cls("SixMonthly")
                
                @schemas.classproperty
                def STATEMENT_MONTHLY(cls):
                    return cls("StatementMonthly")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("Weekly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("Yearly")
            
            
            class FeeCategory(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def SERVICING(cls):
                    return cls("Servicing")
            
            
            class FeeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def SERVICE_CACCOUNT_FEE(cls):
                    return cls("ServiceCAccountFee")
                
                @schemas.classproperty
                def SERVICE_CACCOUNT_FEE_MONTHLY(cls):
                    return cls("ServiceCAccountFeeMonthly")
                
                @schemas.classproperty
                def SERVICE_CACCOUNT_FEE_QUARTERLY(cls):
                    return cls("ServiceCAccountFeeQuarterly")
                
                @schemas.classproperty
                def SERVICE_CFIXED_TARIFF(cls):
                    return cls("ServiceCFixedTariff")
                
                @schemas.classproperty
                def SERVICE_CBUSI_DEP_ACC_BREAKAGE(cls):
                    return cls("ServiceCBusiDepAccBreakage")
                
                @schemas.classproperty
                def SERVICE_CMINIMUM_MONTHLY_FEE(cls):
                    return cls("ServiceCMinimumMonthlyFee")
                
                @schemas.classproperty
                def SERVICE_COTHER(cls):
                    return cls("ServiceCOther")
            
            
            class CalculationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ON_CLOSING(cls):
                    return cls("OnClosing")
                
                @schemas.classproperty
                def ON_OPENING(cls):
                    return cls("OnOpening")
                
                @schemas.classproperty
                def CHARGING_PERIOD(cls):
                    return cls("ChargingPeriod")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("Daily")
                
                @schemas.classproperty
                def PER_ITEM(cls):
                    return cls("PerItem")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("Monthly")
                
                @schemas.classproperty
                def ON_ANNIVERSARY(cls):
                    return cls("OnAnniversary")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def PER_HUNDRED_POUNDS(cls):
                    return cls("PerHundredPounds")
                
                @schemas.classproperty
                def PER_HOUR(cls):
                    return cls("PerHour")
                
                @schemas.classproperty
                def PER_OCCURRENCE(cls):
                    return cls("PerOccurrence")
                
                @schemas.classproperty
                def PER_SHEET(cls):
                    return cls("PerSheet")
                
                @schemas.classproperty
                def PER_TRANSACTION(cls):
                    return cls("PerTransaction")
                
                @schemas.classproperty
                def PER_TRANSACTION_AMOUNT(cls):
                    return cls("PerTransactionAmount")
                
                @schemas.classproperty
                def PER_TRANSACTION_PERCENTAGE(cls):
                    return cls("PerTransactionPercentage")
                
                @schemas.classproperty
                def QUARTERLY(cls):
                    return cls("Quarterly")
                
                @schemas.classproperty
                def SIX_MONTHLY(cls):
                    return cls("SixMonthly")
                
                @schemas.classproperty
                def STATEMENT_MONTHLY(cls):
                    return cls("StatementMonthly")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("Weekly")
                
                @schemas.classproperty
                def YEARLY(cls):
                    return cls("Yearly")
            
            
            class FeeAmount(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def FeeApplicableRange() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange
        
            @staticmethod
            def FeeChargeCap() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap
            
            
            class FeeRate(
                schemas.StrSchema
            ):
                pass
            
            
            class FeeRateType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def GROSS(cls):
                    return cls("Gross")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
            NegotiableIndicator = schemas.BoolSchema
        
            @staticmethod
            def Notes() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes
        
            @staticmethod
            def OtherApplicationFrequency() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency
        
            @staticmethod
            def OtherCalculationFrequency() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency
        
            @staticmethod
            def OtherFeeCategoryType() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType
        
            @staticmethod
            def OtherFeeRateType() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType']:
                return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType
            __annotations__ = {
                "ApplicationFrequency": ApplicationFrequency,
                "FeeCategory": FeeCategory,
                "FeeType": FeeType,
                "CalculationFrequency": CalculationFrequency,
                "FeeAmount": FeeAmount,
                "FeeApplicableRange": FeeApplicableRange,
                "FeeChargeCap": FeeChargeCap,
                "FeeRate": FeeRate,
                "FeeRateType": FeeRateType,
                "NegotiableIndicator": NegotiableIndicator,
                "Notes": Notes,
                "OtherApplicationFrequency": OtherApplicationFrequency,
                "OtherCalculationFrequency": OtherCalculationFrequency,
                "OtherFeeCategoryType": OtherFeeCategoryType,
                "OtherFeeRateType": OtherFeeRateType,
                "OtherFeeType": OtherFeeType,
            }
    
    ApplicationFrequency: MetaOapg.properties.ApplicationFrequency
    FeeType: MetaOapg.properties.FeeType
    FeeCategory: MetaOapg.properties.FeeCategory
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCategory"]) -> MetaOapg.properties.FeeCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> MetaOapg.properties.FeeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationFrequency"]) -> MetaOapg.properties.CalculationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeAmount"]) -> MetaOapg.properties.FeeAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeApplicableRange"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeChargeCap"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRate"]) -> MetaOapg.properties.FeeRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRateType"]) -> MetaOapg.properties.FeeRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NegotiableIndicator"]) -> MetaOapg.properties.NegotiableIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeCategoryType"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ApplicationFrequency", "FeeCategory", "FeeType", "CalculationFrequency", "FeeAmount", "FeeApplicableRange", "FeeChargeCap", "FeeRate", "FeeRateType", "NegotiableIndicator", "Notes", "OtherApplicationFrequency", "OtherCalculationFrequency", "OtherFeeCategoryType", "OtherFeeRateType", "OtherFeeType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCategory"]) -> MetaOapg.properties.FeeCategory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> MetaOapg.properties.FeeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationFrequency"]) -> typing.Union[MetaOapg.properties.CalculationFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeAmount"]) -> typing.Union[MetaOapg.properties.FeeAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeApplicableRange"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeChargeCap"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRate"]) -> typing.Union[MetaOapg.properties.FeeRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRateType"]) -> typing.Union[MetaOapg.properties.FeeRateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NegotiableIndicator"]) -> typing.Union[MetaOapg.properties.NegotiableIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeCategoryType"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ApplicationFrequency", "FeeCategory", "FeeType", "CalculationFrequency", "FeeAmount", "FeeApplicableRange", "FeeChargeCap", "FeeRate", "FeeRateType", "NegotiableIndicator", "Notes", "OtherApplicationFrequency", "OtherCalculationFrequency", "OtherFeeCategoryType", "OtherFeeRateType", "OtherFeeType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ApplicationFrequency: typing.Union[MetaOapg.properties.ApplicationFrequency, str, ],
        FeeType: typing.Union[MetaOapg.properties.FeeType, str, ],
        FeeCategory: typing.Union[MetaOapg.properties.FeeCategory, str, ],
        CalculationFrequency: typing.Union[MetaOapg.properties.CalculationFrequency, str, schemas.Unset] = schemas.unset,
        FeeAmount: typing.Union[MetaOapg.properties.FeeAmount, str, schemas.Unset] = schemas.unset,
        FeeApplicableRange: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange', schemas.Unset] = schemas.unset,
        FeeChargeCap: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap', schemas.Unset] = schemas.unset,
        FeeRate: typing.Union[MetaOapg.properties.FeeRate, str, schemas.Unset] = schemas.unset,
        FeeRateType: typing.Union[MetaOapg.properties.FeeRateType, str, schemas.Unset] = schemas.unset,
        NegotiableIndicator: typing.Union[MetaOapg.properties.NegotiableIndicator, bool, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes', schemas.Unset] = schemas.unset,
        OtherApplicationFrequency: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency', schemas.Unset] = schemas.unset,
        OtherCalculationFrequency: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency', schemas.Unset] = schemas.unset,
        OtherFeeCategoryType: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType', schemas.Unset] = schemas.unset,
        OtherFeeRateType: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItem':
        return super().__new__(
            cls,
            *args,
            ApplicationFrequency=ApplicationFrequency,
            FeeType=FeeType,
            FeeCategory=FeeCategory,
            CalculationFrequency=CalculationFrequency,
            FeeAmount=FeeAmount,
            FeeApplicableRange=FeeApplicableRange,
            FeeChargeCap=FeeChargeCap,
            FeeRate=FeeRate,
            FeeRateType=FeeRateType,
            NegotiableIndicator=NegotiableIndicator,
            Notes=Notes,
            OtherApplicationFrequency=OtherApplicationFrequency,
            OtherCalculationFrequency=OtherCalculationFrequency,
            OtherFeeCategoryType=OtherFeeCategoryType,
            OtherFeeRateType=OtherFeeRateType,
            OtherFeeType=OtherFeeType,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_notes import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemNotes
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_application_frequency import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_category_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_other_fee_type import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType
