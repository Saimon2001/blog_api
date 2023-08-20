from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://fhrmtviw:Zz2OCBJ2GF_MJgCWnMam9SEDfTOMMOTQ@bubble.db.elephantsql.com/fhrmtviw")
meta = MetaData()
conn = engine.connect()
