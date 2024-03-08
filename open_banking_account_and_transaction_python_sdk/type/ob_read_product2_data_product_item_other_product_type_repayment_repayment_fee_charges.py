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

from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_detail import OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail

class RequiredOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges(TypedDict):
    RepaymentFeeChargeDetail: OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetail

class OptionalOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges(TypedDict, total=False):
    RepaymentFeeChargeCap: OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCap

class OBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges(RequiredOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges, OptionalOBReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges):
    pass
