from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import ProductUpdate
from services import update_product_service

app = FastAPI()

@app.put("/products/{product_id}", status_code=status.HTTP_200_OK)
def update_product(
    product_id: int, 
    product_update: ProductUpdate, 
    db: Session = Depends(get_db)
):
    # Gọi logic xử lý từ tầng Service
    updated_product = update_product_service(
        db=db, 
        product_id=product_id, 
        product_update=product_update
    )

    return {
        "message": "Product updated successfully",
        "data": {
            "id": updated_product.id,
            "sku": updated_product.sku,
            "name": updated_product.name,
            "price": updated_product.price
        }
    }