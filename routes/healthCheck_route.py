from fastapi import APIRouter

health_check = APIRouter()

@health_check.get("/")
def validate_healthCheck():
    return "Working correctly."