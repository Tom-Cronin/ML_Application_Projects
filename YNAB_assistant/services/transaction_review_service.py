class TransactionReviewService:
    def __init__(self, ynab_api):
        self.ynab_api = ynab_api
        self.transactions_for_review = []

    def flag_transactions_for_review(self, budget_id, since_date=None):
        transactions = self.ynab_api.fetch_transactions(budget_id, since_date)
        for transaction in transactions:
            if not transaction['category_id'] or transaction['category_name' == "To Be Categorized"]:
                self.transactions_for_review.append(transaction)

    def get_transactions_for_review(self):
        return self.transactions_for_review
