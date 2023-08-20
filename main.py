from fastapi import FastAPI
from routes.main import health_check, countrie
import sys

sys.setrecursionlimit(1500)

app = FastAPI()


app.include_router(health_check)
app.include_router(countrie)