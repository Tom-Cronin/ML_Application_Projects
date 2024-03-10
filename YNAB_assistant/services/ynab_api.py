import requests


class YnabAPI:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_token}"}

    def fetch_transactions(self, budget_id, since_date=None):
        url = f"{self.base_url}/budgets/{budget_id}/transactions"
        if since_date:
            url += f"?since_date={since_date}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['data']['transactions']
        else:
            raise Exception(f"Failed to fetch transactions: {response.status_code}")

    def fetch_categories(self, budget_id):
        url = f"{self.base_url}/budgets/{budget_id}/categories"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()['data']['category_groups']
        else:
            raise Exception(f"Failed to fetch categories: {response.status_code}")

    def update_transaction_category(self, budget_id, transaction_id, category_id):
        url = f"{self.base_url}/budgets/{budget_id}/transactions/{transaction_id}"
        data = {
            "transaction": {
                "category_id": category_id
            }
        }
        response = requests.patch(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update transaction category: {response.status_code}")

