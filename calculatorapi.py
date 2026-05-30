from fastapi import FastAPI, HTTPException
app = FastAPI()
@app.get("/calculate/{operation}")
async def calculate(operation: str, num1: float, num2: float):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = num1 / num2
    else:
        raise HTTPException(status_code=402, detail="KeyError")

    return {
        "operation": operation,
        "numbers": [num1, num2],
        "result": result
    }
