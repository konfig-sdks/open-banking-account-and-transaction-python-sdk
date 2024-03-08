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


class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeType(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Fee/charge type which is being capped
    """


    class MetaOapg:
        min_items = 1
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "ArrangedOverdraft": "ARRANGED_OVERDRAFT",
                    "AnnualReview": "ANNUAL_REVIEW",
                    "EmergencyBorrowing": "EMERGENCY_BORROWING",
                    "BorrowingItem": "BORROWING_ITEM",
                    "OverdraftRenewal": "OVERDRAFT_RENEWAL",
                    "OverdraftSetup": "OVERDRAFT_SETUP",
                    "Surcharge": "SURCHARGE",
                    "TempOverdraft": "TEMP_OVERDRAFT",
                    "UnauthorisedBorrowing": "UNAUTHORISED_BORROWING",
                    "UnauthorisedPaidTrans": "UNAUTHORISED_PAID_TRANS",
                    "Other": "OTHER",
                    "UnauthorisedUnpaidTrans": "UNAUTHORISED_UNPAID_TRANS",
                }
            
            @schemas.classproperty
            def ARRANGED_OVERDRAFT(cls):
                return cls("ArrangedOverdraft")
            
            @schemas.classproperty
            def ANNUAL_REVIEW(cls):
                return cls("AnnualReview")
            
            @schemas.classproperty
            def EMERGENCY_BORROWING(cls):
                return cls("EmergencyBorrowing")
            
            @schemas.classproperty
            def BORROWING_ITEM(cls):
                return cls("BorrowingItem")
            
            @schemas.classproperty
            def OVERDRAFT_RENEWAL(cls):
                return cls("OverdraftRenewal")
            
            @schemas.classproperty
            def OVERDRAFT_SETUP(cls):
                return cls("OverdraftSetup")
            
            @schemas.classproperty
            def SURCHARGE(cls):
                return cls("Surcharge")
            
            @schemas.classproperty
            def TEMP_OVERDRAFT(cls):
                return cls("TempOverdraft")
            
            @schemas.classproperty
            def UNAUTHORISED_BORROWING(cls):
                return cls("UnauthorisedBorrowing")
            
            @schemas.classproperty
            def UNAUTHORISED_PAID_TRANS(cls):
                return cls("UnauthorisedPaidTrans")
            
            @schemas.classproperty
            def OTHER(cls):
                return cls("Other")
            
            @schemas.classproperty
            def UNAUTHORISED_UNPAID_TRANS(cls):
                return cls("UnauthorisedUnpaidTrans")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeType':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
