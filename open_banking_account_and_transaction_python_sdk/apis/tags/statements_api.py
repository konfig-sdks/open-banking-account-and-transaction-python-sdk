# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_statements.get import Get
from open_banking_account_and_transaction_python_sdk.paths.statements.get import GetAll
from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_statements_statement_id.get import GetDetails
from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_statements_statement_id_file.get import GetFile
from open_banking_account_and_transaction_python_sdk.apis.tags.statements_api_raw import StatementsApiRaw


class StatementsApi(
    Get,
    GetAll,
    GetDetails,
    GetFile,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: StatementsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = StatementsApiRaw(api_client)
