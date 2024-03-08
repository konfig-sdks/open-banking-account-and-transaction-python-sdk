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


class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(
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
            
            
            class FeeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ARRANGED_OVERDRAFT(cls):
                    return cls("ArrangedOverdraft")
                
                @schemas.classproperty
                def ANNUAL_REVIEW(cls):
                    return cls("AnnualReview")
                
                @schemas.classproperty
                def EMERGENCY_BORROWING(cls):
                    return cls("EmergencyBorrowing")
                
                @schemas.classproperty
                def BORROWING_ITEM(cls):
                    return cls("BorrowingItem")
                
                @schemas.classproperty
                def OVERDRAFT_RENEWAL(cls):
                    return cls("OverdraftRenewal")
                
                @schemas.classproperty
                def OVERDRAFT_SETUP(cls):
                    return cls("OverdraftSetup")
                
                @schemas.classproperty
                def SURCHARGE(cls):
                    return cls("Surcharge")
                
                @schemas.classproperty
                def TEMP_OVERDRAFT(cls):
                    return cls("TempOverdraft")
                
                @schemas.classproperty
                def UNAUTHORISED_BORROWING(cls):
                    return cls("UnauthorisedBorrowing")
                
                @schemas.classproperty
                def UNAUTHORISED_PAID_TRANS(cls):
                    return cls("UnauthorisedPaidTrans")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def UNAUTHORISED_UNPAID_TRANS(cls):
                    return cls("UnauthorisedUnpaidTrans")
            
            
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
            
            
            class IncrementalBorrowingAmount(
                schemas.StrSchema
            ):
                pass
            NegotiableIndicator = schemas.BoolSchema
        
            @staticmethod
            def Notes() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
        
            @staticmethod
            def OtherApplicationFrequency() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
        
            @staticmethod
            def OtherCalculationFrequency() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
        
            @staticmethod
            def OtherFeeRateType() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
        
            @staticmethod
            def OtherFeeType() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
            OverdraftControlIndicator = schemas.BoolSchema
        
            @staticmethod
            def OverdraftFeeChargeCap() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap']:
                return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
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
    
    ApplicationFrequency: MetaOapg.properties.ApplicationFrequency
    FeeType: MetaOapg.properties.FeeType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeType"]) -> MetaOapg.properties.FeeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationFrequency"]) -> MetaOapg.properties.CalculationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeAmount"]) -> MetaOapg.properties.FeeAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRate"]) -> MetaOapg.properties.FeeRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeRateType"]) -> MetaOapg.properties.FeeRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IncrementalBorrowingAmount"]) -> MetaOapg.properties.IncrementalBorrowingAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NegotiableIndicator"]) -> MetaOapg.properties.NegotiableIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherFeeType"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftControlIndicator"]) -> MetaOapg.properties.OverdraftControlIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ApplicationFrequency", "FeeType", "CalculationFrequency", "FeeAmount", "FeeRate", "FeeRateType", "IncrementalBorrowingAmount", "NegotiableIndicator", "Notes", "OtherApplicationFrequency", "OtherCalculationFrequency", "OtherFeeRateType", "OtherFeeType", "OverdraftControlIndicator", "OverdraftFeeChargeCap", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeType"]) -> MetaOapg.properties.FeeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationFrequency"]) -> typing.Union[MetaOapg.properties.CalculationFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeAmount"]) -> typing.Union[MetaOapg.properties.FeeAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRate"]) -> typing.Union[MetaOapg.properties.FeeRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeRateType"]) -> typing.Union[MetaOapg.properties.FeeRateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IncrementalBorrowingAmount"]) -> typing.Union[MetaOapg.properties.IncrementalBorrowingAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NegotiableIndicator"]) -> typing.Union[MetaOapg.properties.NegotiableIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeRateType"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherFeeType"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftControlIndicator"]) -> typing.Union[MetaOapg.properties.OverdraftControlIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeeChargeCap"]) -> typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ApplicationFrequency", "FeeType", "CalculationFrequency", "FeeAmount", "FeeRate", "FeeRateType", "IncrementalBorrowingAmount", "NegotiableIndicator", "Notes", "OtherApplicationFrequency", "OtherCalculationFrequency", "OtherFeeRateType", "OtherFeeType", "OverdraftControlIndicator", "OverdraftFeeChargeCap", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ApplicationFrequency: typing.Union[MetaOapg.properties.ApplicationFrequency, str, ],
        FeeType: typing.Union[MetaOapg.properties.FeeType, str, ],
        CalculationFrequency: typing.Union[MetaOapg.properties.CalculationFrequency, str, schemas.Unset] = schemas.unset,
        FeeAmount: typing.Union[MetaOapg.properties.FeeAmount, str, schemas.Unset] = schemas.unset,
        FeeRate: typing.Union[MetaOapg.properties.FeeRate, str, schemas.Unset] = schemas.unset,
        FeeRateType: typing.Union[MetaOapg.properties.FeeRateType, str, schemas.Unset] = schemas.unset,
        IncrementalBorrowingAmount: typing.Union[MetaOapg.properties.IncrementalBorrowingAmount, str, schemas.Unset] = schemas.unset,
        NegotiableIndicator: typing.Union[MetaOapg.properties.NegotiableIndicator, bool, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes', schemas.Unset] = schemas.unset,
        OtherApplicationFrequency: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency', schemas.Unset] = schemas.unset,
        OtherCalculationFrequency: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency', schemas.Unset] = schemas.unset,
        OtherFeeRateType: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType', schemas.Unset] = schemas.unset,
        OtherFeeType: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType', schemas.Unset] = schemas.unset,
        OverdraftControlIndicator: typing.Union[MetaOapg.properties.OverdraftControlIndicator, bool, schemas.Unset] = schemas.unset,
        OverdraftFeeChargeCap: typing.Union['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem':
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

from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_notes import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemNotes
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
