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


class RequiredOBMerchantDetails1(TypedDict):
    pass

class OptionalOBMerchantDetails1(TypedDict, total=False):
    # Category code conform to ISO 18245, related to the type of services or goods the merchant provides for the transaction.
    MerchantCategoryCode: str

    # Name by which the merchant is known.
    MerchantName: str

class OBMerchantDetails1(RequiredOBMerchantDetails1, OptionalOBMerchantDetails1):
    pass