import os
from dotenv import load_dotenv
from gochu_sdk import GochuFun
from gochu_types import SwapTransaction, SimSwap, TokenDetails

# Load environment variables
load_dotenv()

# Token mint
TOKEN_MINT = '5nq21THvKZ8YgLRkW2CwKVzB6JuHGjT6uZhCMczEzchu'

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