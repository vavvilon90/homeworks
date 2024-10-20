import sqlite3

connection = sqlite3.connect("initiate.db")
cursor = connection.cursor()
def initiate_db():
    connection = sqlite3.connect("initiate.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    """)
    connection.commit()
    connection.close()


initiate_db()



#for i in range(1, 5):
#    cursor.execute(f'''
#    INSERT INTO Products (title, description, price) VALUES ('Product {i}', 'описание {i}', '{i*100}')
#''')
#    connection.commit()


def get_all_products():
    connection = sqlite3.connect("initiate.db")
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products