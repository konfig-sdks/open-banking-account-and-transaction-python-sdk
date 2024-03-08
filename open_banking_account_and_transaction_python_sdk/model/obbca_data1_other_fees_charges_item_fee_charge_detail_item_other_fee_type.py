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


class OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Other Fee/charge type which is not available in the standard code set
    """


    class MetaOapg:
        required = {
            "Description",
            "FeeCategory",
            "Name",
        }
        
        class properties:
            
            
            class Description(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 350
                    min_length = 1
            
            
            class FeeCategory(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Other": "OTHER",
                        "Servicing": "SERVICING",
                    }
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def SERVICING(cls):
                    return cls("Servicing")
            
            
            class Name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 70
                    min_length = 1
            
            
            class Code(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 4
                    min_length = 0
                    regex=[{
                        'pattern': r'^\w{0,4}$',
                    }]
            __annotations__ = {
                "Description": Description,
                "FeeCategory": FeeCategory,
                "Name": Name,
                "Code": Code,
            }
    
    Description: MetaOapg.properties.Description
    FeeCategory: MetaOapg.properties.FeeCategory
    Name: MetaOapg.properties.Name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeeCategory"]) -> MetaOapg.properties.FeeCategory: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Code"]) -> MetaOapg.properties.Code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Description", "FeeCategory", "Name", "Code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeeCategory"]) -> MetaOapg.properties.FeeCategory: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Code"]) -> typing.Union[MetaOapg.properties.Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Description", "FeeCategory", "Name", "Code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: typing.Union[MetaOapg.properties.Description, str, ],
        FeeCategory: typing.Union[MetaOapg.properties.FeeCategory, str, ],
        Name: typing.Union[MetaOapg.properties.Name, str, ],
        Code: typing.Union[MetaOapg.properties.Code, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            FeeCategory=FeeCategory,
            Name=Name,
            Code=Code,
            _configuration=_configuration,
            **kwargs,
        )
