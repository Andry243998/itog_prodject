import psycopg2

DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'trofimov'
DB_USER = 'postgres'
DB_PASSWORD = '12345678'

conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()
    
create_table_query = '''
CREATE TABLE IF NOT EXISTS test_table (
    "ID" INT,
    "Name" VARCHAR(30),
    "Age" INT,
    "Department" VARCHAR(30));
'''
cursor.execute(create_table_query)
conn.commit()
    
insert_data_query = '''
INSERT INTO test_table VALUES
    (1, 'Maga', 22, 'HR'),
    (2, 'Ramzan', 45, 'Development'),
    (3, 'Sasha', 47, 'Sales'),
    (4, 'Anna', 49, 'Engineering'),
    (5, 'Vasiliy', 20, 'Development'),
    (6, 'Gleb', 18, 'DevOps' ),
    (7, 'Andry', 29, 'Testing'),
    (8, 'Nastya', 33, 'Sales'),
    (9, 'Kristina', 39, 'HR'),
    (10, 'Marina', 19, 'DevOps'),
    (11, 'Iosif', 50, 'DevOps'),
    (12, 'Denis', 19, 'Sales'),
    (13, 'Anton', 26, 'Testing');
'''
cursor.execute(insert_data_query)
conn.commit()
    
select_query = 'SELECT * FROM test_table;'
cursor.execute(select_query)
rows = cursor.fetchall()
column_names = [desc[0] for desc in cursor.description]

for row in rows:
    row_data = ", ".join(f"{column_names[i]}: {value}" for i, value in enumerate(row))
    print(row_data)
    
cursor.close()
conn.close()
print("Databased connection closed")
