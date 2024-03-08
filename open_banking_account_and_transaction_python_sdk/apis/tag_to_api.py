import typing_extensions

from open_banking_account_and_transaction_python_sdk.apis.tags import TagValues
from open_banking_account_and_transaction_python_sdk.apis.tags.statements_api import StatementsApi
from open_banking_account_and_transaction_python_sdk.apis.tags.account_access_api import AccountAccessApi
from open_banking_account_and_transaction_python_sdk.apis.tags.parties_api import PartiesApi
from open_banking_account_and_transaction_python_sdk.apis.tags.transactions_api import TransactionsApi
from open_banking_account_and_transaction_python_sdk.apis.tags.accounts_api import AccountsApi
from open_banking_account_and_transaction_python_sdk.apis.tags.balances_api import BalancesApi
from open_banking_account_and_transaction_python_sdk.apis.tags.beneficiaries_api import BeneficiariesApi
from open_banking_account_and_transaction_python_sdk.apis.tags.direct_debits_api import DirectDebitsApi
from open_banking_account_and_transaction_python_sdk.apis.tags.offers_api import OffersApi
from open_banking_account_and_transaction_python_sdk.apis.tags.products_api import ProductsApi
from open_banking_account_and_transaction_python_sdk.apis.tags.scheduled_payments_api import ScheduledPaymentsApi
from open_banking_account_and_transaction_python_sdk.apis.tags.standing_orders_api import StandingOrdersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.STATEMENTS: StatementsApi,
        TagValues.ACCOUNT_ACCESS: AccountAccessApi,
        TagValues.PARTIES: PartiesApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.BENEFICIARIES: BeneficiariesApi,
        TagValues.DIRECT_DEBITS: DirectDebitsApi,
        TagValues.OFFERS: OffersApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.SCHEDULED_PAYMENTS: ScheduledPaymentsApi,
        TagValues.STANDING_ORDERS: StandingOrdersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.STATEMENTS: StatementsApi,
        TagValues.ACCOUNT_ACCESS: AccountAccessApi,
        TagValues.PARTIES: PartiesApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.BENEFICIARIES: BeneficiariesApi,
        TagValues.DIRECT_DEBITS: DirectDebitsApi,
        TagValues.OFFERS: OffersApi,
        TagValues.PRODUCTS: ProductsApi,
        TagValues.SCHEDULED_PAYMENTS: ScheduledPaymentsApi,
        TagValues.STANDING_ORDERS: StandingOrdersApi,
    }
)
