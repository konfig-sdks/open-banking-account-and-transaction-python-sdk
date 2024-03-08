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


class OBStatement2StatementDateTime(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['OBStatement2StatementDateTimeItem']:
            return OBStatement2StatementDateTimeItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['OBStatement2StatementDateTimeItem'], typing.List['OBStatement2StatementDateTimeItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBStatement2StatementDateTime':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'OBStatement2StatementDateTimeItem':
        return super().__getitem__(i)

from open_banking_account_and_transaction_python_sdk.model.ob_statement2_statement_date_time_item import OBStatement2StatementDateTimeItem
