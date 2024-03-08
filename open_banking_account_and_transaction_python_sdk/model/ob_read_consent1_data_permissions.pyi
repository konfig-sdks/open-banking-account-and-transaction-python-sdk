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


class OBReadConsent1DataPermissions(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def READ_ACCOUNTS_BASIC(cls):
                return cls("ReadAccountsBasic")
            
            @schemas.classproperty
            def READ_ACCOUNTS_DETAIL(cls):
                return cls("ReadAccountsDetail")
            
            @schemas.classproperty
            def READ_BALANCES(cls):
                return cls("ReadBalances")
            
            @schemas.classproperty
            def READ_BENEFICIARIES_BASIC(cls):
                return cls("ReadBeneficiariesBasic")
            
            @schemas.classproperty
            def READ_BENEFICIARIES_DETAIL(cls):
                return cls("ReadBeneficiariesDetail")
            
            @schemas.classproperty
            def READ_DIRECT_DEBITS(cls):
                return cls("ReadDirectDebits")
            
            @schemas.classproperty
            def READ_OFFERS(cls):
                return cls("ReadOffers")
            
            @schemas.classproperty
            def READ_PAN(cls):
                return cls("ReadPAN")
            
            @schemas.classproperty
            def READ_PARTY(cls):
                return cls("ReadParty")
            
            @schemas.classproperty
            def READ_PARTY_PSU(cls):
                return cls("ReadPartyPSU")
            
            @schemas.classproperty
            def READ_PRODUCTS(cls):
                return cls("ReadProducts")
            
            @schemas.classproperty
            def READ_SCHEDULED_PAYMENTS_BASIC(cls):
                return cls("ReadScheduledPaymentsBasic")
            
            @schemas.classproperty
            def READ_SCHEDULED_PAYMENTS_DETAIL(cls):
                return cls("ReadScheduledPaymentsDetail")
            
            @schemas.classproperty
            def READ_STANDING_ORDERS_BASIC(cls):
                return cls("ReadStandingOrdersBasic")
            
            @schemas.classproperty
            def READ_STANDING_ORDERS_DETAIL(cls):
                return cls("ReadStandingOrdersDetail")
            
            @schemas.classproperty
            def READ_STATEMENTS_BASIC(cls):
                return cls("ReadStatementsBasic")
            
            @schemas.classproperty
            def READ_STATEMENTS_DETAIL(cls):
                return cls("ReadStatementsDetail")
            
            @schemas.classproperty
            def READ_TRANSACTIONS_BASIC(cls):
                return cls("ReadTransactionsBasic")
            
            @schemas.classproperty
            def READ_TRANSACTIONS_CREDITS(cls):
                return cls("ReadTransactionsCredits")
            
            @schemas.classproperty
            def READ_TRANSACTIONS_DEBITS(cls):
                return cls("ReadTransactionsDebits")
            
            @schemas.classproperty
            def READ_TRANSACTIONS_DETAIL(cls):
                return cls("ReadTransactionsDetail")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OBReadConsent1DataPermissions':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
