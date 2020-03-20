from sqlalchemy import create_engine, MetaData, Table, select, and_, desc, Integer, func, or_


db_string = "postgres://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"

db = create_engine(db_string)

metadata = MetaData()

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
for result in results:
   print(result.first_name, " ", result.last_name, " ", result.title, " ", result.name)


# Ex 3
category = Table('category', metadata , autoload=True, autoload_with=db)

stmt = select([func.count()]).select_from(category)
results = db.execute(stmt).fetchall()

# Print results
print(results[0][0])


# Ex 4
category = Table('category', metadata , autoload=True, autoload_with=db)

stmt = select([category.c.name])

results = db.execute(stmt).fetchmany(size=2)

# Print results
for result in results:
   print(result.name )


# Ex 5
rental = Table('rental', metadata , autoload=True, autoload_with=db)
inventory = Table('inventory', metadata , autoload=True, autoload_with=db)
film = Table('film', metadata , autoload=True, autoload_with=db)

stmt = select([film.c.title, rental.c.rental_date]).where(and_(film.c.film_id == inventory.c.film_id,
                                                        inventory.c.inventory_id == rental.c.inventory_id)).order_by(rental.c.rental_date)



results = db.execute(stmt).fetchmany(size=1)

# Print results
for result in results:
   print(result.title, " ", result.rental_date)


stmt = select([film.c.title, rental.c.rental_date]).where(and_(film.c.film_id == inventory.c.film_id,
                                                        inventory.c.inventory_id == rental.c.inventory_id)).order_by(desc(rental.c.rental_date))



results = db.execute(stmt).fetchmany(size=1)

# Print results
for result in results:
   print(result.title, " ", result.rental_date)


# Ex 6
actor = Table('actor', metadata , autoload=True, autoload_with=db)

stmt = select([actor.c.first_name, actor.c.last_name]).where(or_(actor.c.first_name == "Olympia",
                                                        actor.c.first_name == "Julia",
                                                        actor.c.first_name == "Ellen"))
#stmt = select([actor.c.first_name])


results = db.execute(stmt).fetchall()

# Print results
for result in results:
   print(result.first_name, " ", result.last_name)