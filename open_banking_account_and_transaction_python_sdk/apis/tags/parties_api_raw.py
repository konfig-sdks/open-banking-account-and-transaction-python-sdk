# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_party.get import GetByAccountIdRaw
from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_parties.get import GetListRaw
from open_banking_account_and_transaction_python_sdk.paths.party.get import GetList0Raw


class PartiesApiRaw(
    GetByAccountIdRaw,
    GetListRaw,
    GetList0Raw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
