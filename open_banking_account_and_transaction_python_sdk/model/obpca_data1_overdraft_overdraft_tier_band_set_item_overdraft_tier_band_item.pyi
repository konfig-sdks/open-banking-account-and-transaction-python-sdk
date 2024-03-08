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


class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Provides overdraft details for a specific tier or band
    """


    class MetaOapg:
        required = {
            "TierValueMin",
        }
        
        class properties:
            
            
            class TierValueMin(
                schemas.StrSchema
            ):
                pass
            BankGuaranteedIndicator = schemas.BoolSchema
            
            
            class EAR(
                schemas.StrSchema
            ):
                pass
            
            
            class Identification(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def Notes() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
        
            @staticmethod
            def OverdraftFeesCharges() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges']:
                return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges
            
            
            class OverdraftInterestChargingCoverage(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TIERED(cls):
                    return cls("Tiered")
                
                @schemas.classproperty
                def WHOLE(cls):
                    return cls("Whole")
            
            
            class RepresentativeAPR(
                schemas.StrSchema
            ):
                pass
            
            
            class TierValueMax(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "TierValueMin": TierValueMin,
                "BankGuaranteedIndicator": BankGuaranteedIndicator,
                "EAR": EAR,
                "Identification": Identification,
                "Notes": Notes,
                "OverdraftFeesCharges": OverdraftFeesCharges,
                "OverdraftInterestChargingCoverage": OverdraftInterestChargingCoverage,
                "RepresentativeAPR": RepresentativeAPR,
                "TierValueMax": TierValueMax,
            }
    
    TierValueMin: MetaOapg.properties.TierValueMin
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMin"]) -> MetaOapg.properties.TierValueMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankGuaranteedIndicator"]) -> MetaOapg.properties.BankGuaranteedIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EAR"]) -> MetaOapg.properties.EAR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Identification"]) -> MetaOapg.properties.Identification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftFeesCharges"]) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftInterestChargingCoverage"]) -> MetaOapg.properties.OverdraftInterestChargingCoverage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepresentativeAPR"]) -> MetaOapg.properties.RepresentativeAPR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TierValueMax"]) -> MetaOapg.properties.TierValueMax: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TierValueMin", "BankGuaranteedIndicator", "EAR", "Identification", "Notes", "OverdraftFeesCharges", "OverdraftInterestChargingCoverage", "RepresentativeAPR", "TierValueMax", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMin"]) -> MetaOapg.properties.TierValueMin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankGuaranteedIndicator"]) -> typing.Union[MetaOapg.properties.BankGuaranteedIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EAR"]) -> typing.Union[MetaOapg.properties.EAR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Identification"]) -> typing.Union[MetaOapg.properties.Identification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftFeesCharges"]) -> typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftInterestChargingCoverage"]) -> typing.Union[MetaOapg.properties.OverdraftInterestChargingCoverage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepresentativeAPR"]) -> typing.Union[MetaOapg.properties.RepresentativeAPR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TierValueMax"]) -> typing.Union[MetaOapg.properties.TierValueMax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TierValueMin", "BankGuaranteedIndicator", "EAR", "Identification", "Notes", "OverdraftFeesCharges", "OverdraftInterestChargingCoverage", "RepresentativeAPR", "TierValueMax", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        TierValueMin: typing.Union[MetaOapg.properties.TierValueMin, str, ],
        BankGuaranteedIndicator: typing.Union[MetaOapg.properties.BankGuaranteedIndicator, bool, schemas.Unset] = schemas.unset,
        EAR: typing.Union[MetaOapg.properties.EAR, str, schemas.Unset] = schemas.unset,
        Identification: typing.Union[MetaOapg.properties.Identification, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes', schemas.Unset] = schemas.unset,
        OverdraftFeesCharges: typing.Union['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges', schemas.Unset] = schemas.unset,
        OverdraftInterestChargingCoverage: typing.Union[MetaOapg.properties.OverdraftInterestChargingCoverage, str, schemas.Unset] = schemas.unset,
        RepresentativeAPR: typing.Union[MetaOapg.properties.RepresentativeAPR, str, schemas.Unset] = schemas.unset,
        TierValueMax: typing.Union[MetaOapg.properties.TierValueMax, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem':
        return super().__new__(
            cls,
            *args,
            TierValueMin=TierValueMin,
            BankGuaranteedIndicator=BankGuaranteedIndicator,
            EAR=EAR,
            Identification=Identification,
            Notes=Notes,
            OverdraftFeesCharges=OverdraftFeesCharges,
            OverdraftInterestChargingCoverage=OverdraftInterestChargingCoverage,
            RepresentativeAPR=RepresentativeAPR,
            TierValueMax=TierValueMax,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_notes import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemNotes
from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesCharges
