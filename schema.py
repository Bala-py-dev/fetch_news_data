from typing import List
from pydantic import BaseModel
from datetime import datetime


class PatientSchemaIn(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    user_name: str
    role: str
    gender: str
    race: str
    phone_number: str
    language: str
    address: str
    state: str
    city: str
    zip_code: int
    date_of_birth: str
    medical_condition: str
    medication: str
    physician: str
    password: str
    
class PatientSchemaOut(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    user_name: str
    user_id: int
    role: str
    gender: str
    race: str
    phone_number: str
    language: str
    address: str
    state: str
    city: str
    zip_code: int
    date_of_birth: str
    medical_condition: str
    medication: str
    physician: str
    created_at: datetime
    updated_at: datetime
    
class ProviderSchemaIn(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    user_name: str
    role: str
    gender: str
    race: str
    phone_number: str
    language: str
    address: str
    state: str
    city: str
    zip_code: int
    provider_id: str
    employee_id: str
    speciality: str
    certification: str
    department_id: int
    admin: str
    password: str
    start_dt: str
    end_dt: str
    
class ProviderSchemaOut(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    email: str
    user_name: str
    user_id: int
    role: str
    gender: str
    race: str
    phone_number: str
    language: str
    address: str
    state: str
    city: str
    zip_code: int
    provider_id: str
    employee_id: str
    speciality: str
    certification: str
    department_id: int
    admin: str
    start_dt: str
    end_dt: str
    created_at: datetime
    updated_at: datetime
    
class LoginSchemaIn(BaseModel):
    user_name: str
    password: str
    
class LoginSchemaOut(BaseModel):
    access_token: str
    token_type: str
    