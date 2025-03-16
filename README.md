# GochuPy SDK

A Python SDK for interacting with the Gochu API. This SDK provides easy-to-use methods for token operations and swap transactions.

## Features

- Token details retrieval
- Swap transaction execution
- Swap simulation/quote generation
- Mints listing with pagination

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/gochupy.git
cd gochupy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```env
SECRET_KEY=your_secret_key
ACCESS_KEY=your_access_key
```

## Usage

### Initialize the SDK

```python
from gochu_sdk import GochuFun
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
token_details = {
    "token_mint": "your_token_mint",
    "encryptedData": gochu.secret_key
}
response = gochu.get_token(token_details)
```

### Simulate Swap

```python
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
