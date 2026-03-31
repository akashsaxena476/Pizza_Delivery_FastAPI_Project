from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int] = None
    username:str
    email:str
    password:str
    is_staff:Optional[bool] = None
    is_active:Optional[bool] = None

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key : str = '7b10a8807b05bccc0acb80e9ce5f172d21893c81d266a911546d29b862051a54'

class LoginModel(BaseModel):
    username:str
    password:str



class OrderModel(BaseModel):
    id:Optional[int]
    quantity: int
    order_status:Optional[str] = "PENDING"
    pizza_size:Optional[str] = "SMALL"
    user_id:Optional[int]


    class Config:
        from_attributes = True
        json_schema_extra = {
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str] = "PENDING"

    class Config:
        from_attributes=True
        json_schema_extra = {
            "example":{
                "order_status":"PENDING"
            }
        }


