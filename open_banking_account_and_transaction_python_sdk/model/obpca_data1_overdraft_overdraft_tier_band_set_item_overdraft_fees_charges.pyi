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


class OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesCharges(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Overdraft fees and charges details
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem']:
            return OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem'], typing.List['OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesCharges':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem':
        return super().__getitem__(i)

from open_banking_account_and_transaction_python_sdk.model.obpca_data1_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item import OBPCAData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem
