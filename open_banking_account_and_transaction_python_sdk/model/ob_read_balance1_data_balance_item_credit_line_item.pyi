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


class OBReadBalance1DataBalanceItemCreditLineItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Set of elements used to provide details on the credit line.
    """


    class MetaOapg:
        required = {
            "Included",
        }
        
        class properties:
            Included = schemas.BoolSchema
        
            @staticmethod
            def Amount() -> typing.Type['OBReadBalance1DataBalanceItemCreditLineItemAmount']:
                return OBReadBalance1DataBalanceItemCreditLineItemAmount
            
            
            class Type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("Available")
                
                @schemas.classproperty
                def CREDIT(cls):
                    return cls("Credit")
                
                @schemas.classproperty
                def EMERGENCY(cls):
                    return cls("Emergency")
                
                @schemas.classproperty
                def PREAGREED(cls):
                    return cls("Pre-Agreed")
                
                @schemas.classproperty
                def TEMPORARY(cls):
                    return cls("Temporary")
            __annotations__ = {
                "Included": Included,
                "Amount": Amount,
                "Type": Type,
            }
    
    Included: MetaOapg.properties.Included
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Included"]) -> MetaOapg.properties.Included: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Amount"]) -> 'OBReadBalance1DataBalanceItemCreditLineItemAmount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Included", "Amount", "Type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Included"]) -> MetaOapg.properties.Included: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Amount"]) -> typing.Union['OBReadBalance1DataBalanceItemCreditLineItemAmount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union[MetaOapg.properties.Type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Included", "Amount", "Type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Included: typing.Union[MetaOapg.properties.Included, bool, ],
        Amount: typing.Union['OBReadBalance1DataBalanceItemCreditLineItemAmount', schemas.Unset] = schemas.unset,
        Type: typing.Union[MetaOapg.properties.Type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadBalance1DataBalanceItemCreditLineItem':
        return super().__new__(
            cls,
            *args,
            Included=Included,
            Amount=Amount,
            Type=Type,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_read_balance1_data_balance_item_credit_line_item_amount import OBReadBalance1DataBalanceItemCreditLineItemAmount