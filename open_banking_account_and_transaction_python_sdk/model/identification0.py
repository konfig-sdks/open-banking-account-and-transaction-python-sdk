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


class Identification0(
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Identification assigned by an institution to identify an account. This identification is known by the account owner.
    """


    class MetaOapg:
        max_length = 256
        min_length = 1
