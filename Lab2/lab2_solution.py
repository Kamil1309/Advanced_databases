from sqlalchemy import create_engine, MetaData, Table


db_string = "postgres://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"

db = create_engine(db_string)

