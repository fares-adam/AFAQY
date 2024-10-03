from pydantic import field_validator
from datetime import datetime

class UserValidators:

    @staticmethod
    @field_validator('phone')
    def validate_phone(cls, phone):
        if phone is None:
            raise ValueError('phone number is required')
        
        if not str(phone).isnumeric():
            raise ValueError('phone number must be in a of valid format example 1458745122')
        return phone

    @staticmethod
    @field_validator('date_of_birth')
    def validate_age(cls, date):
        if date is None:
            raise ValueError('date of birth is required')
        
        if date:
            today = datetime.today().date()
            age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
            if age < 18:
                raise ValueError('user must be at least 18 years old')
        return date

    @staticmethod
    @field_validator('city')
    def validate_city(cls, city):
        if city is None:
            raise ValueError('city is required')
        
        if not city.replace(" ", "").isalpha():
            raise ValueError('city name must contain only letters')
        return city

    @staticmethod
    @field_validator('password')
    def validate_password(cls, pwd):
        if pwd is None:
            raise ValueError('password is required')
        
        if len(pwd) < 4:
            raise ValueError('password must be at least 4 characters long')
        return pwd
