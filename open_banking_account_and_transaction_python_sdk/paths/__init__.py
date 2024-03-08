# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from open_banking_account_and_transaction_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNTACCESSCONSENTS = "/account-access-consents"
    ACCOUNTACCESSCONSENTS_CONSENT_ID = "/account-access-consents/{ConsentId}"
    ACCOUNTS = "/accounts"
    ACCOUNTS_ACCOUNT_ID = "/accounts/{AccountId}"
    ACCOUNTS_ACCOUNT_ID_BALANCES = "/accounts/{AccountId}/balances"
    ACCOUNTS_ACCOUNT_ID_BENEFICIARIES = "/accounts/{AccountId}/beneficiaries"
    ACCOUNTS_ACCOUNT_ID_DIRECTDEBITS = "/accounts/{AccountId}/direct-debits"
    ACCOUNTS_ACCOUNT_ID_OFFERS = "/accounts/{AccountId}/offers"
    ACCOUNTS_ACCOUNT_ID_PARTIES = "/accounts/{AccountId}/parties"
    ACCOUNTS_ACCOUNT_ID_PARTY = "/accounts/{AccountId}/party"
    ACCOUNTS_ACCOUNT_ID_PRODUCT = "/accounts/{AccountId}/product"
    ACCOUNTS_ACCOUNT_ID_SCHEDULEDPAYMENTS = "/accounts/{AccountId}/scheduled-payments"
    ACCOUNTS_ACCOUNT_ID_STANDINGORDERS = "/accounts/{AccountId}/standing-orders"
    ACCOUNTS_ACCOUNT_ID_STATEMENTS = "/accounts/{AccountId}/statements"
    ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID = "/accounts/{AccountId}/statements/{StatementId}"
    ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID_FILE = "/accounts/{AccountId}/statements/{StatementId}/file"
    ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID_TRANSACTIONS = "/accounts/{AccountId}/statements/{StatementId}/transactions"
    ACCOUNTS_ACCOUNT_ID_TRANSACTIONS = "/accounts/{AccountId}/transactions"
    BALANCES = "/balances"
    BENEFICIARIES = "/beneficiaries"
    DIRECTDEBITS = "/direct-debits"
    OFFERS = "/offers"
    PARTY = "/party"
    PRODUCTS = "/products"
    SCHEDULEDPAYMENTS = "/scheduled-payments"
    STANDINGORDERS = "/standing-orders"
    STATEMENTS = "/statements"
    TRANSACTIONS = "/transactions"
