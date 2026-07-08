from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import ProductModel
from schemas import ProductUpdate

def update_product_service(db: Session, product_id: int, product_update: ProductUpdate):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found"
        )

    product.name = product_update.name
    product.price = product_update.price

    db.commit()
    db.refresh(product)
    
    return product