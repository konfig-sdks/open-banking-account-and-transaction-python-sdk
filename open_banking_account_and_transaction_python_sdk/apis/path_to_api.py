import typing_extensions

from open_banking_account_and_transaction_python_sdk.paths import PathValues
from open_banking_account_and_transaction_python_sdk.apis.paths.account_access_consents import AccountAccessConsents
from open_banking_account_and_transaction_python_sdk.apis.paths.account_access_consents_consent_id import AccountAccessConsentsConsentId
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts import Accounts
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id import AccountsAccountId
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_balances import AccountsAccountIdBalances
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_beneficiaries import AccountsAccountIdBeneficiaries
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_direct_debits import AccountsAccountIdDirectDebits
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_offers import AccountsAccountIdOffers
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_parties import AccountsAccountIdParties
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_party import AccountsAccountIdParty
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_product import AccountsAccountIdProduct
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_scheduled_payments import AccountsAccountIdScheduledPayments
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_standing_orders import AccountsAccountIdStandingOrders
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_statements import AccountsAccountIdStatements
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_statements_statement_id import AccountsAccountIdStatementsStatementId
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_statements_statement_id_file import AccountsAccountIdStatementsStatementIdFile
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_statements_statement_id_transactions import AccountsAccountIdStatementsStatementIdTransactions
from open_banking_account_and_transaction_python_sdk.apis.paths.accounts_account_id_transactions import AccountsAccountIdTransactions
from open_banking_account_and_transaction_python_sdk.apis.paths.balances import Balances
from open_banking_account_and_transaction_python_sdk.apis.paths.beneficiaries import Beneficiaries
from open_banking_account_and_transaction_python_sdk.apis.paths.direct_debits import DirectDebits
from open_banking_account_and_transaction_python_sdk.apis.paths.offers import Offers
from open_banking_account_and_transaction_python_sdk.apis.paths.party import Party
from open_banking_account_and_transaction_python_sdk.apis.paths.products import Products
from open_banking_account_and_transaction_python_sdk.apis.paths.scheduled_payments import ScheduledPayments
from open_banking_account_and_transaction_python_sdk.apis.paths.standing_orders import StandingOrders
from open_banking_account_and_transaction_python_sdk.apis.paths.statements import Statements
from open_banking_account_and_transaction_python_sdk.apis.paths.transactions import Transactions

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNTACCESSCONSENTS: AccountAccessConsents,
        PathValues.ACCOUNTACCESSCONSENTS_CONSENT_ID: AccountAccessConsentsConsentId,
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_BALANCES: AccountsAccountIdBalances,
        PathValues.ACCOUNTS_ACCOUNT_ID_BENEFICIARIES: AccountsAccountIdBeneficiaries,
        PathValues.ACCOUNTS_ACCOUNT_ID_DIRECTDEBITS: AccountsAccountIdDirectDebits,
        PathValues.ACCOUNTS_ACCOUNT_ID_OFFERS: AccountsAccountIdOffers,
        PathValues.ACCOUNTS_ACCOUNT_ID_PARTIES: AccountsAccountIdParties,
        PathValues.ACCOUNTS_ACCOUNT_ID_PARTY: AccountsAccountIdParty,
        PathValues.ACCOUNTS_ACCOUNT_ID_PRODUCT: AccountsAccountIdProduct,
        PathValues.ACCOUNTS_ACCOUNT_ID_SCHEDULEDPAYMENTS: AccountsAccountIdScheduledPayments,
        PathValues.ACCOUNTS_ACCOUNT_ID_STANDINGORDERS: AccountsAccountIdStandingOrders,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS: AccountsAccountIdStatements,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID: AccountsAccountIdStatementsStatementId,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID_FILE: AccountsAccountIdStatementsStatementIdFile,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID_TRANSACTIONS: AccountsAccountIdStatementsStatementIdTransactions,
        PathValues.ACCOUNTS_ACCOUNT_ID_TRANSACTIONS: AccountsAccountIdTransactions,
        PathValues.BALANCES: Balances,
        PathValues.BENEFICIARIES: Beneficiaries,
        PathValues.DIRECTDEBITS: DirectDebits,
        PathValues.OFFERS: Offers,
        PathValues.PARTY: Party,
        PathValues.PRODUCTS: Products,
        PathValues.SCHEDULEDPAYMENTS: ScheduledPayments,
        PathValues.STANDINGORDERS: StandingOrders,
        PathValues.STATEMENTS: Statements,
        PathValues.TRANSACTIONS: Transactions,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNTACCESSCONSENTS: AccountAccessConsents,
        PathValues.ACCOUNTACCESSCONSENTS_CONSENT_ID: AccountAccessConsentsConsentId,
        PathValues.ACCOUNTS: Accounts,
        PathValues.ACCOUNTS_ACCOUNT_ID: AccountsAccountId,
        PathValues.ACCOUNTS_ACCOUNT_ID_BALANCES: AccountsAccountIdBalances,
        PathValues.ACCOUNTS_ACCOUNT_ID_BENEFICIARIES: AccountsAccountIdBeneficiaries,
        PathValues.ACCOUNTS_ACCOUNT_ID_DIRECTDEBITS: AccountsAccountIdDirectDebits,
        PathValues.ACCOUNTS_ACCOUNT_ID_OFFERS: AccountsAccountIdOffers,
        PathValues.ACCOUNTS_ACCOUNT_ID_PARTIES: AccountsAccountIdParties,
        PathValues.ACCOUNTS_ACCOUNT_ID_PARTY: AccountsAccountIdParty,
        PathValues.ACCOUNTS_ACCOUNT_ID_PRODUCT: AccountsAccountIdProduct,
        PathValues.ACCOUNTS_ACCOUNT_ID_SCHEDULEDPAYMENTS: AccountsAccountIdScheduledPayments,
        PathValues.ACCOUNTS_ACCOUNT_ID_STANDINGORDERS: AccountsAccountIdStandingOrders,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS: AccountsAccountIdStatements,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID: AccountsAccountIdStatementsStatementId,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID_FILE: AccountsAccountIdStatementsStatementIdFile,
        PathValues.ACCOUNTS_ACCOUNT_ID_STATEMENTS_STATEMENT_ID_TRANSACTIONS: AccountsAccountIdStatementsStatementIdTransactions,
        PathValues.ACCOUNTS_ACCOUNT_ID_TRANSACTIONS: AccountsAccountIdTransactions,
        PathValues.BALANCES: Balances,
        PathValues.BENEFICIARIES: Beneficiaries,
        PathValues.DIRECTDEBITS: DirectDebits,
        PathValues.OFFERS: Offers,
        PathValues.PARTY: Party,
        PathValues.PRODUCTS: Products,
        PathValues.SCHEDULEDPAYMENTS: ScheduledPayments,
        PathValues.STANDINGORDERS: StandingOrders,
        PathValues.STATEMENTS: Statements,
        PathValues.TRANSACTIONS: Transactions,
    }
)
