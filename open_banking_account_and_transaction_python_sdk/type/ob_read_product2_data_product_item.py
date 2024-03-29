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

from open_banking_account_and_transaction_python_sdk.type.account_id import AccountId
from open_banking_account_and_transaction_python_sdk.type.ob_read_product2_data_product_item_other_product_type import OBReadProduct2DataProductItemOtherProductType
from open_banking_account_and_transaction_python_sdk.type.obbca_data1 import OBBCAData1
from open_banking_account_and_transaction_python_sdk.type.obpca_data1 import OBPCAData1

class RequiredOBReadProduct2DataProductItem(TypedDict):
    AccountId: AccountId

    # Product type : Personal Current Account, Business Current Account
    ProductType: str

class OptionalOBReadProduct2DataProductItem(TypedDict, total=False):
    BCA: OBBCAData1

    # Unique and unambiguous identification of a  Product Marketing State.
    MarketingStateId: str

    OtherProductType: OBReadProduct2DataProductItemOtherProductType

    PCA: OBPCAData1

    # The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers.
    ProductId: str

    # The name of the Product used for marketing purposes from a customer perspective. I.e. what the customer would recognise.
    ProductName: str

    # Any secondary Identification which  supports Product Identifier to uniquely identify the current account banking products.
    SecondaryProductId: str

class OBReadProduct2DataProductItem(RequiredOBReadProduct2DataProductItem, OptionalOBReadProduct2DataProductItem):
    pass
