from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="FastAPI on Vercel", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def root():
    return {
        "message": "Hello from FastAPI on Vercel!",
        "status": "success",
        "endpoints": [
            "GET /",
            "GET /items/{item_id}",
            "POST /items/",
            "GET /health"
        ]
    }

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q,
        "message": f"Item {item_id} retrieved successfully"
    }

@app.post("/items/")
async def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item.dict(),
        "total_price": item.price + (item.tax or 0)
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "FastAPI"}

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)