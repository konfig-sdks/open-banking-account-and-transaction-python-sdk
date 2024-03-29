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


class OBPCAData1Overdraft(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about Overdraft rates, fees & charges
    """


    class MetaOapg:
        required = {
            "OverdraftTierBandSet",
        }
        
        class properties:
        
            @staticmethod
            def OverdraftTierBandSet() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSet']:
                return OBPCAData1OverdraftOverdraftTierBandSet
        
            @staticmethod
            def Notes() -> typing.Type['OBPCAData1OverdraftNotes']:
                return OBPCAData1OverdraftNotes
            __annotations__ = {
                "OverdraftTierBandSet": OverdraftTierBandSet,
                "Notes": Notes,
            }
    
    OverdraftTierBandSet: 'OBPCAData1OverdraftOverdraftTierBandSet'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OverdraftTierBandSet"]) -> 'OBPCAData1OverdraftOverdraftTierBandSet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Notes"]) -> 'OBPCAData1OverdraftNotes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OverdraftTierBandSet", "Notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OverdraftTierBandSet"]) -> 'OBPCAData1OverdraftOverdraftTierBandSet': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Notes"]) -> typing.Union['OBPCAData1OverdraftNotes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OverdraftTierBandSet", "Notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        OverdraftTierBandSet: 'OBPCAData1OverdraftOverdraftTierBandSet',
        Notes: typing.Union['OBPCAData1OverdraftNotes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBPCAData1Overdraft':
        return super().__new__(
            cls,
            *args,
            OverdraftTierBandSet=OverdraftTierBandSet,
            Notes=Notes,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_notes import OBPCAData1OverdraftNotes
from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set import OBPCAData1OverdraftOverdraftTierBandSet
