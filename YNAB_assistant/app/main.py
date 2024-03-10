from datetime import datetime

import config
from services.ynab_api import YnabAPI

ynab_api = YnabAPI(config.YNAB['api_base_ulr'], config.YNAB['api_key'])
# response = ynab_api.fetch_transactions(config.YNAB['budget_id'], since_date=datetime.now().strftime('%Y-%m-%d'))
response = ynab_api.fetch_categories(config.YNAB['budget_id'])
for category_parent in response:
    for sub_category in category_parent.get('categories'):
        print(category_parent.get('name') + ": " + sub_category.get('name'))
