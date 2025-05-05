import psycopg2

conn = psycopg2.connect("dbname=groups user=postgres  password = 7007")

cur = conn.cursor()

# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar(30));")
cur.execute("INSERT INTO test(num,data) values (30,'salomaleykum');")

conn.commit()
cur.close()
conn.close()