import requests
from dataclasses import dataclass
from typing import Optional
from gochu_types import SwapTransaction, SimSwap, TokenDetails

@dataclass
class GochuFun:
    secret_key: str
    access_key: str
    base_url: str = "https://gochu-contract-caller-production.up.railway.app"

    def __init__(self, config: dict):
        self.secret_key = config['secret_key']
        self.access_key = config['access_key']

    def _make_request(self, endpoint: str, data: dict) -> Optional[dict]:
        """Internal method to make API requests"""
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_key}"
            }

            response = requests.post(
                f"{self.base_url}{endpoint}",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as error:
            print(f"Error making request: {error}")
            return None

    def get_token(self, transaction: TokenDetails) -> Optional[dict]:
        """Get token details from the API"""
        return self._make_request("/api/v1/token/get", transaction)

    def send_swap_transaction(self, transaction: SwapTransaction) -> Optional[dict]:
        """Send swap transaction to the API"""
        return self._make_request("/api/v1/tx/createswaptransaction", transaction)

    def simulate_swap_transaction(self, transaction: SimSwap) -> Optional[dict]:
        """Get a quote for a swap transaction"""
        return self._make_request("/api/v1/tx/simulatetransaction", transaction)
    
    def get_all_mints(self, page: int = 1, per_page: int = 10, sort: str = "recently_created") -> Optional[dict]:
        """
        Fetch all mints from the Gochu API
        
        Args:
            page (int): Page number (default: 1)
            per_page (int): Items per page (default: 10)
            sort (str): Sort criteria (default: "recently_created") or "last_traded"
        
        Returns:
            Dict | None: List of mints or None if error occurs
        
        Example:
            >>> mints = gochu.get_all_mints(page=1, per_page=20)
        """
        try:
            url = f"https://handlers.gochu.fun/fetchAllMints.php"
            params = {
                "page": page,
                "perPage": per_page,
                "sort": sort
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as error:
            print(f"Error fetching mints: {error}")
            return None