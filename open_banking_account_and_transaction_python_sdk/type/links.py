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


class RequiredLinks(TypedDict):
    Self: str

class OptionalLinks(TypedDict, total=False):
    First: str

    Last: str

    Next: str

    Prev: str

class Links(RequiredLinks, OptionalLinks):
    pass