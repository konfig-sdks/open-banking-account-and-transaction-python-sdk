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


class OBReadProduct2DataProductItemOtherProductTypeRepayment(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Repayment details of the Loan product
    """


    class MetaOapg:
        
        class properties:
            
            
            class AmountType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def RABD(cls):
                    return cls("RABD")
                
                @schemas.classproperty
                def RABL(cls):
                    return cls("RABL")
                
                @schemas.classproperty
                def RACI(cls):
                    return cls("RACI")
                
                @schemas.classproperty
                def RAFC(cls):
                    return cls("RAFC")
                
                @schemas.classproperty
                def RAIO(cls):
                    return cls("RAIO")
                
                @schemas.classproperty
                def RALT(cls):
                    return cls("RALT")
                
                @schemas.classproperty
                def USOT(cls):
                    return cls("USOT")
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes
        
            @staticmethod
            def OtherAmountType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType
        
            @staticmethod
            def OtherRepaymentFrequency() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency
        
            @staticmethod
            def OtherRepaymentType() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType
        
            @staticmethod
            def RepaymentFeeCharges() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges
            
            
            class RepaymentFrequency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SMDA(cls):
                    return cls("SMDA")
                
                @schemas.classproperty
                def SMFL(cls):
                    return cls("SMFL")
                
                @schemas.classproperty
                def SMFO(cls):
                    return cls("SMFO")
                
                @schemas.classproperty
                def SMHY(cls):
                    return cls("SMHY")
                
                @schemas.classproperty
                def SMMO(cls):
                    return cls("SMMO")
                
                @schemas.classproperty
                def SMOT(cls):
                    return cls("SMOT")
                
                @schemas.classproperty
                def SMQU(cls):
                    return cls("SMQU")
                
                @schemas.classproperty
                def SMWE(cls):
                    return cls("SMWE")
                
                @schemas.classproperty
                def SMYE(cls):
                    return cls("SMYE")
        
            @staticmethod
            def RepaymentHoliday() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday
            
            
            class RepaymentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USBA(cls):
                    return cls("USBA")
                
                @schemas.classproperty
                def USBU(cls):
                    return cls("USBU")
                
                @schemas.classproperty
                def USCI(cls):
                    return cls("USCI")
                
                @schemas.classproperty
                def USCS(cls):
                    return cls("USCS")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("USER")
                
                @schemas.classproperty
                def USFA(cls):
                    return cls("USFA")
                
                @schemas.classproperty
                def USFB(cls):
                    return cls("USFB")
                
                @schemas.classproperty
                def USFI(cls):
                    return cls("USFI")
                
                @schemas.classproperty
                def USIO(cls):
                    return cls("USIO")
                
                @schemas.classproperty
                def USOT(cls):
                    return cls("USOT")
                
                @schemas.classproperty
                def USPF(cls):
                    return cls("USPF")
                
                @schemas.classproperty
                def USRW(cls):
                    return cls("USRW")
                
                @schemas.classproperty
                def USSL(cls):
                    return cls("USSL")
            __annotations__ = {
                "AmountType": AmountType,
                "Notes": Notes,
                "OtherAmountType": OtherAmountType,
                "OtherRepaymentFrequency": OtherRepaymentFrequency,
                "OtherRepaymentType": OtherRepaymentType,
                "RepaymentFeeCharges": RepaymentFeeCharges,
                "RepaymentFrequency": RepaymentFrequency,
                "RepaymentHoliday": RepaymentHoliday,
                "RepaymentType": RepaymentType,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AmountType"]) -> MetaOapg.properties.AmountType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherAmountType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherRepaymentFrequency"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherRepaymentType"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepaymentFeeCharges"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepaymentFrequency"]) -> MetaOapg.properties.RepaymentFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepaymentHoliday"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RepaymentType"]) -> MetaOapg.properties.RepaymentType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AmountType", "Notes", "OtherAmountType", "OtherRepaymentFrequency", "OtherRepaymentType", "RepaymentFeeCharges", "RepaymentFrequency", "RepaymentHoliday", "RepaymentType", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AmountType"]) -> typing.Union[MetaOapg.properties.AmountType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherAmountType"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherRepaymentFrequency"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherRepaymentType"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepaymentFeeCharges"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepaymentFrequency"]) -> typing.Union[MetaOapg.properties.RepaymentFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepaymentHoliday"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RepaymentType"]) -> typing.Union[MetaOapg.properties.RepaymentType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AmountType", "Notes", "OtherAmountType", "OtherRepaymentFrequency", "OtherRepaymentType", "RepaymentFeeCharges", "RepaymentFrequency", "RepaymentHoliday", "RepaymentType", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AmountType: typing.Union[MetaOapg.properties.AmountType, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes', schemas.Unset] = schemas.unset,
        OtherAmountType: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType', schemas.Unset] = schemas.unset,
        OtherRepaymentFrequency: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency', schemas.Unset] = schemas.unset,
        OtherRepaymentType: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType', schemas.Unset] = schemas.unset,
        RepaymentFeeCharges: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges', schemas.Unset] = schemas.unset,
        RepaymentFrequency: typing.Union[MetaOapg.properties.RepaymentFrequency, str, schemas.Unset] = schemas.unset,
        RepaymentHoliday: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday', schemas.Unset] = schemas.unset,
        RepaymentType: typing.Union[MetaOapg.properties.RepaymentType, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeRepayment':
        return super().__new__(
            cls,
            *args,
            AmountType=AmountType,
            Notes=Notes,
            OtherAmountType=OtherAmountType,
            OtherRepaymentFrequency=OtherRepaymentFrequency,
            OtherRepaymentType=OtherRepaymentType,
            RepaymentFeeCharges=RepaymentFeeCharges,
            RepaymentFrequency=RepaymentFrequency,
            RepaymentHoliday=RepaymentHoliday,
            RepaymentType=RepaymentType,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_notes import OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_other_amount_type import OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_other_repayment_frequency import OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_other_repayment_type import OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_repayment_holiday import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday
