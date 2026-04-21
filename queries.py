# this is query A.
# creating every column of every product
import sqlite3
conn = sqlite3.connect('nyondo_stock.db')
conn.execute('''
SELECT *
FROM products;             

''')
print("\nQuery A Results:")
print(conn.execute('SELECT * FROM products;').fetchall())
#this is the second query B. Get only the name and price of all products
conn.execute('''
SELECT name,price
FROM products;
''')
print("\nQuery B Results:")
print(conn.execute('SELECT name, price FROM products;').fetchall())
# this is query c

# this query C. Get full details of the product with id = 3
conn.execute('''
SELECT name,price
FROM products
WHERE id = 3;
''')
print("\nQuery C Results:")
print(conn.execute('SELECT * FROM products WHERE id = 3;').fetchall())
# this is query D use the particial match
conn.execute('''
SELECT name
FROM products
WHERE name LIKE '%sheet%';
''')
print("\nQuery D Results:")
print(conn.execute("SELECT * FROM products WHERE name LIKE '%sheet%';").fetchall())
# this is query E
conn.execute('''
SELECT *
FROM products
ORDER BY price DESC;
''')
print("\nQuery E Results:")
print(conn.execute('SELECT * FROM products ORDER BY price DESC;').fetchall())
# this is query f
conn.execute('''
SELECT *
FROM products
ORDER BY price DESC
LIMIT 2;
''')
print("\nQuery F Results:")
print(conn.execute('SELECT * FROM products ORDER BY price DESC LIMIT 2;').fetchall())
# this is Query G updating the price of cement
conn.execute('''
UPDATE products
SET
Price = 38000
WHERE id = 1;
''')
conn.commit()
print("\nQuery G Results (Updated Cement):")
print(conn.execute('SELECT * FROM products WHERE id = 1;').fetchall())

