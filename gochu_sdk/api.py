import logging

import httpx


class GochuFun:
    API_BASE_URL = "https://gochu-contract-caller-production.up.railway.app"

    def __init__(self, access_key: str):
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

    def get_token(self, token_mint: str, encrypted_data: str) -> dict | None:
        """Get token details from the API"""
        transaction = {"token_mint": token_mint, "encryptedData": encrypted_data}
        return self._make_request("/api/v1/token/get", transaction)

    def send_swap_transaction(
            self,
            amount: float,
            is_buy: bool,
            min_output: float,
            token_mint: str,
            private_key: str
    ) -> dict | None:
        """Send swap transaction to the API"""
        transaction = {
            "amount": amount,
            "is_buy": is_buy,
            "min_output": min_output,
            "token_mint": token_mint,
            "privateKey": private_key
        }
        return self._make_request("/api/v1/tx/createswaptransaction", transaction)

    def simulate_swap_transaction(
            self,
            amount: float,
            is_buy: bool,
            token_mint: str,
            encrypted_data: str
    ) -> dict | None:
        """Get a quote for a swap transaction"""
        transaction = {
            "amount": amount,
            "is_buy": is_buy,
            "token_mint": token_mint,
            "encryptedData": encrypted_data
        }
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
