from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db_conection import meta, engine

users = Table('users', meta, 
              Column('id_user', Integer, primary_key = True),
              Column('name_user', String(100)),
              Column('lastname_user', String(100)),
              Column('email_user', String(100)),
              Column('password_user', String(100)),
              Column('countrie_user', Integer))

#meta.create_all()