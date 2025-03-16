import logging

import httpx

from gochu_sdk.types import SwapTransaction, SimSwap, TokenDetails


class GochuFun:
    API_BASE_URL = "https://gochu-contract-caller-production.up.railway.app"

    def __init__(self, secret_key: str, access_key: str):
        self.secret_key = secret_key
        self.access_key = access_key
        self.base_url = "https://gochu-contract-caller-production.up.railway.app"

    def _make_request(self, endpoint: str, data: dict) -> dict | None:
        """Internal method to make API requests"""
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.access_key}"
            }
            response = httpx.post(
                f"{self.base_url}{endpoint}",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            return response.json()

        except httpx.RequestError as error:
            logging.error(f"Error making request: {error}")
            return None

    def get_token(self, transaction: TokenDetails) -> dict | None:
        """Get token details from the API"""
        return self._make_request("/api/v1/token/get", transaction)

    def send_swap_transaction(self, transaction: SwapTransaction) -> dict | None:
        """Send swap transaction to the API"""
        return self._make_request("/api/v1/tx/createswaptransaction", transaction)

    def simulate_swap_transaction(self, transaction: SimSwap) -> dict | None:
        """Get a quote for a swap transaction"""
        return self._make_request("/api/v1/tx/simulatetransaction", transaction)

    # noinspection PyMethodMayBeStatic
    def get_all_mints(self, page: int = 1, per_page: int = 10,
                      sort: str = "recently_created") -> dict | None:
        """
        Fetch all mints from the Gochu API

        Args:
            page (int): Page number (default: 1)
            per_page (int): Items per page (default: 10)
            sort (str): Sort criteria (default: "recently_created") or "last_traded"

        Returns:
            Dict | None: List of mints or None if error occurs

        Example:
            mints = gochu.get_all_mints(page=1, per_page=20)
        """
        try:
            url = "https://handlers.gochu.fun/fetchAllMints.php"
            params = {
                "page": page,
                "perPage": per_page,
                "sort": sort
            }
            response = httpx.get(url, params=params)
            response.raise_for_status()
            return response.json()

        except httpx.RequestError as error:
            logging.error(f"Error fetching mints: {error}")
            return None
