# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_party.get import GetByAccountId
from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_parties.get import GetList
from open_banking_account_and_transaction_python_sdk.paths.party.get import GetList0
from open_banking_account_and_transaction_python_sdk.apis.tags.parties_api_raw import PartiesApiRaw


class PartiesApi(
    GetByAccountId,
    GetList,
    GetList0,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PartiesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PartiesApiRaw(api_client)