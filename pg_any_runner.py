import argparse
import psycopg2
from time import time, sleep

parser = argparse.ArgumentParser(description='Execute SQL command at a given rate for a specified duration.')
parser.add_argument('--conn', type=str, required=True, help='Postgres connection string')
parser.add_argument('--duration', type=int, default=300, help='Duration in seconds (default: 300)')
parser.add_argument('--sql', type=str, required=True, help='SQL command to execute')
parser.add_argument('--rate', type=int, default=1, help='Number of times to execute the SQL command before pausing for a second (default: 1)')

args = parser.parse_args()

conn = psycopg2.connect(args.conn)
cur = conn.cursor()

start_time = time()
print('Starting to execute {args.sql}...')
while time() - start_time < args.duration:
    for _ in range(args.rate):
        cur.execute(args.sql)
    conn.commit()
    print(f'Executed "{args.sql}" {args.rate} times')
    sleep(1)

cur.close()
conn.close()
