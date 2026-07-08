from pydantic import BaseModel

class ProductUpdate(BaseModel):
    name: str
    price: float

class ProductResponse(BaseModel):
    id: int
    sku: str
    name: str
    price: float

    class Config:
        from_attributes = True