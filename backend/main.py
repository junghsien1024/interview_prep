from backend.KVcache import KVCache
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Interview Prep API", version="1.0.0")

# Shared KV cache instance (persists across requests)
kv_cache = KVCache()

# CORS middleware to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    message: str
    status: str


class ItemRequest(BaseModel):
    key: str
    value: str


class ItemResponse(BaseModel):
    key: str
    value: str


class ItemUpdateRequest(BaseModel):
    value: str


class MessageResponse(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "Interview Prep API is running"}


@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        message="Backend is connected and running!",
        status="healthy"
    )

@app.get("/item/{key}", response_model=ItemResponse)
async def get_item(key: str):
    """Retrieve a value from the cache by key"""
    value = kv_cache.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail=f"Item with key '{key}' not found")
    return ItemResponse(key=key, value=value)


@app.post("/item", response_model=ItemResponse)
async def put_item(item: ItemRequest):
    """Store a key-value pair in the cache (creates or updates)"""
    kv_cache.put(item.key, item.value)
    return ItemResponse(key=item.key, value=item.value)


@app.put("/item/{key}", response_model=ItemResponse)
async def update_item(key: str, item: ItemUpdateRequest):
    """Update an existing item's value in the cache"""
    # Check if key exists
    if kv_cache.get(key) is None:
        raise HTTPException(status_code=404, detail=f"Item with key '{key}' not found")
    
    kv_cache.put(key, item.value)
    return ItemResponse(key=key, value=item.value)


@app.delete("/item/{key}", response_model=MessageResponse)
async def delete_item(key: str):
    """Delete an item from the cache"""
    deleted = kv_cache.delete(key)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Item with key '{key}' not found")
    return MessageResponse(message=f"Item with key '{key}' deleted successfully") 



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
