# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCap
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetail
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_other_fees_charges_item_other_tariff_type import OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType

class OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem(BaseModel):
    fee_charge_detail: OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetail = Field(alias='FeeChargeDetail')

    fee_charge_cap: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCap] = Field(None, alias='FeeChargeCap')

    other_tariff_type: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType] = Field(None, alias='OtherTariffType')

    # Name of the tariff
    tariff_name: typing.Optional[str] = Field(None, alias='TariffName')

    # TariffType which defines the fee and charges.
    tariff_type: typing.Optional[Literal["TTEL", "TTMX", "TTOT"]] = Field(None, alias='TariffType')
    class Config:
        arbitrary_types_allowed = True
