#!/usr/bin/env bash

pip install -r requirements.txt

while ! pg_isready -q -h $PGHOST -p $PGPORT -U $PGUSER
do
  echo "$(date) - waiting for database to start"
  sleep 2
done

# Create, migrate, and seed database if it doesn't exist.
if [[ -z `psql -Atqc "\\list $PGDATABASE"` ]]; then
  echo "Database $PGDATABASE does not exist. Creating..."
  createdb -E UTF8 $PGDATABASE -l en_US.UTF-8 -T template0
  echo "Database $PGDATABASE created."
fi

# Create test database if it doesn't exist.
if [[ -z `psql -Atqc "\\list $PGDATABASETEST"` ]]; then
  echo "Database $PGDATABASE does not exist. Creating..."
  createdb -E UTF8 $PGDATABASE -l en_US.UTF-8 -T template0
  echo "Database $PGDATABASE created."
fi

#echo db init
#python manage.py db init
#echo db migrate
#python manage.py db migrate
#echo db upgrade
#python manage.py db upgrade
#
#python manage.py test

python app.py
