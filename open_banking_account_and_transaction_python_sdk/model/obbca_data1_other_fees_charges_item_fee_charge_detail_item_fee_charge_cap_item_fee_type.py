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


class OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeType(
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
                    "Other": "OTHER",
                    "ServiceCAccountFee": "SERVICE_CACCOUNT_FEE",
                    "ServiceCAccountFeeMonthly": "SERVICE_CACCOUNT_FEE_MONTHLY",
                    "ServiceCAccountFeeQuarterly": "SERVICE_CACCOUNT_FEE_QUARTERLY",
                    "ServiceCFixedTariff": "SERVICE_CFIXED_TARIFF",
                    "ServiceCBusiDepAccBreakage": "SERVICE_CBUSI_DEP_ACC_BREAKAGE",
                    "ServiceCMinimumMonthlyFee": "SERVICE_CMINIMUM_MONTHLY_FEE",
                    "ServiceCOther": "SERVICE_COTHER",
                }
            
            @schemas.classproperty
            def OTHER(cls):
                return cls("Other")
            
            @schemas.classproperty
            def SERVICE_CACCOUNT_FEE(cls):
                return cls("ServiceCAccountFee")
            
            @schemas.classproperty
            def SERVICE_CACCOUNT_FEE_MONTHLY(cls):
                return cls("ServiceCAccountFeeMonthly")
            
            @schemas.classproperty
            def SERVICE_CACCOUNT_FEE_QUARTERLY(cls):
                return cls("ServiceCAccountFeeQuarterly")
            
            @schemas.classproperty
            def SERVICE_CFIXED_TARIFF(cls):
                return cls("ServiceCFixedTariff")
            
            @schemas.classproperty
            def SERVICE_CBUSI_DEP_ACC_BREAKAGE(cls):
                return cls("ServiceCBusiDepAccBreakage")
            
            @schemas.classproperty
            def SERVICE_CMINIMUM_MONTHLY_FEE(cls):
                return cls("ServiceCMinimumMonthlyFee")
            
            @schemas.classproperty
            def SERVICE_COTHER(cls):
                return cls("ServiceCOther")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeType':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
