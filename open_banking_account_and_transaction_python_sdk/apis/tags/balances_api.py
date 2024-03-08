# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_balances.get import Get
from open_banking_account_and_transaction_python_sdk.paths.balances.get import GetAll
from open_banking_account_and_transaction_python_sdk.apis.tags.balances_api_raw import BalancesApiRaw


class BalancesApi(
    Get,
    GetAll,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BalancesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BalancesApiRaw(api_client)