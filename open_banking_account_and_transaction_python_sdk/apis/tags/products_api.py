# coding: utf-8

"""
    Account and Transaction API Specification

    Swagger for Account and Transaction API Specification

    The version of the OpenAPI document: 3.1.7
    Contact: ServiceDesk@openbanking.org.uk
    Generated by: https://konfigthis.com
"""

from open_banking_account_and_transaction_python_sdk.paths.accounts_account_id_product.get import GetByAccountId
from open_banking_account_and_transaction_python_sdk.paths.products.get import List
from open_banking_account_and_transaction_python_sdk.apis.tags.products_api_raw import ProductsApiRaw


class ProductsApi(
    GetByAccountId,
    List,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProductsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProductsApiRaw(api_client)