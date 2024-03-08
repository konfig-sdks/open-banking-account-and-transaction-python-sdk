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


class OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Other fee type code which is not available in the standard code set
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem']:
            return OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem'], typing.List['OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeType':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem':
        return super().__getitem__(i)

from open_banking_account_and_transaction_python_sdk.model.obbca_data1_overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item import OBBCAData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem
