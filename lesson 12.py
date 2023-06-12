# from sqlite3 import connect
#
#
# conn = connect('db.sqlite3')
# cur = conn.cursor()
#
#
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS category(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(24) NOT NULL UNIQUE
#     );
# ''')
# conn.commit()

# cur.executemany('''
#     INSERT INTO category (name)
#     VALUES (?);
# ''', (('Coffe', ), ('Tea', )))
# conn.commit()

# cur.execute('''
#     DELETE FROM category
#     WHERE id >= ? OR name = ?;
# ''', (3, 'Tea'))
# conn.commit()


# cur.execute('''
#     UPDATE category SET name = ? WHERE id = ?;
# ''', ('Кофе', 1))
# conn.commit()

# cur.execute('''
#     SELECT * FROM category
#     ORDER BY id ASC;
# ''')
# print(cur.fetchall())
from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor


conn = connect('postgresql://belhard:belhard@localhost:5432/belhard')


with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
    cur.execute('select * from category;')
    for category in cur.fetchall():
        print(category.name)

# with conn.cursor() as cur:
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS category(
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(64) NOT NULL UNIQUE
#         );
#     ''')
#     conn.commit()


# with conn.cursor() as cur:
#     cur.execute('''
#         CREATE TABLE IF NOT EXISTS post(
#             id SERIAL PRIMARY KEY,
#             title VARCHAR(128) NOT NULL,
#             description TEXT NOT NULL,
#             date_publish TIMESTAMP DEFAULT NOW(),
#             category_id INTEGER NOT NULL,
#             FOREIGN KEY (category_id) REFERENCES category(id)
#         );
#     ''')
#     conn.commit()

# with conn.cursor() as cur:
#     # cur.executemany('''
#     #     INSERT INTO category (name)
#     #     VALUES (%s);
#     # ''', (('Finance', ), ('Sport', )))
#     # conn.commit()
#     cur.execute('''
#         INSERT INTO post (title, description, category_id)
#         VALUES (%s, %s, %s);
#     ''', ('Post 1', 'Description', 1))
#     conn.commit()

# with conn.cursor() as cur:
#     cur.execute('''
#         SELECT category.name, post.title FROM category
#         LEFT JOIN post ON post.category_id = category.id
#         ORDER BY category.name;
#     ''')
#     print(cur.fetchall())