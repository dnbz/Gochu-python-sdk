from typing import TypedDict

class SwapTransaction(TypedDict):
    amount: float
    is_buy: bool
    min_output: float
    token_mint: str
    encryptedData: str

class SimSwap(TypedDict):
    amount: float
    is_buy: bool
    token_mint: str
    encryptedData: str

class TokenDetails(TypedDict):
    token_mint: str
    encryptedData: str