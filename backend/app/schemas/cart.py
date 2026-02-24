from typing import Optional

from pydantic import BaseModel, Field


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be than 0)")


class CartItemCreate(CartItemBase):
    pass


class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be than 0)")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="ProductName")
    price: float = Field(..., description="ProductPrice")
    quantity: int = Field(..., gt=0, description="Quantity (must be than 0)")
    subtotal: float = Field(
        ..., description="Total price for this item (price * quantity)"
    )
    image_url: Optional[str] = Field(None, description="Product image URL")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")
