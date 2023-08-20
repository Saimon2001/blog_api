from fastapi import APIRouter
from config.db_conection import conn
from models.main import countries

countrie = APIRouter()

@countrie.get("/countrie")
def get_countries():
    return conn.execute( countries.select())