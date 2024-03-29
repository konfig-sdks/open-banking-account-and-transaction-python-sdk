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

from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_notes import OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_other_amount_type import OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_other_repayment_frequency import OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_other_repayment_type import OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges
from open_banking_account_and_transaction_python_sdk.pydantic.ob_read_product2_data_product_item_other_product_type_repayment_repayment_holiday import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday

class OBReadProduct2DataProductItemOtherProductTypeRepayment(BaseModel):
    # The repayment is for paying just the interest only or both interest and capital or bullet amount or balance to date etc
    amount_type: typing.Optional[Literal["RABD", "RABL", "RACI", "RAFC", "RAIO", "RALT", "USOT"]] = Field(None, alias='AmountType')

    notes: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentNotes] = Field(None, alias='Notes')

    other_amount_type: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType] = Field(None, alias='OtherAmountType')

    other_repayment_frequency: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency] = Field(None, alias='OtherRepaymentFrequency')

    other_repayment_type: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType] = Field(None, alias='OtherRepaymentType')

    repayment_fee_charges: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges] = Field(None, alias='RepaymentFeeCharges')

    # Repayment frequency
    repayment_frequency: typing.Optional[Literal["SMDA", "SMFL", "SMFO", "SMHY", "SMMO", "SMOT", "SMQU", "SMWE", "SMYE"]] = Field(None, alias='RepaymentFrequency')

    repayment_holiday: typing.Optional[OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHoliday] = Field(None, alias='RepaymentHoliday')

    # Repayment type
    repayment_type: typing.Optional[Literal["USBA", "USBU", "USCI", "USCS", "USER", "USFA", "USFB", "USFI", "USIO", "USOT", "USPF", "USRW", "USSL"]] = Field(None, alias='RepaymentType')
    class Config:
        arbitrary_types_allowed = True
