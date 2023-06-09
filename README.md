# pg_query_runner

A program to execute a SQL command at a given rate for a specified duration against a PostgreSQL database.

## Requirements

- Python 3
- `psycopg2` module

You can install the `psycopg2` module using `pip` like this:

```
pip install psycopg2
```

## Usage

To use this program, you need to provide the following command line arguments:

- `--conn`: The PostgreSQL connection string (required)
- `--duration`: The duration in seconds for which the program will run (default: 300)
- `--sql`: The SQL command to execute (required)
- `--rate`: The number of times to execute the SQL command per second (default: 1)

Here's an example that shows how to use the program to insert data into a table for 10 seconds:

```
% python3 pg_any_runner.py --conn "host=localhost dbname=postgres port=5433 user=postgres password=<password>" --sql="insert into test (id, message) values (random()*100, 'from pg_any_runner')" --duration 10
```
