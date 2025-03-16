# GochuPy SDK

A Python SDK for interacting with the Gochu API. This SDK provides easy-to-use methods for token operations and swap transactions.

## Features

- Token details retrieval
- Swap transaction execution
- Swap simulation/quote generation
- Mints listing with pagination

## Installation
Install dependencies:
```bash
pdm install
```

3. Create a `.env` file in the project root:
```env
SECRET_KEY=your_secret_key
ACCESS_KEY=your_access_key
```

## Usage

### Initialize the SDK

```python
from gochu_sdk.api import GochuFun
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize SDK
gochu = GochuFun({
    'secret_key': os.getenv('SECRET_KEY'),
    'access_key': os.getenv('ACCESS_KEY')
})
```

### Get Token Details

```python
import os
from gochu_sdk.api import GochuFun

gochu = GochuFun(
    access_key=os.getenv('ACCESS_KEY'),
    secret_key=os.getenv('SECRET_KEY')
)
token_details = {
    "token_mint": "your_token_mint",
    "encryptedData": gochu.secret_key
}
response = gochu.get_token(token_details)
```

### Simulate Swap

```python
import os
from gochu_sdk.api import GochuFun

gochu = GochuFun(
    access_key=os.getenv('ACCESS_KEY'),
    secret_key=os.getenv('SECRET_KEY')
)
sim_transaction = {
    "amount": 1.0,
    "is_buy": True,
    "token_mint": "your_token_mint",
    "encryptedData": gochu.secret_key
}
quote = gochu.simulate_swap_transaction(sim_transaction)
```

### Execute Swap Transaction

```python
swap_transaction = {
    "amount": 1.0,
    "is_buy": True,
    "min_output": 0.95,
    "token_mint": "your_token_mint",
    "encryptedData": gochu.secret_key
}
response = gochu.send_swap_transaction(swap_transaction)
```

### Get All Mints

```python
mints = gochu.get_all_mints(
    page=1,
    per_page=10,
    sort="recently_created"
)
```

## Type Definitions

The SDK includes TypedDict classes for type safety:

- `TokenDetails`: Token information
- `SimSwap`: Swap simulation parameters
- `SwapTransaction`: Swap transaction parameters


### Example usage
```python
import os
from dotenv import load_dotenv
from gochu_sdk.api import GochuFun
from gochu_sdk.types import SwapTransaction, SimSwap, TokenDetails

# Load environment variables
load_dotenv()

# Token mint
TOKEN_MINT = '<MINT>'

# Initialize SDK
gochu = GochuFun({
    'secret_key': os.getenv('SECRET_KEY'),
    'access_key': os.getenv('ACCESS_KEY')
})


# Example: Get token details
token_details: TokenDetails = {
    "token_mint": TOKEN_MINT,
    "encryptedData": gochu.secret_key
}
# token_response = gochu.get_token(token_details)

# Example: Simulate swap
sim_transaction: SimSwap = {
    "amount": 1.0,
    "is_buy": True,
    "token_mint": TOKEN_MINT,
    "encryptedData": gochu.secret_key
}
# quote = gochu.simulate_swap_transaction(sim_transaction)

# Example: Send swap transaction
swap_transaction: SwapTransaction = {
    "amount": 1.0,
    "is_buy": True,
    "min_output": 0.95,
    "token_mint": TOKEN_MINT,
    "encryptedData": gochu.secret_key
}
# swap_response = gochu.send_swap_transaction(swap_transaction)

# Get specific page with custom settings
custom_mints = gochu.get_all_mints(
    page=1,
    per_page=10,
    sort="recently_created"
)
```
