from sqlalchemy import create_engine, MetaData

#Simon
engine = create_engine("postgresql://bvefxzzu:u-fpvrWMxt64toOtgco1hZyySER7vq3_@batyr.db.elephantsql.com/bvefxzzu")
#Daniel
#engine = create_engine("postgresql://fhrmtviw:Zz2OCBJ2GF_MJgCWnMam9SEDfTOMMOTQ@bubble.db.elephantsql.com/fhrmtviw")
meta = MetaData()
conn = engine.connect()
