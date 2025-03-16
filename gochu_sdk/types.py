# gochu_types.py
# Type aliases for transaction data structures using native Python generics.

# Expected keys for SwapTransaction:
# 'amount' (float), 'is_buy' (bool), 'min_output' (float), 'token_mint' (str), 'encryptedData' (str)
SwapTransaction = dict[str, float | bool | str]

# Expected keys for SimSwap:
#   'amount' (float), 'is_buy' (bool), 'token_mint' (str), 'encryptedData' (str)
SimSwap = dict[str, float | bool | str]

# Expected keys for TokenDetails:
#   'token_mint' (str), 'encryptedData' (str)
TokenDetails = dict[str, str]
