from fastapi import FastAPI
from routes.main import health_check

app = FastAPI()


app.include_router(health_check)