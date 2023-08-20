from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer, Numeric
from config.db_conection import meta,engine

countries = Table('countries', meta, 
              Column('countrie_id', Integer, primary_key = True),
              Column('countrie_name', String(30)))

meta.create_all(engine)