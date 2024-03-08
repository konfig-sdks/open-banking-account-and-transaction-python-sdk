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


class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCap(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about any caps (maximum charges) that apply to a particular fee/charge. Capping can either be based on an amount (in gbp), an amount (in items) or a rate.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem']:
            return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem'], typing.List['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCap':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem':
        return super().__getitem__(i)

from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem
