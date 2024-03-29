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


class OBReadScheduledPayment3Data(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class ScheduledPayment(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OBScheduledPayment3']:
                        return OBScheduledPayment3
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OBScheduledPayment3'], typing.List['OBScheduledPayment3']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ScheduledPayment':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OBScheduledPayment3':
                    return super().__getitem__(i)
            __annotations__ = {
                "ScheduledPayment": ScheduledPayment,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ScheduledPayment"]) -> MetaOapg.properties.ScheduledPayment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ScheduledPayment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ScheduledPayment"]) -> typing.Union[MetaOapg.properties.ScheduledPayment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ScheduledPayment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ScheduledPayment: typing.Union[MetaOapg.properties.ScheduledPayment, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OBReadScheduledPayment3Data':
        return super().__new__(
            cls,
            *args,
            ScheduledPayment=ScheduledPayment,
            _configuration=_configuration,
            **kwargs,
        )

from open_banking_account_and_transaction_python_sdk.model.ob_scheduled_payment3 import OBScheduledPayment3
