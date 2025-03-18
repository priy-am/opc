
# 🚀 FastAPI Order Management Microservice

## 📚 Description
This is a simple **Order Management API** built with **FastAPI** and **PostgreSQL**.  
It is a refactored version of a PHP monolithic system optimized for microservices.

---

## 🛠 Tech Stack
- **FastAPI** - Python Web Framework
- **PostgreSQL** - Database
- **asyncpg** - Async PostgreSQL Driver
- **python-dotenv** - For environment variable management
- **Pydantic** - Data validation

---

## 📦 Project Structure
```
.
├── app
│   ├── main.py        # FastAPI application
│   └── __init__.py
├── .env               # Environment variables (DB URL)
├── requirements.txt   # Python dependencies
└── README.md
```

---

## ⚙️ Setup Instructions

###  Clone the repository


###  Install Dependencies
```bash
pip install -r requirements.txt
```

###  Setup PostgreSQL Database
- Create a database named `orders_db`
- Create the `orders` table:
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
```

###  Configure Environment Variables
Create a `.env` file in the root:
```
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/orders_db
```

###  Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

---

## 📬 API Endpoint

### ➤ POST `/order`
Create a new order.

#### ✅ Request Body:
```json
{
  "customer_name": "John Doe",
  "product_name": "Laptop",
  "price": 1200.50
}
```

#### ✅ Success Response:
```json
{
  "status": "success",
  "order_id": 1
}
```

---

## 📝 Example `.env`
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/orders_db
```

---

## 💻 Example Run Command
```
uvicorn app.main:app --reload
```

Access API at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---


