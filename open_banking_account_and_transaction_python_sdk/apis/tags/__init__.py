# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from open_banking_account_and_transaction_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    STATEMENTS = "Statements"
    ACCOUNT_ACCESS = "Account Access"
    PARTIES = "Parties"
    TRANSACTIONS = "Transactions"
    ACCOUNTS = "Accounts"
    BALANCES = "Balances"
    BENEFICIARIES = "Beneficiaries"
    DIRECT_DEBITS = "Direct Debits"
    OFFERS = "Offers"
    PRODUCTS = "Products"
    SCHEDULED_PAYMENTS = "Scheduled Payments"
    STANDING_ORDERS = "Standing Orders"
