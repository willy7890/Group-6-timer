from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class ATMTransaction(BaseModel):
    account_id: str
    pin: str
    amount: float = Field(gt=0)

class TransferRequest(BaseModel):
    sender_id: str
    pin: str
    receiver_id: str
    amount: float = Field(gt=0)

app = FastAPI(title="MGS ATM API")

ACCOUNTS = {
    "1": {"name": "Wilbard", "pin": "1111", "balance": 50.0},
    "2": {"name": "John", "pin": "2222", "balance": 10.0}
}

@app.post("/deposit")
async def deposit(tx: ATMTransaction):
    #deposit
    if tx.account_id not in ACCOUNTS:
        raise HTTPException(status_code=404, detail="account detail Not found Try again")
    
    if ACCOUNTS[tx.account_id]["pin"] != tx.pin:
        raise HTTPException(status_code=401, detail="Incorrect PIN")

    ACCOUNTS[tx.account_id]["balance"] += tx.amount
    return {
        "message": f"Successfully deposited {tx.amount} TZS",
        "new_balance": ACCOUNTS[tx.account_id]["balance"]
    }

@app.post("/transfer")
async def transfer(req: TransferRequest):
    """Transfer money from one NMB account to another"""
    if req.sender_id not in ACCOUNTS or req.receiver_id not in ACCOUNTS:
        raise HTTPException("One or both accounts not found")
    
    sender = ACCOUNTS[req.sender_id]
    
    if sender["pin"] != req.pin:
        raise HTTPException(status_code=401, detail="Incorrect PIN")
        
    if sender["balance"] < req.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds for transfer")

    # Perform the transfer
    sender["balance"] -= req.amount
    ACCOUNTS[req.receiver_id]["balance"] += req.amount
    
    return {"message": f"Transferred {req.amount} to {req.receiver_id}"}

@app.post("/withdraw")
async def withdraw(tx: ATMTransaction):
    if tx.account_id not in ACCOUNTS:
        raise HTTPException(status_code=404, detail="Account not found")
    
    account = ACCOUNTS[tx.account_id]
    if account["pin"] != tx.pin:
        raise HTTPException(status_code=401, detail="Incorrect PIN")
    
    if account["balance"] < tx.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")
    
    account["balance"] -= tx.amount
    return {"message": "Withdrawal successful", "remaining": account["balance"]}
