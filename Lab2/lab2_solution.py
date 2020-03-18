from sqlalchemy import create_engine, MetaData, Table, select, and_

#Ex 1
db_string = "postgres://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"

db = create_engine(db_string)


# Ex 2

staff = Table('staff', metadata , autoload=True, autoload_with=db)
address = Table('address', metadata , autoload=True, autoload_with=db)
city = Table('city', metadata , autoload=True, autoload_with=db)
country = Table('country', metadata , autoload=True, autoload_with=db)

stmt = select([staff.c.first_name, staff.c.last_name, country.c.country]).where(and_(staff.c.address_id == address.c.address_id,
                                                                                    address.c.city_id == city.c.city_id,
                                                                                    city.c.country_id == country.c.country_id))
results = db.execute(stmt).fetchall()

# Print results
print(results)

actor = Table('actor', metadata , autoload=True, autoload_with=db)
film_actor = Table('film_actor', metadata , autoload=True, autoload_with=db)
film = Table('film', metadata , autoload=True, autoload_with=db)
language = Table('language', metadata , autoload=True, autoload_with=db)

stmt = select([actor.c.first_name, actor.c.last_name, film.c.title, language.c.name]).where(and_(actor.c.actor_id == film_actor.c.actor_id,
                                                                                    film_actor.c.film_id == film.c.film_id,
                                                                                    film.c.language_id == language.c.language_id,
                                                                                    actor.c.first_name == 'Nick',
                                                                                    actor.c.last_name == 'Wahlberg'))
results = db.execute(stmt).fetchall()

# Print results
print(results)