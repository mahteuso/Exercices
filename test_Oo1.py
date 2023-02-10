def create_account(number, user, balance, limit):
    account_1 = {"number": number, "user": user, "balance": balance, "limit": limit}
    return account_1

def extract(account):
    print(f"Your balance is: {account['balance']}")

def deposit(account, value):
    account["balance"] += value

def cash(account, value):
    if account["balance"] <= 0:
        account["limit"] = account["limit"] - value
        account["balance"] = account["limit"]
    else:
        account["balance"] -= value