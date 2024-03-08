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


class OBBCAData1CreditInterestTierBandSetItemTierBand(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Tier Band Details
    """


    class MetaOapg:
        min_items = 1
        
        @staticmethod
        def items() -> typing.Type['OBBCAData1CreditInterestTierBandSetItemTierBandItem']:
            return OBBCAData1CreditInterestTierBandSetItemTierBandItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBBCAData1CreditInterestTierBandSetItemTierBandItem'], typing.List['OBBCAData1CreditInterestTierBandSetItemTierBandItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1CreditInterestTierBandSetItemTierBand':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBBCAData1CreditInterestTierBandSetItemTierBandItem':
        return super().__getitem__(i)

from open_banking_account_and_transaction_python_sdk.model.obbca_data1_credit_interest_tier_band_set_item_tier_band_item import OBBCAData1CreditInterestTierBandSetItemTierBandItem
