from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
users = {}
transaction_fee = 0.01
@app.get("/",response_class=HTMLResponse)
def mgs():
    return """
    <html>
        <head>
            <title>Wilbard Mobile Money Transaction</title>
        </head>
        <body>
            <h1>Welcome to our Mobile Money Service</h1>
            <h1>Register Account</h1>
            <p>To register an account, please provide your name, phone number, and a password. This information will be used to create your account and ensure the security of your transactions.</p>
            <form action="register" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <br>
                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required>
                <br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
                <br>
                <input type="submit" value="Register">
            </form>
             <h1>Perform Transactions</h1>
            <p>Use the Correct password to perform transactions and manage your account.</p>
        </body>
    </html>
    """

@app.post("/register")
def register(name: str, phone_number: str, password: str):
    if phone_number in users:
        return {"message": "Phone number already registered."}
    users[phone_number] = {"name": name, "password": password, "balance": 0}
    return {"message": "Account registered successfully."}
@app.get("/users",response_class=HTMLResponse)
def get_users():
    user_list = "<h1>Registered Users</h1><ul>"
    for phone, info in users.items():
        user_list += f"<li>{info['name']} - {phone}</li>"
    user_list += "</ul>"
    return user_list