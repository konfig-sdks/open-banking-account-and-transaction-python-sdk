<div align="center">

[![Visit Open banking](./header.png)](https://www.openbanking.org.uk&#x2F;)

# Open banking<a id="open-banking"></a>

Swagger for Account and Transaction API Specification


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`openbankingaccountandtransaction.account_access.create_consent`](#openbankingaccountandtransactionaccount_accesscreate_consent)
  * [`openbankingaccountandtransaction.account_access.delete_consent`](#openbankingaccountandtransactionaccount_accessdelete_consent)
  * [`openbankingaccountandtransaction.account_access.get_consent`](#openbankingaccountandtransactionaccount_accessget_consent)
  * [`openbankingaccountandtransaction.accounts.get`](#openbankingaccountandtransactionaccountsget)
  * [`openbankingaccountandtransaction.accounts.get_all`](#openbankingaccountandtransactionaccountsget_all)
  * [`openbankingaccountandtransaction.balances.get`](#openbankingaccountandtransactionbalancesget)
  * [`openbankingaccountandtransaction.balances.get_all`](#openbankingaccountandtransactionbalancesget_all)
  * [`openbankingaccountandtransaction.beneficiaries.get_all`](#openbankingaccountandtransactionbeneficiariesget_all)
  * [`openbankingaccountandtransaction.beneficiaries.get_all_0`](#openbankingaccountandtransactionbeneficiariesget_all_0)
  * [`openbankingaccountandtransaction.direct_debits.get_all`](#openbankingaccountandtransactiondirect_debitsget_all)
  * [`openbankingaccountandtransaction.direct_debits.list`](#openbankingaccountandtransactiondirect_debitslist)
  * [`openbankingaccountandtransaction.offers.get_by_id`](#openbankingaccountandtransactionoffersget_by_id)
  * [`openbankingaccountandtransaction.offers.list`](#openbankingaccountandtransactionofferslist)
  * [`openbankingaccountandtransaction.parties.get_by_account_id`](#openbankingaccountandtransactionpartiesget_by_account_id)
  * [`openbankingaccountandtransaction.parties.get_list`](#openbankingaccountandtransactionpartiesget_list)
  * [`openbankingaccountandtransaction.parties.get_list_0`](#openbankingaccountandtransactionpartiesget_list_0)
  * [`openbankingaccountandtransaction.products.get_by_account_id`](#openbankingaccountandtransactionproductsget_by_account_id)
  * [`openbankingaccountandtransaction.products.list`](#openbankingaccountandtransactionproductslist)
  * [`openbankingaccountandtransaction.scheduled_payments.get_all`](#openbankingaccountandtransactionscheduled_paymentsget_all)
  * [`openbankingaccountandtransaction.scheduled_payments.get_all_0`](#openbankingaccountandtransactionscheduled_paymentsget_all_0)
  * [`openbankingaccountandtransaction.standing_orders.get`](#openbankingaccountandtransactionstanding_ordersget)
  * [`openbankingaccountandtransaction.standing_orders.get_all`](#openbankingaccountandtransactionstanding_ordersget_all)
  * [`openbankingaccountandtransaction.statements.get`](#openbankingaccountandtransactionstatementsget)
  * [`openbankingaccountandtransaction.statements.get_all`](#openbankingaccountandtransactionstatementsget_all)
  * [`openbankingaccountandtransaction.statements.get_details`](#openbankingaccountandtransactionstatementsget_details)
  * [`openbankingaccountandtransaction.statements.get_file`](#openbankingaccountandtransactionstatementsget_file)
  * [`openbankingaccountandtransaction.transactions.get_details`](#openbankingaccountandtransactiontransactionsget_details)
  * [`openbankingaccountandtransaction.transactions.get_details_0`](#openbankingaccountandtransactiontransactionsget_details_0)
  * [`openbankingaccountandtransaction.transactions.get_details_1`](#openbankingaccountandtransactiontransactionsget_details_1)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Open%20Banking&serviceName=Account%20and%20Transaction&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from open_banking_account_and_transaction_python_sdk import (
    OpenBankingAccountAndTransaction,
    ApiException,
)

openbankingaccountandtransaction = OpenBankingAccountAndTransaction(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Create Account Access Consents
    create_consent_response = (
        openbankingaccountandtransaction.account_access.create_consent(
            data={
                "permissions": ["ReadAccountsBasic"],
            },
            risk={},
            x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
            x_fapi_customer_ip_address="string_example",
            x_fapi_interaction_id="string_example",
            x_customer_user_agent="string_example",
        )
    )
    print(create_consent_response)
except ApiException as e:
    print("Exception when calling AccountAccessApi.create_consent: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["errors"])
        pprint(e.body["message"])
        pprint(e.body["id"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["errors"])
        pprint(e.body["message"])
        pprint(e.body["id"])
    if e.status == 403:
        pprint(e.body["code"])
        pprint(e.body["errors"])
        pprint(e.body["message"])
        pprint(e.body["id"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from open_banking_account_and_transaction_python_sdk import (
    OpenBankingAccountAndTransaction,
    ApiException,
)

openbankingaccountandtransaction = OpenBankingAccountAndTransaction(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Create Account Access Consents
        create_consent_response = (
            await openbankingaccountandtransaction.account_access.acreate_consent(
                data={
                    "permissions": ["ReadAccountsBasic"],
                },
                risk={},
                x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
                x_fapi_customer_ip_address="string_example",
                x_fapi_interaction_id="string_example",
                x_customer_user_agent="string_example",
            )
        )
        print(create_consent_response)
    except ApiException as e:
        print("Exception when calling AccountAccessApi.create_consent: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["code"])
            pprint(e.body["errors"])
            pprint(e.body["message"])
            pprint(e.body["id"])
        if e.status == 500:
            pprint(e.body["code"])
            pprint(e.body["errors"])
            pprint(e.body["message"])
            pprint(e.body["id"])
        if e.status == 403:
            pprint(e.body["code"])
            pprint(e.body["errors"])
            pprint(e.body["message"])
            pprint(e.body["id"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from open_banking_account_and_transaction_python_sdk import (
    OpenBankingAccountAndTransaction,
    ApiException,
)

openbankingaccountandtransaction = OpenBankingAccountAndTransaction(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Create Account Access Consents
    create_consent_response = (
        openbankingaccountandtransaction.account_access.raw.create_consent(
            data={
                "permissions": ["ReadAccountsBasic"],
            },
            risk={},
            x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
            x_fapi_customer_ip_address="string_example",
            x_fapi_interaction_id="string_example",
            x_customer_user_agent="string_example",
        )
    )
    pprint(create_consent_response.body)
    pprint(create_consent_response.body["data"])
    pprint(create_consent_response.body["risk"])
    pprint(create_consent_response.body["links"])
    pprint(create_consent_response.body["meta"])
    pprint(create_consent_response.headers)
    pprint(create_consent_response.status)
    pprint(create_consent_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountAccessApi.create_consent: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["code"])
        pprint(e.body["errors"])
        pprint(e.body["message"])
        pprint(e.body["id"])
    if e.status == 500:
        pprint(e.body["code"])
        pprint(e.body["errors"])
        pprint(e.body["message"])
        pprint(e.body["id"])
    if e.status == 403:
        pprint(e.body["code"])
        pprint(e.body["errors"])
        pprint(e.body["message"])
        pprint(e.body["id"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `openbankingaccountandtransaction.account_access.create_consent`<a id="openbankingaccountandtransactionaccount_accesscreate_consent"></a>

Create Account Access Consents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_consent_response = (
    openbankingaccountandtransaction.account_access.create_consent(
        data={
            "permissions": ["ReadAccountsBasic"],
        },
        risk={},
        x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
        x_fapi_customer_ip_address="string_example",
        x_fapi_interaction_id="string_example",
        x_customer_user_agent="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data: [`OBReadConsent1Data`](./open_banking_account_and_transaction_python_sdk/type/ob_read_consent1_data.py)<a id="data-obreadconsent1dataopen_banking_account_and_transaction_python_sdktypeob_read_consent1_datapy"></a>


##### risk: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="risk-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The Risk section is sent by the initiating party to the ASPSP. It is used to specify additional details for risk scoring for Account Info.

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OBReadConsent1`](./open_banking_account_and_transaction_python_sdk/type/ob_read_consent1.py)
Default

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadConsentResponse1`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_consent_response1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account-access-consents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.account_access.delete_consent`<a id="openbankingaccountandtransactionaccount_accessdelete_consent"></a>

Delete Account Access Consents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
openbankingaccountandtransaction.account_access.delete_consent(
    consent_id="ConsentId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent_id: `str`<a id="consent_id-str"></a>

ConsentId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account-access-consents/{ConsentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.account_access.get_consent`<a id="openbankingaccountandtransactionaccount_accessget_consent"></a>

Get Account Access Consents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_consent_response = openbankingaccountandtransaction.account_access.get_consent(
    consent_id="ConsentId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### consent_id: `str`<a id="consent_id-str"></a>

ConsentId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadConsentResponse1`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_consent_response1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/account-access-consents/{ConsentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.accounts.get`<a id="openbankingaccountandtransactionaccountsget"></a>

Get Accounts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = openbankingaccountandtransaction.accounts.get(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadAccount6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_account6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.accounts.get_all`<a id="openbankingaccountandtransactionaccountsget_all"></a>

Get Accounts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.accounts.get_all(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadAccount6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_account6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.balances.get`<a id="openbankingaccountandtransactionbalancesget"></a>

Get Balances

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = openbankingaccountandtransaction.balances.get(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadBalance1`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_balance1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/balances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.balances.get_all`<a id="openbankingaccountandtransactionbalancesget_all"></a>

Get Balances

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.balances.get_all(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadBalance1`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_balance1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/balances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.beneficiaries.get_all`<a id="openbankingaccountandtransactionbeneficiariesget_all"></a>

Get Beneficiaries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.beneficiaries.get_all(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadBeneficiary5`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_beneficiary5.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/beneficiaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.beneficiaries.get_all_0`<a id="openbankingaccountandtransactionbeneficiariesget_all_0"></a>

Get Beneficiaries

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_0_response = openbankingaccountandtransaction.beneficiaries.get_all_0(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadBeneficiary5`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_beneficiary5.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/beneficiaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.direct_debits.get_all`<a id="openbankingaccountandtransactiondirect_debitsget_all"></a>

Get Direct Debits

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.direct_debits.get_all(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadDirectDebit2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_direct_debit2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/direct-debits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.direct_debits.list`<a id="openbankingaccountandtransactiondirect_debitslist"></a>

Get Direct Debits

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = openbankingaccountandtransaction.direct_debits.list(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadDirectDebit2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_direct_debit2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/direct-debits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.offers.get_by_id`<a id="openbankingaccountandtransactionoffersget_by_id"></a>

Get Offers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = openbankingaccountandtransaction.offers.get_by_id(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadOffer1`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_offer1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/offers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.offers.list`<a id="openbankingaccountandtransactionofferslist"></a>

Get Offers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = openbankingaccountandtransaction.offers.list(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadOffer1`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_offer1.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/offers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.parties.get_by_account_id`<a id="openbankingaccountandtransactionpartiesget_by_account_id"></a>

Get Parties

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = openbankingaccountandtransaction.parties.get_by_account_id(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadParty2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_party2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/party` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.parties.get_list`<a id="openbankingaccountandtransactionpartiesget_list"></a>

Get Parties

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = openbankingaccountandtransaction.parties.get_list(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadParty3`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_party3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/parties` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.parties.get_list_0`<a id="openbankingaccountandtransactionpartiesget_list_0"></a>

Get Parties

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_0_response = openbankingaccountandtransaction.parties.get_list_0(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadParty2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_party2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/party` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.products.get_by_account_id`<a id="openbankingaccountandtransactionproductsget_by_account_id"></a>

Get Products

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_account_id_response = (
    openbankingaccountandtransaction.products.get_by_account_id(
        account_id="AccountId_example",
        x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
        x_fapi_customer_ip_address="string_example",
        x_fapi_interaction_id="string_example",
        x_customer_user_agent="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadProduct2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_product2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/product` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.products.list`<a id="openbankingaccountandtransactionproductslist"></a>

Get Products

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = openbankingaccountandtransaction.products.list(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadProduct2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_product2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/products` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.scheduled_payments.get_all`<a id="openbankingaccountandtransactionscheduled_paymentsget_all"></a>

Get Scheduled Payments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.scheduled_payments.get_all(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadScheduledPayment3`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_scheduled_payment3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/scheduled-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.scheduled_payments.get_all_0`<a id="openbankingaccountandtransactionscheduled_paymentsget_all_0"></a>

Get Scheduled Payments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_0_response = openbankingaccountandtransaction.scheduled_payments.get_all_0(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadScheduledPayment3`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_scheduled_payment3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/scheduled-payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.standing_orders.get`<a id="openbankingaccountandtransactionstanding_ordersget"></a>

Get Standing Orders

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = openbankingaccountandtransaction.standing_orders.get(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadStandingOrder6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_standing_order6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/standing-orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.standing_orders.get_all`<a id="openbankingaccountandtransactionstanding_ordersget_all"></a>

Get Standing Orders

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.standing_orders.get_all(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadStandingOrder6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_standing_order6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/standing-orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.statements.get`<a id="openbankingaccountandtransactionstatementsget"></a>

Get Statements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = openbankingaccountandtransaction.statements.get(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
    from_statement_date_time="1970-01-01T00:00:00.00Z",
    to_statement_date_time="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

##### from_statement_date_time: `datetime`<a id="from_statement_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter statements FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

##### to_statement_date_time: `datetime`<a id="to_statement_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter statements TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadStatement2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_statement2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/statements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.statements.get_all`<a id="openbankingaccountandtransactionstatementsget_all"></a>

Get Statements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = openbankingaccountandtransaction.statements.get_all(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    from_statement_date_time="1970-01-01T00:00:00.00Z",
    to_statement_date_time="1970-01-01T00:00:00.00Z",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### from_statement_date_time: `datetime`<a id="from_statement_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter statements FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

##### to_statement_date_time: `datetime`<a id="to_statement_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter statements TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadStatement2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_statement2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/statements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.statements.get_details`<a id="openbankingaccountandtransactionstatementsget_details"></a>

Get Statements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = openbankingaccountandtransaction.statements.get_details(
    statement_id="StatementId_example",
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### statement_id: `str`<a id="statement_id-str"></a>

StatementId

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadStatement2`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_statement2.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/statements/{StatementId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.statements.get_file`<a id="openbankingaccountandtransactionstatementsget_file"></a>

Get Statements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_response = openbankingaccountandtransaction.statements.get_file(
    statement_id="StatementId_example",
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### statement_id: `str`<a id="statement_id-str"></a>

StatementId

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/statements/{StatementId}/file` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.transactions.get_details`<a id="openbankingaccountandtransactiontransactionsget_details"></a>

Get Transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = openbankingaccountandtransaction.transactions.get_details(
    statement_id="StatementId_example",
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### statement_id: `str`<a id="statement_id-str"></a>

StatementId

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadTransaction6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_transaction6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/statements/{StatementId}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.transactions.get_details_0`<a id="openbankingaccountandtransactiontransactionsget_details_0"></a>

Get Transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_0_response = openbankingaccountandtransaction.transactions.get_details_0(
    account_id="AccountId_example",
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
    from_booking_date_time="1970-01-01T00:00:00.00Z",
    to_booking_date_time="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_id: `str`<a id="account_id-str"></a>

AccountId

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

##### from_booking_date_time: `datetime`<a id="from_booking_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter transactions FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

##### to_booking_date_time: `datetime`<a id="to_booking_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter transactions TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadTransaction6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_transaction6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts/{AccountId}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `openbankingaccountandtransaction.transactions.get_details_1`<a id="openbankingaccountandtransactiontransactionsget_details_1"></a>

Get Transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_1_response = openbankingaccountandtransaction.transactions.get_details_1(
    x_fapi_auth_date="Sun, 48 Jul 7288 80:01:52 UTC",
    x_fapi_customer_ip_address="string_example",
    x_fapi_interaction_id="string_example",
    x_customer_user_agent="string_example",
    from_booking_date_time="1970-01-01T00:00:00.00Z",
    to_booking_date_time="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_fapi_auth_date: `str`<a id="x_fapi_auth_date-str"></a>

The time when the PSU last logged in with the TPP.  All dates in the HTTP headers are represented as RFC 7231 Full Dates. An example is below:  Sun, 10 Sep 2017 19:43:31 UTC

##### x_fapi_customer_ip_address: `str`<a id="x_fapi_customer_ip_address-str"></a>

The PSU's IP address if the PSU is currently logged in with the TPP.

##### x_fapi_interaction_id: `str`<a id="x_fapi_interaction_id-str"></a>

An RFC4122 UID used as a correlation id.

##### x_customer_user_agent: `str`<a id="x_customer_user_agent-str"></a>

Indicates the user-agent that the PSU is using.

##### from_booking_date_time: `datetime`<a id="from_booking_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter transactions FROM NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

##### to_booking_date_time: `datetime`<a id="to_booking_date_time-datetime"></a>

The UTC ISO 8601 Date Time to filter transactions TO NB Time component is optional - set to 00:00:00 for just Date. If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

#### 🔄 Return<a id="🔄-return"></a>

[`OBReadTransaction6`](./open_banking_account_and_transaction_python_sdk/pydantic/ob_read_transaction6.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
