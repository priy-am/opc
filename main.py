
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr, condecimal
from typing import Annotated
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()  

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise Exception("DATABASE_URL is not set in the environment variables")


class OrderCreate(BaseModel):
    customer_name: Annotated[str, constr(min_length=1)]
    product_name: Annotated[str, constr(min_length=1)]
    price: Annotated[float, condecimal(gt=0)]

# Database connection pool
@app.on_event("startup")
async def startup():
    app.state.db = await asyncpg.create_pool(DATABASE_URL)

@app.on_event("shutdown")
async def shutdown():
    await app.state.db.close()

@app.post("/order")
async def create_order(order: OrderCreate):
    query = """
        INSERT INTO orders (customer_name, product_name, price)
        VALUES ($1, $2, $3)
        RETURNING id
    """
    async with app.state.db.acquire() as conn:
        try:
            order_id = await conn.fetchval(query, order.customer_name, order.product_name, float(order.price))
            return {"status": "success", "order_id": order_id}
        except Exception as e:
            print(f"Database error: {e}")
            raise HTTPException(status_code=500, detail="Failed to create order")
