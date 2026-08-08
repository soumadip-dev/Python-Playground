from fastapi import FastAPI

app = FastAPI()

customer_accounts = {
    101: {
        "savings": [
            {"transaction_id": 1, "amount": 5000},
            {"transaction_id": 2, "amount": -1200},
        ],
        "current": [
            {"transaction_id": 3, "amount": 15000},
        ],
    },
    102: {
        "savings": [
            {"transaction_id": 4, "amount": 1000},
            {"transaction_id": 5, "amount": -2000},
        ],
        "current": [
            {"transaction_id": 6, "amount": 2000},
            {"transaction_id": 7, "amount": 3000},
        ],
    },
}


@app.get("/customer/{customer_id}/account/{account_type}")
def get_customer_transactions(customer_id: int, account_type: str):
    if customer_id not in customer_accounts:
        return {
            "message": f"No records found for customer ID {customer_id}.",
            "data": None,
        }

    if account_type not in customer_accounts[customer_id]:
        return {
            "message": (
                f"'{account_type}' account does not exist "
                f"for customer ID {customer_id}."
            ),
            "data": None,
        }

    transaction_history = customer_accounts[customer_id][account_type]

    return {
        "message": "Transaction history retrieved successfully.",
        "data": {
            "customer_id": customer_id,
            "account_type": account_type,
            "transactions": transaction_history,
        },
    }
