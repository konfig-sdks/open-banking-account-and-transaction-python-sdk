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


class OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details of capital repayment holiday if any
    """


    class MetaOapg:
        
        class properties:
            MaxHolidayLength = schemas.IntSchema
            
            
            class MaxHolidayPeriod(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PACT": "PACT",
                        "PDAY": "PDAY",
                        "PHYR": "PHYR",
                        "PMTH": "PMTH",
                        "PQTR": "PQTR",
                        "PWEK": "PWEK",
                        "PYER": "PYER",
                    }
                
                @schemas.classproperty
                def PACT(cls):
                    return cls("PACT")
                
                @schemas.classproperty
                def PDAY(cls):
                    return cls("PDAY")
                
                @schemas.classproperty
                def PHYR(cls):
                    return cls("PHYR")
                
                @schemas.classproperty
                def PMTH(cls):
                    return cls("PMTH")
                
                @schemas.classproperty
                def PQTR(cls):
                    return cls("PQTR")
                
                @schemas.classproperty
                def PWEK(cls):
                    return cls("PWEK")
                
                @schemas.classproperty
                def PYER(cls):
                    return cls("PYER")
        
            @staticmethod
            def Notes() -> typing.Type['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes']:
                return OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes
            __annotations__ = {
                "MaxHolidayLength": MaxHolidayLength,
                "MaxHolidayPeriod": MaxHolidayPeriod,
                "Notes": Notes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaxHolidayLength"]) -> MetaOapg.properties.MaxHolidayLength: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaxHolidayPeriod"]) -> MetaOapg.properties.MaxHolidayPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["MaxHolidayLength", "MaxHolidayPeriod", "Notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaxHolidayLength"]) -> typing.Union[MetaOapg.properties.MaxHolidayLength, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaxHolidayPeriod"]) -> typing.Union[MetaOapg.properties.MaxHolidayPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["MaxHolidayLength", "MaxHolidayPeriod", "Notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        MaxHolidayLength: typing.Union[MetaOapg.properties.MaxHolidayLength, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        MaxHolidayPeriod: typing.Union[MetaOapg.properties.MaxHolidayPeriod, str, schemas.Unset] = schemas.unset,
        Notes: typing.Union['OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem':
        return super().__new__(
            cls,
            *args,
            MaxHolidayLength=MaxHolidayLength,
            MaxHolidayPeriod=MaxHolidayPeriod,
            Notes=Notes,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type_repayment_repayment_holiday_item_notes import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemNotes
