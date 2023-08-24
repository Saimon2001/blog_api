from fastapi import APIRouter
from config.db_conection import conn
from models.main import countries
from schemas.main import Countrie

countrie = APIRouter()

@countrie.get("/countries")
def get_countries():
    #result = conn.execute(countries.select()).fetcall()
    result = conn.execute('SELECT * FROM countries').fetchall()
    return result

@countrie.post("/countries")
def create_countrie( countrie: Countrie):
    new_countrie = {
        "countrie_id": countrie.countrie_id,
        "countrie_name": countrie.countrie_name
    }
    conn.execute( countries.insert().values(new_countrie))
    return new_countrie




