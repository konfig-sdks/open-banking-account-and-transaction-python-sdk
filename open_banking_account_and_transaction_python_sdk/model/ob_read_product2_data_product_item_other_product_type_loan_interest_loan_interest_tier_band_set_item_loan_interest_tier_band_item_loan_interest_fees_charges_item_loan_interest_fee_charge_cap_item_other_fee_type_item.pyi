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


class OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Other fee type code which is not available in the standard code set
    """


    class MetaOapg:
        required = {
            "Description",
            "Name",
        }
        
        class properties:
        
            @staticmethod
            def Description() -> typing.Type['Description3']:
                return Description3
        
            @staticmethod
            def Name() -> typing.Type['Name4']:
                return Name4
        
            @staticmethod
            def Code() -> typing.Type['OBCodeMnemonic']:
                return OBCodeMnemonic
            __annotations__ = {
                "Description": Description,
                "Name": Name,
                "Code": Code,
            }
    
    Description: 'Description3'
    Name: 'Name4'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> 'Description3': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> 'Name4': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Code"]) -> 'OBCodeMnemonic': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Description", "Name", "Code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> 'Description3': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> 'Name4': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Code"]) -> typing.Union['OBCodeMnemonic', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Description", "Name", "Code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Description: 'Description3',
        Name: 'Name4',
        Code: typing.Union['OBCodeMnemonic', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItemOtherFeeTypeItem':
        return super().__new__(
            cls,
            *args,
            Description=Description,
            Name=Name,
            Code=Code,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.description3 import Description3
from open_banking_account_and_transaction_python_sdk.model.name4 import Name4
from open_banking_account_and_transaction_python_sdk.model.ob_code_mnemonic import OBCodeMnemonic
