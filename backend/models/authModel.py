from pydantic import BaseModel,EmailStr,field_validator,Field
# from typing import E
from enum import Enum
from datetime import datetime ,timezone
from typing import Union,Optional

class RolesEnum(str,Enum):
    seller='seller'
    buyer='buyer'  
class User(BaseModel):
    name: str =Field(...)
    email: EmailStr =Field(...)
    password: str =Field(...,min_length=6) 
    role: Optional[RolesEnum] =Field(default=RolesEnum.buyer)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
    @field_validator('name')
    def validate_name(cls,value):
        if len(value)<3:
            raise ValueError('name must be at least 3 characters')
        return value
    
class RegisterUser(User):
    pass