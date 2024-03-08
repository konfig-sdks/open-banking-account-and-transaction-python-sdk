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


class OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Tier Band Details
    """


    class MetaOapg:
        required = {
            "FixedVariableInterestRateType",
            "TierValueMinimum",
            "ApplicationFrequency",
            "AER",
        }
        
        class properties:
            
            
            class AER(
                schemas.StrSchema
            ):
                pass
            
            
            class ApplicationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FQAT(cls):
                    return cls("FQAT")
                
                @schemas.classproperty
                def FQDY(cls):
                    return cls("FQDY")
                
                @schemas.classproperty
                def FQHY(cls):
                    return cls("FQHY")
                
                @schemas.classproperty
                def FQMY(cls):
                    return cls("FQMY")
                
                @schemas.classproperty
                def FQOT(cls):
                    return cls("FQOT")
                
                @schemas.classproperty
                def FQQY(cls):
                    return cls("FQQY")
                
                @schemas.classproperty
                def FQSD(cls):
                    return cls("FQSD")
                
                @schemas.classproperty
                def FQWY(cls):
                    return cls("FQWY")
                
                @schemas.classproperty
                def FQYY(cls):
                    return cls("FQYY")
        
            @staticmethod
            def FixedVariableInterestRateType() -> typing.Type['OBInterestFixedVariableType1Code']:
                return OBInterestFixedVariableType1Code
            
            
            class TierValueMinimum(
                schemas.StrSchema
            ):
                pass
            
            
            class BankInterestRate(
                schemas.StrSchema
            ):
                pass
            
            
            class BankInterestRateType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INBB(cls):
                    return cls("INBB")
                
                @schemas.classproperty
                def INFR(cls):
                    return cls("INFR")
                
                @schemas.classproperty
                def INGR(cls):
                    return cls("INGR")
                
                @schemas.classproperty
                def INLR(cls):
                    return cls("INLR")
                
                @schemas.classproperty
                def INNE(cls):
                    return cls("INNE")
                
                @schemas.classproperty
                def INOT(cls):
                    return cls("INOT")
            
            
            class CalculationFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FQAT(cls):
                    return cls("FQAT")
                
                @schemas.classproperty
                def FQDY(cls):
                    return cls("FQDY")
                
                @schemas.classproperty
                def FQHY(cls):
                    return cls("FQHY")
                
                @schemas.classproperty
                def FQMY(cls):
                    return cls("FQMY")
                
                @schemas.classproperty
                def FQOT(cls):
                    return cls("FQOT")
                
                @schemas.classproperty
                def FQQY(cls):
                    return cls("FQQY")
                
                @schemas.classproperty
                def FQSD(cls):
                    return cls("FQSD")
                
                @schemas.classproperty
                def FQWY(cls):
                    return cls("FQWY")
                
                @schemas.classproperty
                def FQYY(cls):
                    return cls("FQYY")
            
            
            class DepositInterestAppliedCoverage(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INBA(cls):
                    return cls("INBA")
                
                @schemas.classproperty
                def INTI(cls):
                    return cls("INTI")
                
                @schemas.classproperty
                def INWH(cls):
                    return cls("INWH")
            
            
            class Identification(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemNotes
        
            @staticmethod
            def OtherApplicationFrequency() -> typing.Type['OBOtherCodeType11']:
                return OBOtherCodeType11
        
            @staticmethod
            def OtherBankInterestType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType']:
                return OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType
        
            @staticmethod
            def OtherCalculationFrequency() -> typing.Type['OBOtherCodeType12']:
                return OBOtherCodeType12
            
            
            class TierValueMaximum(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "AER": AER,
                "ApplicationFrequency": ApplicationFrequency,
                "FixedVariableInterestRateType": FixedVariableInterestRateType,
                "TierValueMinimum": TierValueMinimum,
                "BankInterestRate": BankInterestRate,
                "BankInterestRateType": BankInterestRateType,
                "CalculationFrequency": CalculationFrequency,
                "DepositInterestAppliedCoverage": DepositInterestAppliedCoverage,
                "Identification": Identification,
                "Notes": Notes,
                "OtherApplicationFrequency": OtherApplicationFrequency,
                "OtherBankInterestType": OtherBankInterestType,
                "OtherCalculationFrequency": OtherCalculationFrequency,
                "TierValueMaximum": TierValueMaximum,
            }
    
    FixedVariableInterestRateType: 'OBInterestFixedVariableType1Code'
    TierValueMinimum: MetaOapg.properties.TierValueMinimum
    ApplicationFrequency: MetaOapg.properties.ApplicationFrequency
    AER: MetaOapg.properties.AER
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AER"]) -> MetaOapg.properties.AER: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FixedVariableInterestRateType"]) -> 'OBInterestFixedVariableType1Code': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMinimum"]) -> MetaOapg.properties.TierValueMinimum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankInterestRate"]) -> MetaOapg.properties.BankInterestRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankInterestRateType"]) -> MetaOapg.properties.BankInterestRateType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CalculationFrequency"]) -> MetaOapg.properties.CalculationFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DepositInterestAppliedCoverage"]) -> MetaOapg.properties.DepositInterestAppliedCoverage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> MetaOapg.properties.Identification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> 'OBOtherCodeType11': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherBankInterestType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> 'OBOtherCodeType12': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMaximum"]) -> MetaOapg.properties.TierValueMaximum: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AER", "ApplicationFrequency", "FixedVariableInterestRateType", "TierValueMinimum", "BankInterestRate", "BankInterestRateType", "CalculationFrequency", "DepositInterestAppliedCoverage", "Identification", "Notes", "OtherApplicationFrequency", "OtherBankInterestType", "OtherCalculationFrequency", "TierValueMaximum", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AER"]) -> MetaOapg.properties.AER: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApplicationFrequency"]) -> MetaOapg.properties.ApplicationFrequency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FixedVariableInterestRateType"]) -> 'OBInterestFixedVariableType1Code': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMinimum"]) -> MetaOapg.properties.TierValueMinimum: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankInterestRate"]) -> typing.Union[MetaOapg.properties.BankInterestRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankInterestRateType"]) -> typing.Union[MetaOapg.properties.BankInterestRateType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CalculationFrequency"]) -> typing.Union[MetaOapg.properties.CalculationFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DepositInterestAppliedCoverage"]) -> typing.Union[MetaOapg.properties.DepositInterestAppliedCoverage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> typing.Union[MetaOapg.properties.Identification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherApplicationFrequency"]) -> typing.Union['OBOtherCodeType11', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherBankInterestType"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherCalculationFrequency"]) -> typing.Union['OBOtherCodeType12', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMaximum"]) -> typing.Union[MetaOapg.properties.TierValueMaximum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AER", "ApplicationFrequency", "FixedVariableInterestRateType", "TierValueMinimum", "BankInterestRate", "BankInterestRateType", "CalculationFrequency", "DepositInterestAppliedCoverage", "Identification", "Notes", "OtherApplicationFrequency", "OtherBankInterestType", "OtherCalculationFrequency", "TierValueMaximum", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        FixedVariableInterestRateType: 'OBInterestFixedVariableType1Code',
        TierValueMinimum: typing.Union[MetaOapg.properties.TierValueMinimum, str, ],
        ApplicationFrequency: typing.Union[MetaOapg.properties.ApplicationFrequency, str, ],
        AER: typing.Union[MetaOapg.properties.AER, str, ],
        BankInterestRate: typing.Union[MetaOapg.properties.BankInterestRate, str, schemas.Unset] = schemas.unset,
        BankInterestRateType: typing.Union[MetaOapg.properties.BankInterestRateType, str, schemas.Unset] = schemas.unset,
        CalculationFrequency: typing.Union[MetaOapg.properties.CalculationFrequency, str, schemas.Unset] = schemas.unset,
        DepositInterestAppliedCoverage: typing.Union[MetaOapg.properties.DepositInterestAppliedCoverage, str, schemas.Unset] = schemas.unset,
        Identification: typing.Union[MetaOapg.properties.Identification, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemNotes', schemas.Unset] = schemas.unset,
        OtherApplicationFrequency: typing.Union['OBOtherCodeType11', schemas.Unset] = schemas.unset,
        OtherBankInterestType: typing.Union['OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType', schemas.Unset] = schemas.unset,
        OtherCalculationFrequency: typing.Union['OBOtherCodeType12', schemas.Unset] = schemas.unset,
        TierValueMaximum: typing.Union[MetaOapg.properties.TierValueMaximum, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem':
        return super().__new__(
            cls,
            *args,
            FixedVariableInterestRateType=FixedVariableInterestRateType,
            TierValueMinimum=TierValueMinimum,
            ApplicationFrequency=ApplicationFrequency,
            AER=AER,
            BankInterestRate=BankInterestRate,
            BankInterestRateType=BankInterestRateType,
            CalculationFrequency=CalculationFrequency,
            DepositInterestAppliedCoverage=DepositInterestAppliedCoverage,
            Identification=Identification,
            Notes=Notes,
            OtherApplicationFrequency=OtherApplicationFrequency,
            OtherBankInterestType=OtherBankInterestType,
            OtherCalculationFrequency=OtherCalculationFrequency,
            TierValueMaximum=TierValueMaximum,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_interest_fixed_variable_type1_code import OBInterestFixedVariableType1Code
from open_banking_account_and_transaction_python_sdk.model.ob_other_code_type11 import OBOtherCodeType11
from open_banking_account_and_transaction_python_sdk.model.ob_other_code_type12 import OBOtherCodeType12
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_notes import OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import OBReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType
