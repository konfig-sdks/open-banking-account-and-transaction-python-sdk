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


class OBReadProduct2DataProductItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Product details associated with the Account
    """


    class MetaOapg:
        required = {
            "AccountId",
            "ProductType",
        }
        
        class properties:
        
            @staticmethod
            def AccountId() -> typing.Type['AccountId']:
                return AccountId
            
            
            class ProductType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BUSINESS_CURRENT_ACCOUNT(cls):
                    return cls("BusinessCurrentAccount")
                
                @schemas.classproperty
                def COMMERCIAL_CREDIT_CARD(cls):
                    return cls("CommercialCreditCard")
                
                @schemas.classproperty
                def OTHER(cls):
                    return cls("Other")
                
                @schemas.classproperty
                def PERSONAL_CURRENT_ACCOUNT(cls):
                    return cls("PersonalCurrentAccount")
                
                @schemas.classproperty
                def SMELOAN(cls):
                    return cls("SMELoan")
        
            @staticmethod
            def BCA() -> typing.Type['OBBCAData1']:
                return OBBCAData1
            
            
            class MarketingStateId(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def OtherProductType() -> typing.Type['OBReadProduct2DataProductItemOtherProductType']:
                return OBReadProduct2DataProductItemOtherProductType
        
            @staticmethod
            def PCA() -> typing.Type['OBPCAData1']:
                return OBPCAData1
            
            
            class ProductId(
                schemas.StrSchema
            ):
                pass
            
            
            class ProductName(
                schemas.StrSchema
            ):
                pass
            
            
            class SecondaryProductId(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "AccountId": AccountId,
                "ProductType": ProductType,
                "BCA": BCA,
                "MarketingStateId": MarketingStateId,
                "OtherProductType": OtherProductType,
                "PCA": PCA,
                "ProductId": ProductId,
                "ProductName": ProductName,
                "SecondaryProductId": SecondaryProductId,
            }
    
    AccountId: 'AccountId'
    ProductType: MetaOapg.properties.ProductType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductType"]) -> MetaOapg.properties.ProductType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BCA"]) -> 'OBBCAData1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MarketingStateId"]) -> MetaOapg.properties.MarketingStateId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherProductType"]) -> 'OBReadProduct2DataProductItemOtherProductType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PCA"]) -> 'OBPCAData1': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductId"]) -> MetaOapg.properties.ProductId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductName"]) -> MetaOapg.properties.ProductName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SecondaryProductId"]) -> MetaOapg.properties.SecondaryProductId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AccountId", "ProductType", "BCA", "MarketingStateId", "OtherProductType", "PCA", "ProductId", "ProductName", "SecondaryProductId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountId"]) -> 'AccountId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductType"]) -> MetaOapg.properties.ProductType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BCA"]) -> typing.Union['OBBCAData1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MarketingStateId"]) -> typing.Union[MetaOapg.properties.MarketingStateId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherProductType"]) -> typing.Union['OBReadProduct2DataProductItemOtherProductType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PCA"]) -> typing.Union['OBPCAData1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductId"]) -> typing.Union[MetaOapg.properties.ProductId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductName"]) -> typing.Union[MetaOapg.properties.ProductName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SecondaryProductId"]) -> typing.Union[MetaOapg.properties.SecondaryProductId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AccountId", "ProductType", "BCA", "MarketingStateId", "OtherProductType", "PCA", "ProductId", "ProductName", "SecondaryProductId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AccountId: 'AccountId',
        ProductType: typing.Union[MetaOapg.properties.ProductType, str, ],
        BCA: typing.Union['OBBCAData1', schemas.Unset] = schemas.unset,
        MarketingStateId: typing.Union[MetaOapg.properties.MarketingStateId, str, schemas.Unset] = schemas.unset,
        OtherProductType: typing.Union['OBReadProduct2DataProductItemOtherProductType', schemas.Unset] = schemas.unset,
        PCA: typing.Union['OBPCAData1', schemas.Unset] = schemas.unset,
        ProductId: typing.Union[MetaOapg.properties.ProductId, str, schemas.Unset] = schemas.unset,
        ProductName: typing.Union[MetaOapg.properties.ProductName, str, schemas.Unset] = schemas.unset,
        SecondaryProductId: typing.Union[MetaOapg.properties.SecondaryProductId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItem':
        return super().__new__(
            cls,
            *args,
            AccountId=AccountId,
            ProductType=ProductType,
            BCA=BCA,
            MarketingStateId=MarketingStateId,
            OtherProductType=OtherProductType,
            PCA=PCA,
            ProductId=ProductId,
            ProductName=ProductName,
            SecondaryProductId=SecondaryProductId,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.model.ob_read_product2_data_product_item_other_product_type import OBReadProduct2DataProductItemOtherProductType
from open_banking_account_and_transaction_python_sdk.model.obbca_data1 import OBBCAData1
from open_banking_account_and_transaction_python_sdk.model.obpca_data1 import OBPCAData1
