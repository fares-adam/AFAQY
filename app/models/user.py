from datetime import date
from bson import ObjectId
from typing import Dict, Optional
from pydantic import BaseModel, EmailStr, Field, SecretStr
from app.validators.user_validators import UserValidators 
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from typing import Literal


PyObjectId = Annotated[str, BeforeValidator(str)]




class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, ObjectId):
            return str(v)  # Convert ObjectId to string
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return v  # If it's already a valid string, return as is

    @classmethod
    def __get_pydantic_json_schema__(cls, schema_or_field, handler):
        """Customize schema for ObjectId."""
        if isinstance(schema_or_field, dict):
            schema_or_field.update(type="string")
        return schema_or_field


class User(BaseModel):
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    date_of_birth: Optional[date] = Field(default=None, example="1990-01-01")
    phone: str = Field(..., example="123-456-7890")
    gender: Optional[Literal["male", "female"]] = Field(default=None, example="male")
    city: str = Field(example="New York")
    role : Literal["user","admin"] = Field(default="user")
    password: Optional[SecretStr] = None
    weather: Optional[Dict] = Field(default=None)
    state : Optional[Literal["active", "inactive", "suspended"]] = Field(default = None)
    _validate_phone = UserValidators.validate_phone
    _validate_age = UserValidators.validate_age
    _validate_city = UserValidators.validate_city
    _validate_password = UserValidators.validate_password
    class Config:
        from_attributes = True
        # enable aliases
        populate_by_name = True 