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


class OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about any caps (maximum charges) that apply to a particular or group of fee/charge
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem']:
            return OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem'], typing.List['OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCap':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem':
        return super().__getitem__(i)

from open_banking_account_and_transaction_python_sdk.model.obbca_data1_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item import OBBCAData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem
